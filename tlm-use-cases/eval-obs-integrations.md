---
sidebar_position: 9
sidebar_label: Evals/Observability
---

# Automatically Find Inaccurate LLM Responses in Evaluation and Observability Platforms

Cleanlab's Trustworthy Language Model (TLM) enables evaluation and observability platform users to quickly identify low quality and hallucinated responses from any LLM trace.

TLM automatically finds the poor quality and incorrect LLM responses lurking within your production logs and traces. This helps you perform better Evals, with significantly less manual review and annotation work to find these bad responses yourself.

The integrations below show how to use TLM with various 3rd party LLM evaluation/observability platforms.

## Arize Phoenix

[Arize Phoenix](https://github.com/Arize-ai/phoenix) is an open-source AI observability platform designed for experimentation, evaluation, and troubleshooting.

- [Documentation for Cleanlab Integration](https://docs.arize.com/phoenix/integrations/cleanlab)
- [Github Example](https://github.com/Arize-ai/phoenix/blob/main/tutorials/integrations/evaluating_traces_cleanlabTLM.ipynb)
- [Colab Example](https://colab.research.google.com/github/Arize-ai/phoenix/blob/main/tutorials/integrations/evaluating_traces_cleanlabTLM.ipynb)

## Langfuse

[Langfuse](https://langfuse.com/) is an open-source platform for LLM engineering.

- [Documentation for Cleanlab Integration](https://langfuse.com/docs/integrations/other/cleanlab)
- [Github Example](https://github.com/langfuse/langfuse-docs/blob/main/cookbook/evaluation_of_llms_with_cleanlab.ipynb)
- [Colab Example](https://colab.research.google.com/github/langfuse/langfuse-docs/blob/main/cookbook/evaluation_of_llms_with_cleanlab.ipynb)

## MLflow

[MLflow](https://mlflow.org/) is an open source MLOps platform for GenAI applications.

- [Documentation for Cleanlab Integration](https://mlflow.org/blog/tlm-tracing)
- [Github Example](https://github.com/cleanlab/cleanlab-tools/blob/main/TLM-MLflow-Integration/evaluating_traces_TLM_mlflow_dl.ipynb)
- [Colab Example](https://colab.research.google.com/github/cleanlab/cleanlab-tools/blob/main/TLM-MLflow-Integration/evaluating_traces_TLM_mlflow_dl.ipynb)