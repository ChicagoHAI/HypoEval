# HypoEval: Hypothesis-Guided Evaluation for Natural Language Generation (Evaluators)
This repository provides off-the-shelf 0-shot LLM-based evaluators for summarization and story generation, from the paper HypoEval: Hypothesis-Guided Evaluation of Natural Language Generation (TODO: add url). For more details on HypoEval implementation, reproducing results, and adding new evaluated aspects, please refer to [**ChicagoHAI/HypoEval-Gen**](https://github.com/ChicagoHAI/HypoEval-Gen).

TODO: add pip install support.

## Usage

To use the evaluator for summaries on aspect in `["coherence", "consistency", "informativeness", "fluency", "relevance"]`:

```bash
from hypoeval.evaluator import SummaryEvaluator

evaluator = SummaryEvaluator(model_name=MODEL_NAME, model_path=MODEL_PATH) # (optional) specify model path for local models
evaluated_aspect = "coherence"
summary_list = ["...", "..."]
source_text_list = ["...", "..."]
evaluation_scores = evaluator.batched_evaluate(aspect=evaluated_aspect, summaries=summary_list, source_texts=source_text_list)
```

To use the evaluator for stories on aspect in `["coherence", "cohesiveness", "complexity", "empathy", "engagement", "grammaticality", "likability", "relevance", "surprise"]`:

```bash
from hypoeval.evaluator import StoryEvaluator

evaluator = StoryEvaluator(model_name=MODEL_NAME, model_path=MODEL_PATH) # (optional) specify model path for local models
evaluated_aspect = "coherence"
story_list = ["...", "..."]
story_prompt_list = ["...", "..."]
evaluation_scores = evaluator.batched_evaluate(aspect=evaluated_aspect, stories=story_list, story_prompts=story_prompt_list)
```

## Citation

Please consider citing our work if it contributes to your research:

(TODO: add bibtex)