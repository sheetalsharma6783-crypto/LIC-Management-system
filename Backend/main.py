from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from typing import List
from database import SessionLocal, get_db
from database import engine
from crud import get_dashboard_stats
from crud import get_customer_from_policy
from schemas import agentCreate, agentLogin
from crud import create_agent, authenticate_agent
from auth import create_access_token, get_current_user
from fastapi import Depends
from models import Base
from database import engine
from schemas import CustomerLogin
from crud import authenticate_customer
from crud import get_policies_by_customer
from sqlalchemy.orm import Session
from schemas import CustomerRegister
from crud import register_customer
from AI.rag import ask_rag
from models import Customer, Policy

from crud import (
    get_all_customers,
    get_customer_by_id,
    create_customer,
    update_customer,
    delete_customer,
    get_all_policies,
    get_policy_by_number,
    create_policy,
    update_policy,
    delete_policy,
    get_policies_by_customer,
    get_customer_summary,
    search_customer_by_name,
    search_customer_by_mobile,
    search_policy_by_type,
    highest_premium,
    lowest_premium,
    gender_distribution,
    policy_distribution,
    average_age
)

from schemas import (
    CustomerCreate,
    CustomerResponse,
    PolicyCreate,
    PolicyResponse
)
from exceptions import (
    customer_not_found,
    policy_not_found,
    email_exists,
    invalid_login
)
Base.metadata.create_all(bind=engine)
print("Tables created")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5175",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Insurance Management System"
    }


# ---------------------- CUSTOMER APIs ---------------------- #

@app.get("/customers", response_model=List[CustomerResponse])
def customers(current_user=Depends(get_current_user)):

    db = SessionLocal()

    try:
        return get_all_customers(db)

    finally:
        db.close()


@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def customer(customer_id: int):

    db = SessionLocal()

    try:
        data = get_customer_by_id(db, customer_id)

        if data is None:
            customer_not_found()

        return data

    finally:
        db.close()


@app.post("/customers", response_model=CustomerResponse)
def add_customer(customer: CustomerCreate):

    db = SessionLocal()

    try:
        return create_customer(db, customer)

    finally:
        db.close()


@app.put("/customers/{customer_id}", response_model=CustomerResponse)
def update(customer_id: int, customer: CustomerCreate):

    db = SessionLocal()

    try:
        updated_customer = update_customer(db, customer_id, customer)

        if updated_customer is None:
            customer_not_found()
        return updated_customer

    finally:
        db.close()


@app.delete("/customers/{customer_id}")
def delete(customer_id: int):

    db = SessionLocal()

    try:
        deleted_customer = delete_customer(db, customer_id)

        if deleted_customer is None:
            customer_not_found()
        return {
            "message": "Customer deleted successfully"
        }

    finally:
        db.close()


# ---------------------- POLICY APIs ---------------------- #

@app.get("/policies", response_model=List[PolicyResponse])
def policies():

    db = SessionLocal()

    try:
        return get_all_policies(db)

    finally:
        db.close()


@app.get("/policies/{policy_number}", response_model=PolicyResponse)
def policy(policy_number: int):

    db = SessionLocal()

    try:
        data = get_policy_by_number(db, policy_number)

        if data is None:
            policy_not_found()

        return data

    finally:
        db.close()


@app.post("/policies", response_model=PolicyResponse)
def add_policy(policy: PolicyCreate):

    db = SessionLocal()

    try:
        new_policy = create_policy(db, policy)

        if new_policy is None:
           customer_not_found()

        return new_policy

    finally:
        db.close()


@app.put("/policies/{policy_number}", response_model=PolicyResponse)
def update_policy_api(policy_number: int, policy: PolicyCreate):

    db = SessionLocal()

    try:
        updated_policy = update_policy(
            db,
            policy_number,
            policy
        )

        if updated_policy is None:
           policy_not_found()

        return updated_policy

    finally:
        db.close()


@app.delete("/policies/{policy_number}")
def delete_policy_api(policy_number: int):

    db = SessionLocal()

    try:
        deleted_policy = delete_policy(
            db,
            policy_number
        )

        if deleted_policy is None:
            policy_not_found()

        return {
            "message": "Policy deleted successfully"
        }

    finally:
        db.close()


@app.get("/customers/{customer_id}/policies")
def customer_policies(customer_id: int, db: Session = Depends(get_db)):
    return get_policies_by_customer(db, customer_id)
@app.get("/customers/{customer_id}/summary")
def customer_summary(customer_id: int):

    db = SessionLocal()

    try:
        data = get_customer_summary(db, customer_id)

        if data is None:
            customer_not_found()

        return data

    finally:
        db.close()
@app.get("/dashboard")
def dashboard():

    db = SessionLocal()

    try:
        return get_dashboard_stats(db)

    finally:
        db.close()
