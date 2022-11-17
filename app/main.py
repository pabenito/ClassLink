from fastapi import FastAPI

# Create app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Educa"}