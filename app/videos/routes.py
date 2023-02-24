from fastapi import APIRouter, status, responses, Request, Header, Response

from app.videos.service import get_audio_stream
from app.config import TEMPLATES

routes = APIRouter()


@routes.get('/videos/{video_id}')
def audio_streaming(video_id: str, range: str = Header(None)):
    start, end = range.replace('bytes=', '').split("-")
    start = int(start)
    end = int(end) if end else None
    audio_stream = get_audio_stream(video_id, start, end)
    headers = {
        'Content-Range': f'bytes {audio_stream.start}-{audio_stream.end}/'
                         f'{audio_stream.filesize}',
        'Accept-Ranges': 'bytes'
    }
    return Response(
        audio_stream.data,
        status_code=status.HTTP_206_PARTIAL_CONTENT,
        headers=headers,
        media_type="audio/mp4"
    )


@routes.get('/{video_id}', response_class=responses.HTMLResponse)
def get_audio_page(video_id: str, request: Request):
    return TEMPLATES.TemplateResponse('audio.html', {
        'request': request,
        'video_id': video_id
    })
