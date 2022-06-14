from sqlalchemy.orm.session import Session

from .models import Address
from .schemas import AddressSchemas


class AddressCrud():

    def add_addres(db: Session, addres: AddressSchemas):
        try:
            obj = Address(line1=addres.line1, latitude=addres.latitude, longitude=addres.longitude)
        except Exception as e:
            return{"detail": "Server error.", "error":str(e)}
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return {"detail":"Data added Successfully!", "data":obj}

    def get_addres(db: Session, id: int):
        addres = db.query(Address).filter(Address.id == id).first()
        if addres is None:
            return None
        return {"data":addres}
    
    def update_addres(db: Session, id: int, data: AddressSchemas):
        res = AddressCrud.get_addres(db,id)
        if res is None:
            return {"detail": "Not Found"}
        addres = res.get("data")
        addres.line1 = data.line1
        addres.latitude = data.latitude
        addres.longitude = data.longitude
        db.commit()
        db.refresh(addres)
        return {"detail":"Addres Update Successfully!","data":addres}
