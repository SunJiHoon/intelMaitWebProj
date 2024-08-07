from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

# Jinja2Templates 설정
templates = Jinja2Templates(directory="templates")

# 학생별 페이지 라우팅
@router.get("/jihoon", response_class=HTMLResponse)
async def read_student_page(request: Request):
    template_path = "jihoon/index.html"
    return templates.TemplateResponse(template_path, {"request": request})

# Jihoon's forPrac 페이지 라우팅
@router.get("/jihoon/forPrac", response_class=HTMLResponse)
async def read_list_page(request: Request):
    items = ["Item 1", "Item 2", "Item 3", "Item 4"]
    return templates.TemplateResponse("jihoon/forPrac.html", {"request": request, "items": items})
