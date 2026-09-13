def chunk_text(text: str, chunk_size: int = 900, overlap: int = 150) -> list[str]:
    """Cut text into overlapping pieces of roughly chunk_size characters.
    Works on any text, regardless of structure -- this is the fallback
    that makes ingestion work even when a document has no clear headings."""
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap  # step back by `overlap` so pieces share some text
    return chunks
