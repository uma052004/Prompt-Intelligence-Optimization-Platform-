from evaluator import evaluate_response, total_score

print("\n🧠 Prompt Evaluation System\n")

task = input("Enter task/problem statement:\n> ")

num_prompts = int(input("\nHow many prompts do you want to evaluate? "))

prompts = []

for i in range(num_prompts):
    p = input(f"\nEnter Prompt {i + 1}:\n> ")
    prompts.append(p)

print("\n📊 Evaluation Results\n")
print("-" * 70)
print(f"{'Prompt':<10}{'Relevance':<12}{'Clarity':<10}{'Adherence':<12}{'Concise':<10}{'Total'}")
print("-" * 70)

results = []

for i, prompt in enumerate(prompts):
    response = f"Simulated response for: {prompt}"
    scores = evaluate_response(response)
    total = total_score(scores)

    results.append({
        "prompt": prompt,
        "scores": scores,
        "total": total
    })

    print(
        f"{i+1:<10}"
        f"{scores['relevance']:<12}"
        f"{scores['clarity']:<10}"
        f"{scores['adherence']:<12}"
        f"{scores['conciseness']:<10}"
        f"{total}"
    )

print("-" * 70)

best = max(results, key=lambda x: x["total"])

print("\n🏆 BEST PROMPT")
print(best["prompt"])
print("Score:", best["total"])

