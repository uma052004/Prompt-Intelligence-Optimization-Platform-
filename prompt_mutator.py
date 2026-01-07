def mutate_prompt(original_prompt, dna):
    improved_prompt = original_prompt

    # Add role if missing
    if not dna["role"]:
        improved_prompt = "You are an expert assistant. " + improved_prompt

    # Add context if missing
    if not dna["context"]:
        improved_prompt += " Explain it for a beginner."

    # Add output format if missing
    if not dna["output_format"]:
        improved_prompt += " Use bullet points."

    # Add constraints if missing
    if not dna["constraints"]:
        improved_prompt += " Limit the response to 100 words."

    return improved_prompt
