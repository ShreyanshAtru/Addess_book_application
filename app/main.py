from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from address.v1 import router as address_app
from address.database import engine
from address import models as address_model

app = FastAPI(title="Location API")

address_model.Base.metadata.create_all(bind=engine)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(address_app)
