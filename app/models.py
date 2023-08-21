from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "postgresql://localhost:5432/postgres"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, future=True)
Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    text_query = Column(String, index=True)
    user_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

class OrderHistory(Base):
    __tablename__ = "order_history"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    execution_time = Column(DateTime, default=datetime.utcnow)
    image_url = Column(String)

# Теперь вызываем create_all после определения моделей
Base.metadata.create_all(bind=engine)
