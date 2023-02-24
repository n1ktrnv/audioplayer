from fastapi import FastAPI, BackgroundTasks


from app.videos.routes import routes as video_routes

app = FastAPI()
app.include_router(video_routes)
