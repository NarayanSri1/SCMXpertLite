from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from route import add

# including origins to get input
origins = [
    "*"
]

app=FastAPI()

# prevents CORS error and router
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# exception 500
@app.exception_handler(500)
async def internal_exception_handler(request:Request, exc:Exception):
    return JSONResponse(status_code=500, content=jsonable_encoder({"code": 500, "msg": "Internal Server Error"}))

# encodes route api add into app
app.include_router(add)

