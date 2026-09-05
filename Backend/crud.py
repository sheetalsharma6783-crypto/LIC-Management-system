from sqlalchemy.orm import Session
from models import Customer, Policy
from schemas import CustomerCreate, PolicyCreate
from datetime import date, timedelta
from logger import logger


def get_all_customers(db: Session):
    return db.query(Customer).all()


def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(
        Customer.customer_id == customer_id
    ).first()


def create_customer(db: Session, customer: CustomerCreate):
    new_customer = Customer(
        name=customer.name,
        age=customer.age,
        gender=customer.gender,
        dob=customer.dob,
        mobile_number=customer.mobile_number
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)
    
    logger.info(f"Customer created : {customer.customer_id}")
    
    return new_customer
def get_all_policies(db: Session):
    return db.query(Policy).all()


def get_policy_by_number(db: Session, policy_number: int):
    return db.query(Policy).filter(
        Policy.policy_number == policy_number
    ).first()


def create_policy(db: Session, policy: PolicyCreate):

    customer = db.query(Customer).filter(
        Customer.customer_id == policy.customer_id
    ).first()

    if customer is None:
        return None

    new_policy = Policy(
        customer_id=policy.customer_id,
        policy_type=policy.policy_type,
        premium_amount=policy.premium_amount,
        premium_type=policy.premium_type,
        date_of_commencement=policy.date_of_commencement,
        end_of_premium_paying=policy.end_of_premium_paying,
        date_of_maturity=policy.date_of_maturity
    )

    db.add(new_policy)
    db.commit()
    db.refresh(new_policy)
    logger.info(f"Policy created : {policy.policy_number}")
    return new_policy


def update_policy(db: Session, policy_number: int, updated_policy: PolicyCreate):

    policy = db.query(Policy).filter(
        Policy.policy_number == policy_number
    ).first()

    if policy is None:
        return None

    policy.customer_id = updated_policy.customer_id
    policy.policy_type = updated_policy.policy_type
    policy.premium_amount = updated_policy.premium_amount
    policy.premium_type = updated_policy.premium_type
    policy.date_of_commencement = updated_policy.date_of_commencement
    policy.end_of_premium_paying = updated_policy.end_of_premium_paying
    policy.date_of_maturity = updated_policy.date_of_maturity

    db.commit()
    db.refresh(policy)

    return policy


def delete_policy(db: Session, policy_number: int):

    policy = db.query(Policy).filter(
        Policy.policy_number == policy_number
    ).first()

    if policy is None:
        return None

    db.delete(policy)
    db.commit()

    return policy


def get_policies_by_customer(db: Session, customer_id: int):
    return db.query(Policy).filter(
        Policy.customer_id == customer_id
    ).all()


def update_customer(db: Session, customer_id: int, updated_customer: CustomerCreate):
    customer = db.query(Customer).filter(
        Customer.customer_id == customer_id
    ).first()

    if customer is None:
        return None

    customer.name = updated_customer.name
    customer.age = updated_customer.age
    customer.gender = updated_customer.gender
    customer.dob = updated_customer.dob
    customer.mobile_number = updated_customer.mobile_number

    db.commit()
    db.refresh(customer)

    return customer
def delete_customer(db: Session, customer_id: int):
    customer = db.query(Customer).filter(
        Customer.customer_id == customer_id
    ).first()

    if customer is None:
        return None

    db.delete(customer)
    db.commit()
    logger.info(f"Customer deleted : {customer.customer_id}")
    return customer
from sqlalchemy import func

def get_dashboard_stats(db: Session):

    total_customers = db.query(Customer).count()

    total_policies = db.query(Policy).count()

    total_premium = db.query(
        func.sum(Policy.premium_amount)
    ).scalar()

    average_premium = db.query(
        func.avg(Policy.premium_amount)
    ).scalar()

    return {
        "total_customers": total_customers,
        "total_policies": total_policies,
        "total_premium": float(total_premium or 0),
        "average_premium": float(average_premium or 0)
    }
