

def extract_title(markdown: str) -> str | None:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("#").strip()
    raise Exception("No H1 header found")
