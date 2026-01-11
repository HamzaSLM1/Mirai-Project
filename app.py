from fastapi import FastAPI
from pydantic import BaseModel
from core.database import init, record, history
from core.risk_engine import check_risk
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request


app = FastAPI(title="Mirai API", version="0.1.0")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Make sure DB + table exist on startup
init()

class DoseIn(BaseModel):
    name: str
    supplement: str

@app.get("/")
def root():
    return {"status": "ok", "service": "Mirai API"}

@app.get("/web", response_class=HTMLResponse)
def web(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/dose")
def log_dose(dose: DoseIn):
    # Simple server-side time string
    from datetime import datetime
    t = datetime.now().strftime("%H:%M")
    record(dose.name, dose.supplement, t)
    return {"message": "dose logged", "name": dose.name, "supplement": dose.supplement, "time": t}

@app.get("/history/{name}")
def get_history(name: str, limit: int = 10):
    rows = history(name, limit=limit)
    return {
        "name": name,
        "count": len(rows),
        "rows": [{"date": d, "time": tm, "supplement": s} for (d, tm, s) in rows],
    }

@app.get("/risk/{name}")
def get_risk(name: str):
    return {"name": name, "risk": check_risk(name)}

