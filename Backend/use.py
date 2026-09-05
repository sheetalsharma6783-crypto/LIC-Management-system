from schemas import CustomerCreate

customer = CustomerCreate(
    name="Sheetal",
    age=22,
    dob="2004-01-15",
    gender="F",
    mobile_number="9876543210"
)

print(customer)