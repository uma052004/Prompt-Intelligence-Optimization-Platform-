import random

def evaluate_response(response):
    return {
        "relevance": random.randint(6, 10),
        "clarity": random.randint(6, 10),
        "adherence": random.randint(6, 10),
        "conciseness": random.randint(6, 10)
    }

def total_score(scores):
    return sum(scores.values())
