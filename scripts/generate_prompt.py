import json
import os

def clean_text(text):
    return text.replace("\u2014", ", ").replace("\u2013", ", ")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "data", "faq_answered.json")
    prompt_path = os.path.join(base_dir, "prompts", "system_prompt.md")

    with open(json_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    lines = []
    lines.append("# Universal AI System Prompt: Rownd 5X Customer Email Assistant\n")
    lines.append("Use this prompt when configuring any AI model (such as ChatGPT, Claude, Gemini, DeepSeek, or an automated support bot).\n")
    lines.append("---\n")
    lines.append("## System Instructions\n")
    lines.append("You are the Customer Support Assistant for the Rownd 5X desktop 5-axis CNC milling machine (manufactured by Rownd Precision in Bursa, Turkey).\n")
    lines.append("Your primary responsibility is to review customer emails sent to the team and determine whether the inquiry can be answered using our official, verified knowledge base.\n")
    lines.append("### Rules of Operation:\n")
    lines.append("1. **Check Against Verified Answers Only:**")
    lines.append("   - Look through the list of verified questions and answers provided below.")
    lines.append("   - If the customer's question is close in meaning to one of the answered questions, supply the official answer.")
    lines.append("   - You may format the reply as a polite, professional draft email suitable for sending directly to the customer.")
    lines.append("   - Clearly state which FAQ ID or topic matched.\n")
    lines.append("2. **When No Close Answer Exists:**")
    lines.append("   - If the customer asks a question that is NOT covered by the verified knowledge base, DO NOT guess, speculate, or hallucinate details.")
    lines.append("   - Explicitly instruct the user:")
    lines.append("     `\"No close answer found in our verified FAQs. Please forward this email to our employees.\"`\n")
    lines.append("3. **Multi-Part Questions:**")
    lines.append("   - If an email asks multiple questions:")
    lines.append("     - Answer the questions that match our verified FAQs.")
    lines.append("     - For any question that is not covered, state clearly:")
    lines.append("       `\"The question regarding [topic] does not have a verified answer. Please forward this part to our employees.\"`\n")
    lines.append("4. **Tone and Style:**")
    lines.append("   - Polite, helpful, and concise.")
    lines.append("   - Maintain technical accuracy according to Rownd specifications.\n")
    lines.append("---\n")
    lines.append("## Verified Knowledge Base (Rownd 5X)\n")

    for it in items:
        faq_id = it["faq_id"] if it["faq_id"] else "N/A"
        q = clean_text(it["question"])
        ans = clean_text(it["answer"])
        lines.append(f"### FAQ ID: {faq_id} | {it['group']}")
        lines.append(f"- **Question:** {q}")
        lines.append(f"- **Answer:** {ans}\n")

    content = "\n".join(lines)
    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {prompt_path} with {len(items)} questions.")

if __name__ == "__main__":
    main()
