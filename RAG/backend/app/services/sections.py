import re

# A line that is: a 1-2 digit number, whitespace, a short Capitalised phrase, no trailing period.
HEADING_RE = re.compile(
    r"^(\d{1,2})\s+([A-Z][A-Za-z0-9 ,&/'-]{2,60})$", re.MULTILINE)


def clean_text(raw: str) -> str:
    """Normalise PDF extraction quirks: line endings, hyphenated breaks, stray whitespace."""
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"-\n(?=[a-z])", "", text)
    text = text.replace("\u00A0", " ")
    text = re.sub(r"[ \t]{2,}", "  ", text)
    text = re.sub(r"^\s*Page \d+ of \d+\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_into_sections(text: str) -> list[dict]:
    """Split a document's text into sections by heading, e.g. '2  Annual Leave'."""
    marks = list(HEADING_RE.finditer(text))

    if not marks:
        return [{"section_no": "0", "section_title": "Full document", "section_text": text}]

    sections = []
    for i, m in enumerate(marks):
        start = m.start()
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        body = text[start:end].strip()
        if len(body) < 40:
            continue
        sections.append({
            "section_no": m.group(1),
            "section_title": m.group(2).strip(),
            "section_text": body,
        })
    return sections
