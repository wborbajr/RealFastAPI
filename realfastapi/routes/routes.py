from fastapi import APIRouter

# from app.api.api_v1.endpoints import login, notes, users, utils
from realfastapi.routes.endpoints import default, music

api_router = APIRouter()
api_router.include_router(default.router, tags=["default"])  # type ignore
api_router.include_router(music.router, prefix="/music", tags=["music"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(notes.router, prefix="/notes", tags=["notes"])
