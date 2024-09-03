from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def book():
    return {"messae": "Hello denny"}