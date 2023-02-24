from pathlib import Path

from app.videos.shemas import AudioStream, Video
from app.config import CHUNK_SIZE, AUDIOS_DIR


def get_audio_stream(
        video_id: str, start: int = 0, end: int | None = None) -> AudioStream:
    if not end:
        end = start + CHUNK_SIZE
    path = AUDIOS_DIR / video_id
    data = _read_audio_bytes(path, start, end)
    filesize = path.stat().st_size
    return AudioStream(start=start, end=end, data=data, filesize=filesize)


def _read_audio_bytes(path: Path, start, end: int) -> bytes:
    with open(path, 'rb') as video:
        video.seek(start)
        return video.read(end - start)

