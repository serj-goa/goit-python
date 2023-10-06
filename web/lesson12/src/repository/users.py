from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.db.models import User
from src.schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User:
    return db.query(User).filter(User.email == email).first()


async def create_user(body: UserModel, db: Session) -> User:
    avatar = None

    try:
        g = Gravatar(body.email)
        avatar = g.get_image()

    except Exception as err:
        print(err)

    new_user = User(**body.model_dump(), avatar=avatar)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    user.refresh_token = token
    db.commit()
