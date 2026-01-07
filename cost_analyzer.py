def estimate_tokens(text):
    """
    Rough token estimation:
    1 token ≈ 4 characters
    """
    return max(1, len(text) // 4)


def estimate_cost(tokens, cost_per_1k=0.002):
    """
    Estimate API cost based on tokens
    """
    return round((tokens / 1000) * cost_per_1k, 6)


def cost_quality_score(total_score, cost):
    """
    Higher score = better quality per dollar
    """
    if cost == 0:
        return total_score
    return round(total_score / cost, 2)
