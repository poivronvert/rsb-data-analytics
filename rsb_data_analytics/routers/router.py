from fastapi import APIRouter, HTTPException, Request, status, Response
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import rsb_data_analytics
import logging, os
LIB_ROOT:os.PathLike = os.path.dirname(os.path.realpath(rsb_data_analytics.__file__))
router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(LIB_ROOT, 'templates'))
router.mount("/static", StaticFiles(directory=os.path.join(LIB_ROOT, 'static')), name="static")

@router.get("/", response_class=HTMLResponse)
async def redirect_homepage(request: Request):
    return RedirectResponse("/about")

@router.get("/favicon.ico")
async def get_favicon(request: Request):
    favicon_path = os.path.join(os.path.join(LIB_ROOT, 'templates'), "favicon.ico")
    return FileResponse(path=favicon_path, media_type="image/vnd.microsoft.icon")

@router.get("/colosscious-logo.svg")
async def get_logo_svg(request: Request):
    favicon_path = os.path.join(os.path.join(LIB_ROOT, 'templates'), "colosscious-logo.svg")
    return FileResponse(path=favicon_path, media_type="image/svg+xml")

@router.get("/about", response_class=HTMLResponse)
async def get_about(request:Request):
    return templates.TemplateResponse("author.html", context={"request": request})

@router.get("/dashboard", response_class=HTMLResponse)
async def get_about(request:Request):
    return templates.TemplateResponse("dashboard.html", context={"request": request})