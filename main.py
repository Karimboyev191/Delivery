import uvicorn
from fastapi import FastAPI
from user_routes import user_router
from zakaz_routes import zakaz_router

app=FastAPI()
app.include_router(user_router)
app.include_router(zakaz_router)


@app.get("/")
async def home():
    return {"message":"bu yetkazib berish web sahifasining API"}

if __name__=="__main__":
    uvicorn.run("main:app",port=5000)