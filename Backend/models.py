from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    dob = Column(Date)
    mobile_number = Column(String)
    password = Column(String)

    policies = relationship("Policy", back_populates="customer")

class Policy(Base):
    __tablename__ = "policy"

    policy_number = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    policy_type = Column(String)
    premium_amount = Column(Numeric)
    premium_type = Column(String)
    date_of_commencement = Column(Date)
    end_of_premium_paying = Column(Date)
    date_of_maturity = Column(Date)

    customer = relationship("Customer", back_populates="policies")
class agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)