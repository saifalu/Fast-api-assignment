# main.py

from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Azure Web Apps!"}

if __name__ == "__main__":
    import uvicorn

    # Get port from environment variable or use default (8000)
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
