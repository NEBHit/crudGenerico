from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers.rubro_router import router as rubroRouter

app = FastAPI()

# agregar routers
app.include_router(rubroRouter)

# static
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates
templates = Jinja2Templates(directory="templates")