import streamlit as st
import pandas as pd

# Core evaluation
from evaluator import evaluate_response, total_score

# Analysis modules
from prompt_dna import analyze_prompt_dna
from explain_score import explain_why_score
from explainability_score import calculate_explainability_score
from prompt_failure_simulator import simulate_prompt_failures

# Optimization modules
from prompt_mutator import mutate_prompt
from cost_analyzer import estimate_tokens, estimate_cost, cost_quality_score

# Version control
from prompt_version_control import add_prompt_version, load_versions

# Domain optimization
from domain_optimizer import apply_domain_optimization
from domain_rules import DOMAIN_RULES


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Prompt Evaluation System", layout="centered")
st.title("🧠 Prompt Evaluation & Optimization System")

# ---------------- USER INPUT ----------------
task = st.text_area("Enter task / problem statement")

prompt_text = st.text_area("Enter prompts (one per line)", height=200)

domain = st.selectbox("Select Domain", list(DOMAIN_RULES.keys()))

# ---------------- MAIN ACTION ----------------
if st.button("Evaluate Prompts"):

    prompts = [p for p in prompt_text.split("\n") if p.strip()]
    st.subheader("📊 Evaluation Results")

    results = []

    # Chart data containers
    prompt_labels = []
    explainability_scores = []
    costs = []
    total_scores = []

    # -------- EVALUATION --------
    for prompt in prompts:
        scores = evaluate_response("response")
        total = total_score(scores)
        results.append((prompt, scores, total))

    # -------- PER PROMPT ANALYSIS --------
    for i, (p, s, t) in enumerate(results):
        st.write(f"### Prompt {i+1}")
        st.write("📝 Original Prompt:")
        st.write(p)

        dna = analyze_prompt_dna(p)
        st.write("🧬 Prompt DNA Analysis")
        st.json(dna)

        st.write("📊 Scores:", s)
        st.write("⭐ Total Score:", t)

        explanation = explain_why_score(dna, s)
        st.info("💡 Why this score?")
        st.write(explanation)

        explainability = calculate_explainability_score(dna, s)
        st.metric("🧠 Explainability Score", f"{explainability}/100")

        warnings = simulate_prompt_failures(p, dna)
        st.warning("🚨 Prompt Failure Simulation")
        for w in warnings:
            st.write("•", w)

        improved_prompt = mutate_prompt(p, dna)
        st.success("🚀 Auto-Improved Prompt")
        st.write(improved_prompt)

        domain_prompt = apply_domain_optimization(improved_prompt, domain)
        st.success("🌐 Domain-Optimized Prompt")
        st.write(domain_prompt)

        if domain == "Healthcare":
            st.warning("⚠️ Healthcare content is informational only.")

        tokens = estimate_tokens(improved_prompt)
        cost = estimate_cost(tokens)
        efficiency = cost_quality_score(t, cost)

        st.write("💰 Cost vs Quality")
        st.write(f"Tokens: {tokens} | Cost: ${cost} | Efficiency: {efficiency}")

        # -------- SAVE VERSION --------
        add_prompt_version(p, improved_prompt, t, explainability)

        # -------- COLLECT CHART DATA --------
        prompt_labels.append(f"Prompt {i+1}")
        explainability_scores.append(explainability)
        costs.append(cost)
        total_scores.append(t)

        st.divider()

    # ---------------- CHARTS ----------------
    st.subheader("📊 Explainability Score Comparison")
    st.bar_chart(pd.DataFrame(
        {"Explainability Score": explainability_scores},
        index=prompt_labels
    ))

    st.subheader("⚖️ Cost vs Quality Scatter Plot")
    st.scatter_chart(pd.DataFrame({
        "Cost": costs,
        "Quality Score": total_scores
    }))

    st.subheader("📈 Prompt Improvement Over Versions")
    version_scores = []
    for record in load_versions():
        for v in record["versions"]:
            version_scores.append(v["total_score"])

    if version_scores:
        st.line_chart(version_scores)
