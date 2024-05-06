from fastapi import APIRouter

zakaz_router=APIRouter(prefix="/zakaz")

@zakaz_router.get("/")
async def zakazlar():
    return {"zakaz":"Bu zakazlar ro'yhati"}