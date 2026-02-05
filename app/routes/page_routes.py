from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from fastapi.templating import Jinja2Templates

PageRouter = APIRouter(
    prefix="",
    tags=["Páginas"]
)

templates = Jinja2Templates(directory="app/templates")

@PageRouter.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {"request": request, "title": "Weather GO"}
    return templates.TemplateResponse(name="home.html", context=context)
@PageRouter.get("/about", response_class=HTMLResponse)
def home(request: Request):
    context = {"request": request, "title": "Weather GO - Sobre"}
    return templates.TemplateResponse(name="about.html", context=context)