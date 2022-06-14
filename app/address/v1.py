from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from address.schemas import AddressSchemas

from .database import SessionLocal
from .crud import AddressCrud

router = APIRouter(prefix="/addres",
    tags=["Address"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add")
def add_addres(addres: AddressSchemas,db: Session = Depends(get_db)):
    return AddressCrud.add_addres(db,addres)

@router.get("/")
def get_addres_with_id(id: int,db: Session = Depends(get_db)):
    addres = AddressCrud.get_addres(db,id)
    if addres is None:
            return {"detail": "Not Found"}
    return addres

@router.put("/update")
def update_addres(id: int, addres: AddressSchemas,db: Session = Depends(get_db)):
    return AddressCrud.update_addres(db,id,addres)
