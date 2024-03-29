from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from src.db.db_connection import get_db
from src.repository import users as repository_users
from src.schemas import TokenModel, UserModel, UserResponse
from src.services.auth import auth_service


router = APIRouter(prefix='/auth', tags=['auth'])
security = HTTPBearer()


@router.post('/signup', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(body: UserModel, db: Session = Depends(get_db)):
    """
    Sign up a new user.
    :param body: The user data to sign up.
    :type body: UserModel
    :param db: The database session.
    :type db: Session
    :return: The newly created user and a success message.
    :rtype: dict
    """

    exist_user = await repository_users.get_user_by_email(body.email, db)

    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Account already exists')

    body.password = auth_service.get_password_hash(body.password)
    new_user = await repository_users.create_user(body, db)

    return {'user': new_user, 'detail': 'User successfully created'}


@router.post('/login', response_model=TokenModel)
async def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Log in a user and generate an access token and a refresh token.
    :param body: The login credentials.
    :type body: OAuth2PasswordRequestForm
    :param db: The database session.
    :type db: Session
    :return: The access token and refresh token.
    :rtype: dict
    """

    user = await repository_users.get_user_by_email(body.username, db)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid email')

    if not auth_service.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid password')

    access_token = await auth_service.create_access_token(data={'sub': user.email})
    refresh_token = await auth_service.create_refresh_token(data={'sub': user.email})

    await repository_users.update_token(user, refresh_token, db)

    return {'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'}


@router.get('/refresh_token', response_model=TokenModel)
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    """
    Refresh an access token using a refresh token.
    :param credentials: The authorization credentials.
    :type credentials: HTTPAuthorizationCredentials
    :param db: The database session.
    :type db: Session
    :return: The new access token and refresh token.
    :rtype: dict
    """

    token = credentials.credentials

    email = await auth_service.decode_refresh_token(token)
    user = await repository_users.get_user_by_email(email, db)

    if user.refresh_token != token:
        await repository_users.update_token(user, None, db)

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid refresh token')

    access_token = await auth_service.create_access_token(data={'sub': email})
    refresh_token = await auth_service.create_refresh_token(data={'sub': email})

    await repository_users.update_token(user, refresh_token, db)

    return {'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'}
