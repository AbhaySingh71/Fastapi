def is_eligible_for_loan(income: int, age: int, employment_status: str) -> bool:
    if age < 21:
        return False
    if income < 50000:
        return False
    if employment_status.lower() != "employed":
        return False
    return True
