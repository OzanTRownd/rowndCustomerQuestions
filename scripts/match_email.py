import os
import json
import re

def load_knowledge_base():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    faq_path = os.path.join(base_dir, "data", "faq_answered.json")
    if not os.path.exists(faq_path):
        raise FileNotFoundError(f"Knowledge base not found at {faq_path}. Run extract_faq.py first.")
    with open(faq_path, "r", encoding="utf-8") as f:
        return json.load(f)

def tokenize(text):
    words = re.findall(r"\b[a-zA-Z0-9_]{3,}\b", text.lower())
    stopwords = {
        "the", "and", "for", "are", "with", "will", "this", "that", "from",
        "have", "has", "can", "you", "your", "what", "when", "where", "which",
        "how", "who", "does", "about", "our", "all", "any"
    }
    return set(w for w in words if w not in stopwords)

def find_matches(email_text, knowledge_base, threshold=0.15):
    email_tokens = tokenize(email_text)
    if not email_tokens:
        return []

    results = []
    for item in knowledge_base:
        q_tokens = tokenize(item["question"])
        # Also include keywords from group name
        group_tokens = tokenize(item["group"])
        combined_ref_tokens = q_tokens.union(group_tokens)

        intersection = email_tokens.intersection(combined_ref_tokens)
        if not intersection:
            continue

        score = len(intersection) / float(len(combined_ref_tokens))
        if score >= threshold:
            results.append({
                "score": round(score, 3),
                "matched_terms": list(intersection),
                "faq": item
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def evaluate_email(email_text):
    kb = load_knowledge_base()
    matches = find_matches(email_text, kb)

    print("=" * 60)
    print("CUSTOMER INQUIRY EVALUATION")
    print("=" * 60)
    print(f"Email content:\n{email_text.strip()}\n")
    print("-" * 60)

    if not matches:
        print("[DECISION]: No close answer found in verified FAQs.")
        print("[ACTION]: Please forward this inquiry to our employees.")
        print("=" * 60)
        return

    top_match = matches[0]
    faq = top_match["faq"]
    faq_id = faq.get("faq_id") or "N/A"

    print(f"[DECISION]: Found close answer (FAQ ID: {faq_id}, Category: {faq['group']})")
    print(f"Similarity Score: {top_match['score']} (Matched words: {', '.join(top_match['matched_terms'])})")
    print(f"Matched Question: {faq['question']}")
    print("\nVerified Answer:")
    print(faq["answer"])
    print("=" * 60)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        evaluate_email(query)
    else:
        sample_email = "Hello, could you let me know how much the Rownd 5X weighs and what the shipping weight is?"
        print("Running sample query:")
        evaluate_email(sample_email)
