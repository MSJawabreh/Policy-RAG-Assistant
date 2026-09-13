from google import genai
from google.genai import types

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def embed_text(text: str) -> list[float]:
    """Turn a piece of text into a list of numbers (a vector) representing its meaning."""
    result = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=3072),
    )
    return list(result.embeddings[0].values)
