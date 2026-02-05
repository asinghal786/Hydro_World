from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.routes.train import router as train_router
from backend.routes.history import router as history_router
from backend.routes.predict import router as predict_router

# --------------------------------------------------
# CREATE APP (THIS IS WHAT WAS MISSING)
# --------------------------------------------------
app = FastAPI(title="Hydro_World API")

# --------------------------------------------------
# CORS
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# API ROUTES
# --------------------------------------------------
app.include_router(train_router, prefix="/api")
app.include_router(history_router, prefix="/api")
app.include_router(predict_router, prefix="/api")

# --------------------------------------------------
# WEB (YOUR STRUCTURE: web/)
# --------------------------------------------------
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")


from fastapi import Request

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
