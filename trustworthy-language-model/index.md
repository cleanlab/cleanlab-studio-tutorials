# Trustworthy Language Model (TLM)

## The Problem with LLMs
Generative AI and Large Language Models (LLMs) are revolutionizing automation and data-driven decision-making. But there’s a catch: LLMs often produce “hallucinations,” generating incorrect or nonsensical answers that can undermine your business.

## Introducing the Trustworthy Language Model
Cleanlab’s Trustworthy Language Model (TLM) is the solution. It adds a trustworthiness score to every LLM response, letting you know which outputs are reliable and which ones need extra scrutiny. TLM is a robust LLM designed for high-quality outputs and enhanced reliability—perfect for enterprise applications where unchecked hallucinations are unacceptable. Get started with our [quickstart](/tutorials/tlm), or read about [use-cases](https://cleanlab.ai/blog/trustworthy-language-model/) and [benchmarks](https://towardsdatascience.com/benchmarking-hallucination-detection-methods-in-rag-6a03c555f063).

**Key Features**
- Trustworthiness Scores: Each response comes with a trustworthiness score, helping you reliably gauge the likelihood of hallucinations.
- Higher Accuracy: [Rigorous benchmarks](https://cleanlab.ai/blog/trustworthy-language-model/) show TLM consistently produces more accurate results than LLMs alone, or other [hallucination detection methods](https://towardsdatascience.com/benchmarking-hallucination-detection-methods-in-rag-6a03c555f063).
- Scalable API: Designed to handle large datasets, TLM is suitable for most enterprise applications, including data extraction, tagging/labeling, Q&A (RAG), and more.

## Unlocking Enterprise Use Cases

- Retrieval-Augmented Generation: TLM tells you which RAG responses are unreliable by providing a trustworthiness score for every RAG answer relative to a given question. Ensure users don’t lose trust in your Q&A system and review untrustworthy responses to discover possible improvements.
- Chatbots: TLM informs you which LLM outputs you can use directly (refund, reply, auto-triage) and which LLM outputs you should flag or escalate for human review based on the corresponding trustworthiness score. With standard LLM APIs, you do not know which outputs to trust.
- Auto-Labeling: Streamline your data annotation process. TLM auto-labels data with high accuracy and reliable confidence scores. Let LLMs automatically process the subset of the data that they can reliably handle.
- Extraction: TLM tells you which data auto-extracted from documents, databases, transcripts is reliable and which should be double checked for review. This enables teams to transform raw unstructured data into structured data, with less errors and 90% less time spent reviewing outputs.
