from datetime import datetime, timedelta
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status

from sqlalchemy import text
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import Contact, ContactRequest, ContactResponse


router = APIRouter(prefix='/contacts', tags=['contacts'])


@router.post('/', response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(contact: ContactRequest, db: Session = Depends(get_db)):
    if db.query(Contact).filter_by(phone_number=contact.phone_number).first():
        raise HTTPException(status_code=400, detail='The phone number is already in the database')

    db_contact = Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    return db_contact


@router.get('/', response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    contact = db.query(Contact).offset(skip).limit(limit=limit).all()

    return contact


@router.get('/{contact_id}', response_model=ContactResponse)
async def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()

    if contact is None:
        raise HTTPException(status_code=404, detail='Contact is missing')

    else:
        return contact


@router.put('/{contact_id}', response_model=ContactResponse)
async def update_contact(contact_id: int, updated_contact: ContactRequest, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()

    if contact is None:
        raise HTTPException(status_code=404, detail='Contact is missing')

    for attr, value in updated_contact.model_dump().items():
        setattr(contact, attr, value)

    db.commit()
    db.refresh(contact)

    return contact


@router.delete('/{contact_id}', response_model=ContactResponse)
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()

    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact is missing')

    else:
        db.delete(contact)
        db.commit()

        return contact


@router.get('/', response_model=List[ContactResponse])
async def search_contacts(
        query: str = Query(..., description='Search by first name, last name or email address'),
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db),
):
    contacts = (
        db.query(Contact).filter(
            Contact.first_name.ilike(f'%{query}%')
            | Contact.last_name.ilike(f'%{query}%')
            | Contact.email.ilike(f'%{query}%')
        ).offset(skip).limit(limit=limit).all()
    )

    return contacts


@router.get('/birthday', response_model=List[ContactResponse])
async def future_birthdays(db: Session = Depends(get_db)):
    today = datetime.today()
    today_plus_seven_days = today + timedelta(days=7)
    future_birthdays_in_current_year = (
        db.query(Contact).filter(text("TO_CHAR(birthday, 'MM-DD') BETWEEN :start_date AND :end_date"))
        .params(start_date=today.strftime('%m-%d'), end_date=today_plus_seven_days.strftime('%m-%d')).all()
    )

    return future_birthdays_in_current_year
