from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models_sql import Usuario, Mascota, Users, Pets

router = APIRouter()


def register_crud(router, model):
    table = model.__tablename__
    cols = [c.name for c in model.__table__.columns]

    def list_items(db: Session = Depends(get_db)):
        items = db.query(model).all()
        return [i.to_dict() for i in items]

    def get_item(item_id: int, db: Session = Depends(get_db)):
        item = db.get(model, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Not found")
        return item.to_dict()

    def create_item(data: dict, db: Session = Depends(get_db)):
        payload = {k: v for k, v in data.items() if k in cols}
        item = model(**payload)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item.to_dict()

    def update_item(item_id: int, data: dict, db: Session = Depends(get_db)):
        item = db.get(model, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Not found")
        for k, v in data.items():
            if k in cols:
                setattr(item, k, v)
        db.commit()
        db.refresh(item)
        return item.to_dict()

    def delete_item(item_id: int, db: Session = Depends(get_db)):
        item = db.get(model, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Not found")
        db.delete(item)
        db.commit()
        return {"status": "deleted"}

    # register routes
    router.add_api_route(f"/{table}", list_items, methods=["GET"])
    router.add_api_route(f"/{table}/{{item_id}}", get_item, methods=["GET"])
    router.add_api_route(f"/{table}", create_item, methods=["POST"])
    router.add_api_route(f"/{table}/{{item_id}}", update_item, methods=["PUT"])
    router.add_api_route(f"/{table}/{{item_id}}", delete_item, methods=["DELETE"])


# Register CRUD for our detected models
register_crud(router, Usuario)
register_crud(router, Mascota)
register_crud(router, Users)
register_crud(router, Pets)

# additional simple endpoints
@router.get('/health')
def health():
    return {"status": "ok"}
