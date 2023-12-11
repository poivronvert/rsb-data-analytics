import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import logging
from rsb_data_analytics.routers.router import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='0.0.0.0',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LIB_ROOT:os.PathLike = os.path.dirname(os.path.realpath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(LIB_ROOT, 'static')), name="static")

app.include_router(router)
logging.info('Start listen on: http://localhost:21116')