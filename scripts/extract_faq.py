import os
import json
from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_tr = False
        self.in_td = False
        self.current_row = []
        self.current_cell = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.in_tr = True
            self.current_row = []
        elif tag == "td" and self.in_tr:
            self.in_td = True
            self.current_cell = []
        elif tag == "br" and self.in_td:
            self.current_cell.append("\n")

    def handle_endtag(self, tag):
        if tag == "tr":
            self.in_tr = False
            if self.current_row:
                self.rows.append(self.current_row)
        elif tag == "td" and self.in_td:
            self.in_td = False
            self.current_row.append("".join(self.current_cell).strip())

    def handle_data(self, data):
        if self.in_td:
            self.current_cell.append(data)

def clean_text(text):
    if not text:
        return ""
    # Normalize unicode dashes to standard ASCII hyphen or comma
    text = text.replace("\u2014", ", ").replace("\u2013", ", ")
    return text.strip()

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_path = os.path.join(base_dir, "Customer Questions - Grouped.xlsm", "Grouped Questions.html")
    
    if not os.path.exists(html_path):
        print(f"Error: Could not find file at {html_path}")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        parser = TableParser()
        parser.feed(f.read())

    all_items = []
    answered_items = []
    current_group = ""

    # Skip top 3 header/title rows
    for r in parser.rows[3:]:
        if len(r) >= 4:
            group = clean_text(r[0])
            faq_id = clean_text(r[1])
            question = clean_text(r[2])
            answer = clean_text(r[3])

            if group:
                current_group = group
            effective_group = current_group if not group else group

            if question:
                item = {
                    "faq_id": faq_id if faq_id else None,
                    "group": effective_group,
                    "question": question,
                    "answer": answer if answer else None,
                    "is_answered": bool(answer)
                }
                all_items.append(item)
                if answer:
                    answered_items.append(item)

    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    # Save JSON files
    all_json_path = os.path.join(data_dir, "faq_all.json")
    with open(all_json_path, "w", encoding="utf-8") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)

    answered_json_path = os.path.join(data_dir, "faq_answered.json")
    with open(answered_json_path, "w", encoding="utf-8") as f:
        json.dump(answered_items, f, indent=2, ensure_ascii=False)

    # Save Markdown file for answered questions
    md_path = os.path.join(data_dir, "faq_answered.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Rownd 5X Answered Customer Questions Knowledge Base\n\n")
        f.write("This file contains verified, officially answered customer questions for the Rownd 5X CNC machine.\n")
        f.write("AI models can consult this document to answer inbound customer inquiries.\n\n")
        f.write(f"Total answered questions: {len(answered_items)}\n\n")
        f.write("---\n\n")

        for idx, item in enumerate(answered_items, 1):
            faq_id_label = f"FAQ ID: {item['faq_id']}" if item["faq_id"] else "FAQ ID: Unassigned"
            f.write(f"## {idx}. [{item['group']}] {faq_id_label}\n\n")
            f.write(f"**Question:**\n> {item['question']}\n\n")
            # Format multi-line answer
            formatted_ans = item['answer'].replace("\n", "\n\n")
            f.write(f"**Official Answer:**\n{formatted_ans}\n\n")
            f.write("---\n\n")

    print(f"Successfully processed {len(all_items)} total questions.")
    print(f"Extracted {len(answered_items)} answered questions.")
    print(f"Files saved to: {data_dir}")

if __name__ == "__main__":
    main()
