def explain_why_score(dna, scores):
    reasons = []

    # DNA-based explanations
    if not dna["role"]:
        reasons.append("the prompt does not define a clear role")
    if not dna["constraints"]:
        reasons.append("no constraints like word limit or format are specified")
    if not dna["output_format"]:
        reasons.append("the expected output format is not mentioned")
    if not dna["context"]:
        reasons.append("the target audience or context is missing")

    # Score-based explanations
    if scores["clarity"] < 7:
        reasons.append("the response lacks clarity")
    if scores["conciseness"] < 7:
        reasons.append("the response could be more concise")

    if not reasons:
        return "This prompt is well-structured with clear instructions and constraints."

    explanation = "This prompt scored this way because " + ", ".join(reasons) + "."
    return explanation