def get_customer_summary(db: Session, customer_id: int):

    customer = db.query(Customer).filter(
        Customer.customer_id == customer_id
    ).first()

    if customer is None:
        return None

    policies = db.query(Policy).filter(
        Policy.customer_id == customer_id
    ).all()

    total_premium = sum(
        float(policy.premium_amount) for policy in policies
    )

    return {
        "customer_id": customer.customer_id,
        "name": customer.name,
        "age": customer.age,
        "gender": customer.gender,
        "mobile_number": customer.mobile_number,
        "total_policies": len(policies),
        "total_premium": total_premium,
        "policies": policies
    }
def search_customer_by_name(db: Session, name: str):
    return db.query(Customer).filter(
        Customer.name.ilike(f"%{name}%")
    ).all()
def search_customer_by_mobile(db: Session, mobile_number: str):

    mobile_number = mobile_number.strip()

    return db.query(Customer).filter(
        Customer.mobile_number.like(f"{mobile_number}%")
    ).first()
def search_policy_by_type(db: Session, policy_type: str):
    return db.query(Policy).filter(
        Policy.policy_type.ilike(f"%{policy_type}%")
    ).all()
from sqlalchemy import func
from datetime import date, timedelta

def highest_premium(db: Session):
    return db.query(func.max(Policy.premium_amount)).scalar()


def lowest_premium(db: Session):
    return db.query(func.min(Policy.premium_amount)).scalar()


def gender_distribution(db: Session):
    return db.query(
        Customer.gender,
        func.count(Customer.customer_id)
    ).group_by(Customer.gender).all()


def policy_distribution(db: Session):
    return db.query(
        Policy.policy_type,
        func.count(Policy.policy_number)
    ).group_by(Policy.policy_type).all()


def average_age(db: Session):
    return db.query(func.avg(Customer.age)).scalar()
def get_customer_from_policy(db: Session, policy_number: int):

    policy = db.query(Policy).filter(
        Policy.policy_number == policy_number
    ).first()

    if policy:
        return policy.customer

    return None
def active_policies(db: Session):
    today = date.today()
    return db.query(Policy).filter(
        Policy.date_of_maturity >= today
    ).all()
def expired_policies(db: Session):
    today = date.today()
    return db.query(Policy).filter(
        Policy.date_of_maturity < today
    ).all()
def maturity_this_year(db: Session):

    year = date.today().year

    return db.query(Policy).filter(
        func.extract("year",
        Policy.date_of_maturity)==year
    ).all()
def upcoming_maturity(db: Session):

    today = date.today()

    next30 = today + timedelta(days=30)

    return db.query(Policy).filter(
        Policy.date_of_maturity.between(today,next30)
    ).all()
from models import agent
from auth import hash_password, verify_password
from models import Customer
from auth import create_access_token


def create_agent(db: Session, agentname: str, email: str, password: str):

    existing_agent = db.query(agent).filter(
    agent.email == email).first()
    if existing_agent:
        return None

    new_agent = agent(
        username=username,
        email=email,
        password=hash_password(password)
    )

    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)

    return new_agent


def authenticate_agent(db: Session, email: str, password: str):

    agent = db.query(agent).filter(
        agent.email == email
    ).first()

    if agent is None:
        return None

    if not verify_password(password, agent.password):
        return None

    return agent
from auth import verify_password

def authenticate_customer(
    db: Session,
    mobile_number: str,
    password: str
):

    print("LOGIN MOBILE:", mobile_number)
    print("LOGIN PASSWORD:", password)

    customer = db.query(Customer).filter(
        Customer.mobile_number == mobile_number
    ).first()

    print("CUSTOMER FOUND:", customer)

    if customer is None:
        return None

    print("DATABASE PASSWORD:", customer.password)

    if customer.password != password:
        print("PASSWORD NOT MATCH")
        return None

    print("LOGIN SUCCESS")

    return customer
from auth import hash_password

def register_customer(db: Session, mobile_number: str, password: str):

    customer = db.query(Customer).filter(
        Customer.mobile_number == mobile_number
    ).first()

    if customer is None:
        return None

    if customer.password:
        return "already_registered"

    customer.password = hash_password(password)

    db.commit()
    db.refresh(customer)

    return customer