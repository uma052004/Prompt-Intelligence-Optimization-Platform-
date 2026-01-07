def calculate_explainability_score(dna, scores):
    score = 0

    if dna.get("role"):
        score += 20
    if dna.get("task"):
        score += 20
    if dna.get("constraints"):
        score += 20
    if dna.get("output_format"):
        score += 20

    # Normalize clarity (1–10 → 0–20)
    clarity_score = scores.get("clarity", 0)
    score += min(20, clarity_score * 2)

    return score
