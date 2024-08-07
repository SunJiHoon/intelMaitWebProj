from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Static files 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2Templates 설정
templates = Jinja2Templates(directory="templates")

# 학생별 페이지 라우팅
@app.get("/jihoon", response_class=HTMLResponse)
async def read_student_page(request: Request):
    template_path = "jihoon/index.html"
    return templates.TemplateResponse(template_path, {"request": request})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)