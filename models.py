from pydantic import BaseModel


class Segment(BaseModel):
    index: int
    start: float
    end: float
    text: str


class transcription_request(BaseModel):
    filename: str
    language_from: str
    language_to: str
    segments: list[Segment]


class transcription_response(BaseModel):
    filename: str
    language_from: str
    language_to: str
    segments: list[Segment]
