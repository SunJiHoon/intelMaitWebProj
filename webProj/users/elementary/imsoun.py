from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

# Jinja2Templates 설정
templates = Jinja2Templates(directory="templates")

# imsoun's index 페이지 라우팅
@router.get("/elementary/imsoun", response_class=HTMLResponse)
async def read_student_page(request: Request):
    template_path = "elementary/imsoun/index.html"
    return templates.TemplateResponse(template_path, {"request": request})

# imsoun's forPrac 페이지 라우팅
@router.get("/elementary/imsoun/forPrac", response_class=HTMLResponse)
async def read_list_page(request: Request):
    items = ["Item 1", "Item 2", "Item 3", "Item 4"]
    return templates.TemplateResponse("elementary/imsoun/forPrac.html", {"request": request, "items": items})
