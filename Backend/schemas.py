from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import date
from decimal import Decimal


# ---------------- CUSTOMER ---------------- #

class CustomerCreate(BaseModel):
    name: str
    age: int
    dob: date
    gender: str
    mobile_number: str


class CustomerResponse(BaseModel):
    customer_id: int
    name: str
    age: int
    dob: date
    gender: str
    mobile_number: str

    model_config = ConfigDict(from_attributes=True)


# ---------------- POLICY ---------------- #

class PolicyCreate(BaseModel):
    customer_id: int
    policy_type: str
    premium_amount: Decimal
    premium_type: str
    date_of_commencement: date
    end_of_premium_paying: date
    date_of_maturity: date


from pydantic import BaseModel
from datetime import date
from decimal import Decimal


class PolicyResponse(BaseModel):
    policy_number: int
    customer_id: int
    policy_type: str
    premium_amount: Decimal
    premium_type: str
    date_of_commencement: date

    class Config:
        from_attributes = True

# ---------------- USER ---------------- #

class agentCreate(BaseModel):
    username: str
    email: str
    password: str


class agentLogin(BaseModel):
    email: str
    password: str

class CustomerLogin(BaseModel):
    mobile_number: str
    password: str
class CustomerRegister(BaseModel):
    mobile_number: str
    password: str
class AIRequest(BaseModel):
    customer_id: int
    question: str