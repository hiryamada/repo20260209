from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    """Return the current time."""
    current_time = datetime.now().isoformat()
    return {"current_time": current_time}
