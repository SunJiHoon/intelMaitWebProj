from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from users import jihoon   # jihoon 모듈 임포트

from users.elementary import imsoun
from users.elementary import johayun
from users.elementary import leedanwoo
from users.elementary import leehaechan
from users.elementary import notaewan

from users.intermediate import junjunghyeon
from users.intermediate import kimminjae
from users.intermediate import leewoohyeon
from users.intermediate import parksiwoo


app = FastAPI()

# Static files 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# jihoon 라우터 포함
app.include_router(jihoon.router)
app.include_router(imsoun.router)
app.include_router(johayun.router)
app.include_router(leedanwoo.router)
app.include_router(leehaechan.router)
app.include_router(notaewan.router)

app.include_router(junjunghyeon.router)
app.include_router(kimminjae.router)
app.include_router(leewoohyeon.router)
app.include_router(parksiwoo.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
