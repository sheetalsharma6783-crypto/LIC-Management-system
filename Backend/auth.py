from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from database import SessionLocal
from models import agent

# ---------------- JWT CONFIG ---------------- #

SECRET_KEY = "sheetal_super_secret_key_12345"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# ---------------- PASSWORD HASH ---------------- #

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def hash_password(password):

    print("Password received:", password)

    hashed = pwd_context.hash(password)

    print("Password hashed")

    return hashed

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ---------------- CREATE TOKEN ---------------- #

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ---------------- GET CURRENT USER ---------------- #

def get_current_user(
        token: str = Depends(oauth2_scheme)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid Token"
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    db = SessionLocal()

    user = db.query(User).filter(
        User.email == email
    ).first()

    db.close()

    if user is None:
        raise credentials_exception

    return user
from models import Customer

def get_current_customer(
        token: str = Depends(oauth2_scheme)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid Customer Token"
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        customer_id = payload.get("sub")

        if customer_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    db = SessionLocal()

    customer = db.query(Customer).filter(
        Customer.customer_id == int(customer_id)
    ).first()

    db.close()

    if customer is None:
        raise credentials_exception

    return customer