@app.get("/customers/search/name/{name}", response_model=List[CustomerResponse])
def search_name(name: str):

    db = SessionLocal()

    try:
        return search_customer_by_name(db, name)

    finally:
        db.close()
@app.get("/customers/search/mobile/{mobile_number}", response_model=CustomerResponse)
def search_mobile(mobile_number: str):

    db = SessionLocal()

    try:
        customer = search_customer_by_mobile(db, mobile_number)

        if customer is None:
            customer_not_found()
        return customer

    finally:
        db.close()
@app.get("/policies/search/type/{policy_type}", response_model=List[PolicyResponse])
def search_policy(policy_type: str):

    db = SessionLocal()

    try:
        return search_policy_by_type(db, policy_type)

    finally:
        db.close()
@app.get("/analytics/highest-premium")
def get_highest():
    db = SessionLocal()
    return {"highest_premium": highest_premium(db)}
@app.get("/analytics/lowest-premium")
def get_lowest():
    db = SessionLocal()
    return {"lowest_premium": lowest_premium(db)}
@app.get("/analytics/average-age")
def avg_age():
    db = SessionLocal()
    return {"average_age": average_age(db)}
@app.get("/analytics/gender-distribution")
def gender():
    db = SessionLocal()

    data = gender_distribution(db)

    return {g: c for g, c in data}
@app.get("/analytics/policy-distribution")
def policy():
    db = SessionLocal()

    data = policy_distribution(db)

    return {p: c for p, c in data}
@app.get("/policies/{policy_number}/customer",
response_model=CustomerResponse)
def customer_from_policy(policy_number: int):

    db = SessionLocal()

    customer = get_customer_from_policy(db, policy_number)

    if customer is None:
       policy_not_found()
    return customer
@app.post("/register")
def register(agent: agentCreate):

    print("Received Data:")
    print(agent)

    db = SessionLocal()

    try:
        new_agent = create_agent(
            db,
            agent.username,
            agent.email,
            agent.password
        )

        if new_agent is None:
            email_exists()

        return {
            "message": "Agent registered successfully"
        }

    finally:
        db.close()
@app.post("/login")
def login(agent: agentLogin):
    db = SessionLocal()

    try:

        valid_agent = authenticate_agent(
            db,
            agent.email,
            agent.password
        )

        if valid_agent is None:
            invalid_login()

        from logger import logger
        logger.info(f"{valid_agent.email} logged in")

        token = create_access_token(
            {"sub": valid_agent.email}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    finally:
        db.close()


@app.get("/customer/{customer_id}/policies", response_model=List[PolicyResponse])
def customer_policies(customer_id: int):

    db = SessionLocal()

    try:
        return get_customer_policies(db, customer_id)

    finally:
        db.close()

@app.post("/customer-login")
def customer_login(customer: CustomerLogin):

    db = SessionLocal()

    try:

        valid_customer = authenticate_customer(
            db,
            customer.mobile_number,
            customer.password
        )

        if valid_customer is None:
            raise HTTPException(
                status_code=401,
                detail="Customer not found"
            )

        token = create_access_token(
            {"sub": str(valid_customer.customer_id)}
        )

        return {
            "access_token": token,
            "customer": {
                "customer_id": valid_customer.customer_id,
                "name": valid_customer.name,
                "mobile_number": valid_customer.mobile_number
            }
        }

    finally:
        db.close()
@app.post("/customer-register")
def customer_register(customer: CustomerRegister):

    db = SessionLocal()

    try:

        result = register_customer(
            db,
            customer.mobile_number,
            customer.password
        )

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        if result == "already_registered":
            raise HTTPException(
                status_code=400,
                detail="Customer already registered"
            )

        return {
            "message": "Registration Successful"
        }

    finally:
        db.close()
from pydantic import BaseModel

class AIRequest(BaseModel):
    customer_id: int
    question: str

@app.post("/ask-ai")
def ask_ai(data: AIRequest):

    customer_id = data.customer_id
    question = data.question

    db = SessionLocal()

    try:

        customer = db.query(Customer).filter(
            Customer.customer_id == customer_id
        ).first()

        if customer is None:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        policies = db.query(Policy).filter(
            Policy.customer_id == customer_id
        ).all()

        context = f"""
Customer Name: {customer.name}
Mobile Number: {customer.mobile_number}
Age: {customer.age}
Gender: {customer.gender}

Policies:
"""

        for p in policies:

            context += f"""

Policy Number: {p.policy_number}
Policy Type: {p.policy_type}
Premium Amount: {p.premium_amount}
Premium Type: {p.premium_type}
Commencement Date: {p.date_of_commencement}
Maturity Date: {p.date_of_maturity}

"""

        answer = ask_rag(question, context)

        return {
            "answer": answer
        }

    finally:
        db.close()