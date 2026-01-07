import re

def analyze_prompt_dna(prompt: str):
    dna = {
        "role": False,
        "task": False,
        "constraints": False,
        "output_format": False,
        "context": False
    }

    # Role detection
    if re.search(r"\byou are\b|\bact as\b|\bas a\b", prompt.lower()):
        dna["role"] = True

    # Task detection (verbs)
    if re.search(r"\bexplain\b|\bwrite\b|\bgenerate\b|\blist\b|\bcreate\b", prompt.lower()):
        dna["task"] = True

    # Constraints detection
    if re.search(r"\bunder\b|\blimit\b|\bwithin\b|\bwords\b|\bsteps\b", prompt.lower()):
        dna["constraints"] = True

    # Output format detection
    if re.search(r"\bbullet\b|\bpoints\b|\bjson\b|\btable\b|\bstep\b", prompt.lower()):
        dna["output_format"] = True

    # Context detection
    if re.search(r"\bfor a\b|\bbeginner\b|\bexpert\b|\bstudent\b", prompt.lower()):
        dna["context"] = True

    return dna
