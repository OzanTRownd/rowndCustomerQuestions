# Rownd 5X Customer Email Inquiry Assistant

This project organizes customer questions and official answers for the Rownd 5X CNC machine. Its purpose is to assist customer support by matching incoming customer emails against verified, already-answered questions.

---

## 1. Project Goal

When a customer sends an inquiry or email:
1. **Match Against Verified Answers:** Check if the email asks something that has already been answered officially.
2. **Provide the Answer:** If a close match is found, output the verified answer or generate a ready-to-send draft response.
3. **Escalate Unanswered Inquiries:** If there is no close match in the verified questions, immediately notify the user to forward the email to company employees.
4. **Handle Multi-Part Emails:** If an email contains multiple questions where only some are answered, provide answers for the matched questions and flag the remaining questions for employee escalation.

---

## 2. Project Structure

```
rowndCustomerQuestions/
├── .agents/
│   └── rules/
│       └── customer_support_assistant.md   # Automatic behavior rules for IDE AI agents
├── Customer Questions - Grouped.xlsm/
│   ├── Grouped Questions.html             # Original source table of customer questions
│   └── resources/                         # Original stylesheet and assets
├── data/
│   ├── faq_answered.json                  # Clean JSON dataset of all 16 verified, answered questions
│   ├── faq_all.json                       # Complete JSON dataset of all 62 questions (answered and pending)
│   └── faq_answered.md                    # Formatted Markdown reference of verified questions and answers
├── prompts/
│   ├── system_prompt.md                   # Universal system prompt for any AI model (ChatGPT, Claude, Gemini, etc.)
│   └── example_queries.md                 # Real-world examples showing matching and forwarding scenarios
├── scripts/
│   ├── extract_faq.py                     # Script to re-parse Grouped Questions.html into data/ files
│   └── match_email.py                     # Standalone Python CLI utility to search inquiries from terminal
└── README.md                              # This documentation file
```

---

## 3. How to Use with Any AI Model (Instructions for Future Models)

If you use this project with a new AI model (such as ChatGPT, Claude, Gemini, or a local LLM), follow these steps:

### Option A: Direct Chat / Copy-Paste
1. Open [system_prompt.md](file:///d:/vscode/rowndCustomerQuestions/prompts/system_prompt.md).
2. Copy the contents of the file and paste it as the system instructions or initial prompt into the AI model.
3. Paste the customer's incoming email into the chat.
4. The AI will:
   - Identify if the question matches an FAQ.
   - Reply with the official answer if matched.
   - Tell you: `"No close answer found in our verified FAQs. Please forward this email to our employees."` if unmatched.

### Option B: In This IDE / Assistant
- The `.agents/rules/customer_support_assistant.md` rule is already configured.
- You can simply copy and paste any customer email into the chat with this AI assistant at any time, and it will immediately follow these rules.

### Option C: Command Line Search
You can also evaluate an inquiry using the included Python CLI:
```bash
python scripts/match_email.py "When will pre-orders begin and how much will it cost?"
```

---

## 4. Operational Guidelines for AI Models

Any AI model handling this task must strictly follow these rules:

1. **Zero Hallucination:** Only provide technical specifications, pricing, timelines, or company claims that are documented in the verified knowledge base (`data/faq_answered.json` or `data/faq_answered.md`).
2. **Clear Escalation:** If the question is not covered by an answered FAQ, never guess. Explicitly tell the user to forward the message to human employees.
3. **Partial Answers:** If a customer asks two questions (e.g., machine weight and custom color options), answer the weight using FAQ ID 29, and explicitly instruct the user to forward the question about custom color options to employees.
4. **Professionalism:** When generating email drafts, maintain a helpful, welcoming, and professional tone representing the Rownd team.

---

## 5. Updating the Knowledge Base

When new questions are answered or updated in `Customer Questions - Grouped.xlsm/Grouped Questions.html`:
1. Save the updated HTML file.
2. Run the extraction script:
   ```bash
   python scripts/extract_faq.py
   ```
3. The script will automatically regenerate:
   - [data/faq_answered.json](file:///d:/vscode/rowndCustomerQuestions/data/faq_answered.json)
   - [data/faq_all.json](file:///d:/vscode/rowndCustomerQuestions/data/faq_all.json)
   - [data/faq_answered.md](file:///d:/vscode/rowndCustomerQuestions/data/faq_answered.md)
4. Update [prompts/system_prompt.md](file:///d:/vscode/rowndCustomerQuestions/prompts/system_prompt.md) if you are exporting prompts to external web chatbots.
