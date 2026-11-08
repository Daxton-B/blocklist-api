from fastapi import FastAPI, HTTPException
from blocklist import load_blocklist, is_blocked
from pathlib import Path

BLOCKLIST = load_blocklist(Path(__file__).parent / "blocklist.txt")


app = FastAPI()


@app.get("/health")
def read_root():
    return {"status": "ok"}


@app.get("/check/{ip}")
def check(ip: str):
    try:
        blocked = is_blocked(ip, BLOCKLIST)
    except ValueError:
        raise HTTPException(status_code=400, detail="invalid IP address")
    return {"ip": ip, "blocked": blocked}
