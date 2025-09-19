---
title: Integration Tutorials
sidebar_label: Integration Tutorials
sidebar_position: 5
---

import TutorialFinder from "@site/src/components/TutorialFinder/TutorialFinder";

# Integrating the Cleanlab AI Platform into your AI application

Here you can find step-by-step developer tutorials to easily integrate Cleanlab with your existing AI app, no matter how it is architected.
We provide tutorials for many different AI frameworks, as well as [types of Cleanlab integrations](/codex/concepts/integrations/).

<div className="cl-design-system flex flex-col min-h-[calc(100vh-140px)] justify-between">
<div className="flex flex-col gap-13">
<TutorialFinder decisionTree={
    {
        "questions": {
            "rag": {
                "title": "Select your AI framework",
                "placeholder": "AI framework"
            },
            "integration": {
                "title": "Select an integration style",
                "description": "These are the recommended [ways to integrate](/codex/concepts/integrations) Cleanlab for your current AI system",
                "placeholder": "Integration style"
            }
        },
        "tree": {
            "question": "rag",
            "options": [
                {
                    "value": "Custom AI",
                    "next": {
                        "question": "integration",
                        "options": [
                            {
                                "value": "Cleanlab with your custom AI architecture",
                                "contents": "[Guide: Cleanlab with any custom AI architecture](/codex/tutorials/other_rag_frameworks/validator/)"
                            },
                        ]
                    }
                },
                {
                    "value": "Azure AI",
                    "next": {
                        "question": "integration",
                        "options": [
                            {
                                "value": "Cleanlab with Azure AI",
                                "contents": "[Guide: Cleanlab with Azure AI](/codex/tutorials/azure/Azure_Guardrails_CodexAsBackup/)"
                            },
                        ]
                    }
                },
                {
                    "value": "AWS Knowledge Bases",
                    "next": {
                        "question": "integration",
                        "options": [
                            {
                                "value": "Cleanlab with AWS Knowledge Bases",
                                "contents": "[Guide: Cleanlab with AWS Knowledge Bases](/codex/tutorials/aws/AWSBedrock_CodexAsBackup/)"
                            },
                        ]
                    }
                },
                {
                    "value": "OpenAI Assistants",
                    "next": {
                        "question": "integration",
                        "options": [
                            {
                                "value": "Cleanlab with OpenAI Assistants",
                                "contents": "[Guide: Cleanlab with OpenAI Assistants](/codex/tutorials/openai/OpenAIAssistants_CodexAsBackup/)"
                            },
                        ]
                    }
                }
            ]
        }
    }
} />
</div>
</div>
