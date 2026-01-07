from domain_rules import DOMAIN_RULES

def apply_domain_optimization(prompt, domain):
    rules = DOMAIN_RULES.get(domain, DOMAIN_RULES["General"])

    optimized_prompt = prompt

    # Inject role
    if rules["role"] not in optimized_prompt:
        optimized_prompt = rules["role"] + " " + optimized_prompt

    # Inject constraints
    if rules["constraints"]:
        optimized_prompt += " " + rules["constraints"]

    # Inject style
    if rules["style"]:
        optimized_prompt += " " + rules["style"]

    return optimized_prompt
