from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Form

router = APIRouter()

# Jinja2Templates 설정
templates = Jinja2Templates(directory="templates")

# imsoun's index 페이지 라우팅
@router.get("/intermediate/junjunghyeon", response_class=HTMLResponse)
async def read_student_page(request: Request):
    template_path = "intermediate/junjunghyeon/index.html"
    return templates.TemplateResponse(template_path, {"request": request})

# imsoun's forPrac 페이지 라우팅
@router.get("/intermediate/junjunghyeon/forPrac", response_class=HTMLResponse)
async def read_list_page(request: Request):
    items = ["Item 1", "Item 2", "Item 3", "Item 4"]
    return templates.TemplateResponse("intermediate/junjunghyeon/forPrac.html", {"request": request, "items": items})


@router.get("/intermediate/junjunghyeon/calc", response_class=HTMLResponse)
async def get_calc_page(request: Request):
    return templates.TemplateResponse("intermediate/junjunghyeon/calc.html", {"request": request})

# imsoun's calc 페이지 라우팅 (POST 요청)
@router.post("/intermediate/junjunghyeon/calc", response_class=HTMLResponse)
async def post_calc_page(request: Request, num1: float = Form(...), num2: float = Form(...), operation: str = Form(...)):
    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    return templates.TemplateResponse("intermediate/junjunghyeon/calc.html", {"request": request, "result": result, "num1": num1, "num2": num2, "operation": operation})
