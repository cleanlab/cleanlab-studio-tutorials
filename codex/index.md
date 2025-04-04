---
title: Integration Tutorials
sidebar_label: Integration Tutorials
sidebar_position: 5
---

import TutorialFinder from "@site/src/components/TutorialFinder/TutorialFinder";

# Integrating Codex into your RAG application

Here you can find step-by-step developer tutorials to easily integrate Codex with your existing RAG app.
We provide tutorials for many different RAG frameworks, as well as [types of Codex integrations](/codex/concepts/integrations/).

<div className="cl-design-system flex flex-col min-h-[calc(100vh-140px)] justify-between">
<div className="flex flex-col gap-13">
<TutorialFinder decisionTree={
    {
        "questions": {
            "rag": {
                "title": "Select your RAG framework",
                "placeholder": "RAG framework"
            },
            "integration": {
                "title": "Select an integration style",
                "description": "There are multiple [ways to integrate](/codex/concepts/integrations) Codex depending on your current RAG setup.",
                "placeholder": "Integration style"
            }
        },
        "tree": {
            "question": "rag",
            "options": [
                {
                    "value": "OpenAI Assistants",
                    "next": {
                        "question": "integration",
                        "options": [
                            {
                                "value": "Backup (recommended)",
                                "contents": "[Guide: Codex as a Backup with OpenAI Assistants](/codex/tutorials/openai/OpenAIAssistants_CodexAsBackup/)"
                            },
                            {
                                "value": "Tool",
                                "contents": "[Guide: Codex as a Tool with OpenAI Assistants](/codex/tutorials/openai/OpenAIAssistants_AddingCodexAsTool/)"
                            }
                        ]
                    }
                },
                {
                    "value": "LangChain",
                    "contents": "[Guide: Codex as a Tool with LangChain](/codex/tutorials/langchain/langchain_CodexAsTool/)"
                },
                {
                    "value": "LlamaIndex",
                    "contents": "[Guide: Codex as a Tool with LlamaIndex](/codex/tutorials/llama/LlamaIndex_CodexAsTool/)"
                },
                {
                    "value": "AWS Knowledge Bases",
                    "next": {
                        "question": "integration",
                        "options": [
                            {
                                "value": "Backup (recommended)",
                                "contents": "[Guide: Codex as a Backup with AWS Knowledge Bases](/codex/tutorials/aws/AWSBedrock_CodexAsBackup/)"
                            },
                            {
                                "value": "Tool",
                                "contents": "[Guide: Codex as Tool with AWS Knowledge Bases](/codex/tutorials/aws/AWSBedrock_AddingCodexAsTool/)"
                            }
                        ]
                    }
                },
                {
                    "value": "smolagents",
                    "contents": "[Guide: Codex as a Tool with smolagents](/codex/tutorials/smolagents/smolagents_AddingCodexAsTool/)"
                },
                {
                    "value": "Other RAG Frameworks",
                    "next": {
                        "question": "integration",
                        "options": [
                            {
                                "value": "Tool",
                                "contents": "[Guide: Codex as a Tool with any RAG framework](/codex/tutorials/other_rag_frameworks/OtherRAG_CodexAsTool/)"
                            },
                            {
                                "value": "Backup",
                                "contents": "[Guide: Codex as a Backup with any RAG framework](/codex/tutorials/advanced/validator/)"
                            }
                        ]
                    }
                }
            ]
        }
    }
} />
</div>
</div>