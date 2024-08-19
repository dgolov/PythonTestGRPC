from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def ping():
    return {"ping": True}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
