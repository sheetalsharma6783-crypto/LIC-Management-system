from fastapi import HTTPException


def customer_not_found():
    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )


def policy_not_found():
    raise HTTPException(
        status_code=404, 
        detail="Policy not found"
    )


def email_exists():
    raise HTTPException(
        status_code=400,
        detail="Email already exists"
    )


def invalid_login():
    raise HTTPException(
        status_code=401,
        detail="Invalid email or password"
    )