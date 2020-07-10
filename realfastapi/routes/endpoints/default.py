from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def working():
    return {"Working"}

