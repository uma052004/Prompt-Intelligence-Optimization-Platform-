import re

def simulate_prompt_failures(prompt, dna):
    warnings = []

    # 1️⃣ Vague prompt
    if len(prompt.split()) < 4:
        warnings.append("Prompt is very short and may be too vague.")

    if not dna.get("task"):
        warnings.append("No clear task/action verb detected.")

    # 2️⃣ Conflicting constraints
    if "short" in prompt.lower() and "detailed" in prompt.lower():
        warnings.append("Conflicting instructions: 'short' and 'detailed' used together.")

    word_limits = re.findall(r"\b\d+\s*words?\b", prompt.lower())
    if len(word_limits) > 1:
        warnings.append("Multiple word limits detected, which may confuse the model.")

    # 3️⃣ Hallucination risk
    if not dna.get("constraints") and not dna.get("context"):
        warnings.append("High hallucination risk due to missing constraints and context.")

    # 4️⃣ Instruction overload
    if len(prompt.split()) > 60:
        warnings.append("Prompt is very long and may overload instructions.")

    if not warnings:
        warnings.append("No major prompt failure risks detected.")

    return warnings
