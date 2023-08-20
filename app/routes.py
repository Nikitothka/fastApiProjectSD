from fastapi import APIRouter, HTTPException
from .models import SessionLocal, Order
from .tasks import generate_image

router = APIRouter()

@router.post("/orders/")
async def create_order(text_query: str, user_id: int):
    session = SessionLocal()
    try:
        new_order = Order(text_query=text_query, user_id=user_id)
        session.add(new_order)
        session.commit()
        generate_image.delay(text_query)
        return {"message": "Order received and added to the queue"}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()
