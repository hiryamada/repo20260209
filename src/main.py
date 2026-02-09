from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Return a simple hello world message."""
    return {"message": "hello world"}
