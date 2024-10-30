from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Availability(Base):
    __tablename__ = "availabilities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    coming_week = Column(String, index=True)
    next_two_weeks = Column(String, index=True)
    long_term = Column(String, index=True)

Base.metadata.create_all(bind=engine)

class AvailabilityCreate(BaseModel):
    name: str
    coming_week: str
    next_two_weeks: str
    long_term: str

class AvailabilityUpdate(BaseModel):
    coming_week: str
    next_two_weeks: str
    long_term: str

@app.post("/availabilities/", response_model=AvailabilityCreate)
def create_availability(availability: AvailabilityCreate):
    db = SessionLocal()
    db_availability = Availability(**availability.dict())
    db.add(db_availability)
    db.commit()
    db.refresh(db_availability)
    db.close()
    return db_availability

@app.get("/availabilities/", response_model=List[AvailabilityCreate])
def read_availabilities(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    availabilities = db.query(Availability).offset(skip).limit(limit).all()
    db.close()
    return availabilities

@app.put("/availabilities/{availability_id}", response_model=AvailabilityUpdate)
def update_availability(availability_id: int, availability: AvailabilityUpdate):
    db = SessionLocal()
    db_availability = db.query(Availability).filter(Availability.id == availability_id).first()
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    for key, value in availability.dict().items():
        setattr(db_availability, key, value)
    db.commit()
    db.refresh(db_availability)
    db.close()
    return db_availability

@app.delete("/availabilities/{availability_id}")
def delete_availability(availability_id: int):
    db = SessionLocal()
    db_availability = db.query(Availability).filter(Availability.id == availability_id).first()
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    db.delete(db_availability)
    db.commit()
    db.close()
    return {"detail": "Availability deleted"}
