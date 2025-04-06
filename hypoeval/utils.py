import numpy as np
import json
import sys
import os
import yaml
import string
import re
from typing import List, Dict, Any
import random
from LLM_wrapper.logger_config import LoggerConfig


def get_aspect_definition(dataset_name, aspect):
    if dataset_name == "summeval":
        if aspect == "coherence":
            return "Coherence measures the quality of all sentences collectively, focusing on how well they fit together and sound natural as a whole."
        elif aspect == "consistency":
            return "Consistency measures whether the facts in the summary align with those in the original article, ensuring all facts are accurately reproduced and no untrue information is introduced."
        elif aspect == "fluency":
            return "Fluency measures the quality of individual sentences, evaluating whether they are well-written and grammatically correct."
        elif aspect == "relevance":
            return "Relevance measures how well the summary captures the key points of the article, considering whether all and only the important aspects are included."
        else:
            print(f"Aspect {aspect} for dataset {dataset_name} not supported!")
            return ""
    elif dataset_name == "newsroom":
        if aspect == "coherence":
            return "Do phrases and sentences of the summary fit together and make sense collectively?"
        elif aspect == "fluency":
            return "Are the individual sentences of the summary well-written and grammatical?"
        elif aspect == "informativeness":
            return "How well does the summary capture the key points of the article?"
        elif aspect == "relevance":
            return "Are the details provided by the summary consistent with the details in the article?"
        else:
            print(f"Aspect {aspect} for dataset {dataset_name} not supported!")
            return ""
    elif dataset_name == "hanna":
        if aspect == "coherence":
            return "Coherence measures whether the story makes sense"
        elif aspect == "empathy":
            return "Empathy measures how well you understood the characters' emotions (regardless of whether you agreed with them)"
        elif aspect == "surprise":
            return "Surprise measures how surprising the end of the story was"
        elif aspect == "engagement":
            return "Engagement measures how much you engaged with the story"
        elif aspect == "complexity":
            return "Complexity measures how elaborate the story is"
        elif aspect == "relevance":
            return "Relevance measures how well the story matches its prompt"
        else:
            print(f"Aspect {aspect} for dataset {dataset_name} not supported!")
            return ""
    elif dataset_name == "writingprompt":
        if aspect == "grammaticality":
            return "How grammatically correct is the text of the story fragment?"
        elif aspect == "cohesiveness":
            return "How well do the sentences in the story fragment fit together?"
        elif aspect == "likability":
            return "How enjoyable do you find the story fragment?"
        elif aspect == "relevance":
            return "How relevant is the story fragment to the prompt?"
        else:
            print(f"Aspect {aspect} for dataset {dataset_name} not supported!")
            return ""
    else:
        print(f"dataset {dataset_name} not supported!")
        return ""

def batched_extract_likert_scores(responses: List[str]):
    logger = LoggerConfig.get_logger("extract_label")
    scores = []
    for response in responses:
        if response is None:
            logger.warning(f"Could not extract label from text: {response}")
            scores.append(-1)
            continue

        response = response.lower()
        patterns = [
            r"final score: (\d+)",
            r"answer is: \$\\boxed{(\d+)}\$"
        ]
        flag = False
        for pattern in patterns:
            match = re.findall(pattern, response)
            if len(match) > 0:
                scores.append(match[-1])
                flag = True
                break
        if flag == False:
            logger.warning(f"Could not extract label from text: {response}")
            scores.append(-1)

    return [float(score) for score in scores]
