from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class Source(BaseModel):
    marker: str
    citation: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]


class DocumentUploadResponse(BaseModel):
    doc_id: str
    chunks_stored: int
