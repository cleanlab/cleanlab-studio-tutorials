from datetime import datetime
from openai import OpenAI
import json
import os

def get_todays_date(date_format: str) -> str:
  """A tool that returns today's date in the date format requested."""
  datetime_str = datetime.now().strftime(date_format)
  return datetime_str

todays_date_tool_json = {
  "type": "function",
  "function": {
    "name": "get_todays_date",
    "description": "A tool that returns today's date in the date format requested. Options are: 'YYYY-MM-DD', 'DD', 'MM', 'YYYY'.",
    "parameters": {
      "type": "object",
      "properties": {
        "date_format": {
          "type": "string",
          "enum": ["%Y-%m-%d", "%d", "%m", "%Y"],
          "default": "%Y-%m-%d",
          "description": "The date format to return today's date in."
        }
      },
      "required": ["date_format"],
    }
  }
}

def rag(client, model: str, user_question: str, system_prompt: str, tools: list[dict]) -> str:
  retrieved_context = retrieve_context(user_question)
  question_with_context = form_prompt(user_question, retrieved_context)
  print(f"[internal log] Invoking LLM with prompt + context\n{question_with_context}\n\n")

  messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": question_with_context},
  ]
  
  response_messages = stream_response(client=client, messages=messages, model=model, tools=tools)
  return f"[RAG response] {response_messages.get('content')}"

def retrieve_context(user_question: str) -> str:
  """Mock retrieval function returns same context for any user_question. Replace with actual retrieval step in your RAG system."""
  contexts = """Simple Water Bottle - Amber (limited edition launched Jan 1st 2025)
A water bottle designed with a perfect blend of functionality and aesthetics in mind. Crafted from high-quality, durable plastic with a sleek honey-colored finish.
Price: $24.99 \nDimensions: 10 inches height x 4 inches width"""
  return contexts

def form_prompt(user_question: str, retrieved_context: str) -> str:
  question_with_context = f"Context:\n{retrieved_context}\n\nUser Question:\n{user_question}"
  indented_question_with_context = "\n".join(f"  {line}" for line in question_with_context.splitlines())    # line is just formatting the final prompt for readability in the tutorial
  return indented_question_with_context

def simulate_response_as_message(response: str) -> list[dict]:
  """Commits the response to a conversation history to return back to the model."""
  return {"role": "assistant", "content": response}

def simulate_tool_call_as_message(tool_call_id: str, function_name: str, function_arguments: str) -> dict:
  """Commits the tool call to a conversation history to return back to the model."""
  tool_call_message = {
    "role": "assistant",
    "tool_calls": [{
            "id": tool_call_id,
            "type": "function",
            "function": {
                "arguments": function_arguments,
                "name": function_name
            }
  }]}
  return tool_call_message


def simulate_tool_call_response_as_message(tool_call_id: str, function_response: str) -> dict:
  """Commits the result of the function call to a conversation history to return back to the model."""
  function_call_result_message = {
    "role": "tool",
    "content": function_response,
    "tool_call_id": tool_call_id,
  }
  return function_call_result_message

def stream_response(client, messages: list[dict], model: str, tools: list[dict]) -> str:
    """Processes a streaming response dynamically handling any tool.
    Params:
        messages: message history list in openai format
        model: model name
        tools: list of tools model can call
    Returns:
        response: final response in openai format
    """

    response_stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
        tools=tools,
        parallel_tool_calls=False,  # prevents OpenAI from making multiple tool calls in a single response
    )

    function_arguments = ""
    function_name = ""
    function_call_id = ""
    is_collecting_function_args = False
    collected_messages = []

    for part in response_stream:
        delta = part.choices[0].delta
        finish_reason = part.choices[0].finish_reason

        if not delta.tool_calls:  # Regular response
            chunk_message = part.choices[0].delta.content
            collected_messages.append(chunk_message)
        else:  # Tool call logic
            is_collecting_function_args = True
            tool_call = delta.tool_calls[0]

            if tool_call.id:
                function_call_id = tool_call.id
            if tool_call.function.name:
                function_name = tool_call.function.name
            if tool_call.function.arguments:
                function_arguments += tool_call.function.arguments

        # Process tool call when all arguments are collected
        if finish_reason == "tool_calls" and is_collecting_function_args:
            args = json.loads(function_arguments)
            function_response = _handle_any_tool_call_for_stream_response(function_name, args)
            is_collecting_function_args = False

    # Finalize response
    if finish_reason == "tool_calls":
        tool_call_response_message = simulate_tool_call_response_as_message(function_call_id, function_response)

        # If the tool call resulted in an error, return the message instead of continuing the conversation
        if "error" in tool_call_response_message["content"]:
            return tool_call_response_message

        response = [
            simulate_tool_call_as_message(function_call_id, function_name, function_arguments),
            tool_call_response_message,
        ]
        
        # If needed, extend messages and re-call the stream response
        messages.extend(response)
        response = stream_response(client=client, messages=messages, model=model, tools=tools)  # This recursive call handles the case when a tool calls another tool until all tools are resolved and a final response is returned
    else:
        collected_messages = [m for m in collected_messages if m is not None]
        full_str_response = "".join(collected_messages)
        response = simulate_response_as_message(full_str_response)

    return response


def _handle_any_tool_call_for_stream_response(function_name: str, arguments: dict) -> str:
    """Handles any tool dynamically by calling the function by name and passing in collected arguments.
       Returns a dictionary of the tool output.
       Returns error message if the tool is not found, not callable or called incorrectly.
    """

    try:
        tool_function = globals().get(function_name) or locals().get(function_name)
        if callable(tool_function):
            # Dynamically call the tool function with arguments
            tool_output = tool_function(**arguments)
            return json.dumps(tool_output)
        else:
            return json.dumps({
                "error": f"Tool '{function_name}' not found or not callable.",
                "arguments": arguments,
            })
    except Exception as e:
        return json.dumps({
            "error": f"Exception in handling tool '{function_name}': {str(e)}",
            "arguments": arguments,
        })
    

fallback_answer = "Based on the available information, I cannot provide a complete answer to this question."

system_prompt = f"""
    Answer the user's Question based on the following possibly relevant Context. Follow these rules:
    1. Never use phrases like "according to the context," "as the context states," etc. Treat the Context as your own knowledge, not something you are referencing.
    2. Give a clear, short, and accurate answer. Explain complex terms if needed.
    3. If the answer to the question requires today's date, use the following tool: get_todays_date.
    4. If the Context doesn't adequately address the Question, say: "{fallback_answer}" only, nothing else.

    Remember, your purpose is to provide information based on the Context, not to offer original advice.
"""