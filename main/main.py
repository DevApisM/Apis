from fastapi import FastAPI 

app = FastAPI()

@app.post("/init")
async def initialize():
    # Your initialization logic here
    # For example, preparing a database, loading config, etc.
    return {"status": "initialized successfully"}

