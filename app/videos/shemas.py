from pydantic import BaseModel


class AudioStream(BaseModel):
    start: int
    end: int
    data: bytes
    filesize: int
