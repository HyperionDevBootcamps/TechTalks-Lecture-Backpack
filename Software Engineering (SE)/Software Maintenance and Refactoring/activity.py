
class Employee:
    """
    This is a docstring is about the function
    """
    def __init__(self, role, base, multiplier=1):
        self.role = role
        self.base = base
        self.multiplier = multiplier
        self.bonus = self.base * self.multiplier
        self.tax = (self.base + self.bonus) * self.multiplier

# This is a comment

def calculate_salary(employee):
    """
    This is a docstring is about the function
    """
    # This comment is about the manager
    if employee["role"] == "manager":
        base = 5000
        bonus = base * 0.1
        # This is a comment
        tax = (base + bonus) * 0.25
        net = base + bonus - tax
    elif employee["role"] == "developer":
        base = 4000
        bonus = calculate_bonus()
        tax = (base + bonus) * 0.2
        net = base + bonus - tax
    elif employee["role"] == "intern":
        base = 2000
        bonus = 0
        tax = base * 0.1
        # This is a comment
        net = base - tax
    return net

def calculate_bonus(employee):
    return "bonus"

# This is a comment
print(calculate_salary({"role": "intern"}))


def doStuff(a, b):
    return (a + b) * 0.9 - 100 + (a * 3.14)
	
Problems:
Poor function name (doStuff gives no indication of purpose)
No comments or docstring
Magic numbers (0.9, 100, 3.14) with no explanation
Unclear purpose

# -----------------------------------------------------------------------------
def process_order(order):
    print("Processing order for", order["customer"])
    if order["type"] == "online":
        send_email(order["customer"])
    elif order["type"] == "pickup":
        print("Customer will pick up")
    else:
        print("Unknown order type")
    with open("orders.txt", "a") as f:
        f.write(str(order) + "\n")
		
Problems:
UI, business logic, and persistence are tightly coupled
No error handling
Hard to modify if logic or output format changes
Reuse and testing are difficult

# -----------------------------------------------------------------------------

def calculate_salary(employee):
    if employee["role"] == "manager":
        base = 5000
        bonus = base * 0.1
        tax = (base + bonus) * 0.25
        net = base + bonus - tax
    elif employee["role"] == "developer":
        base = 4000
        bonus = base * 0.05
        tax = (base + bonus) * 0.2
        net = base + bonus - tax
    elif employee["role"] == "intern":
        base = 2000
        bonus = 0
        tax = base * 0.1
        net = base - tax
    return net

Problems:
Lots of duplication
Hard to add a new role
Logic is buried in conditional blocks

# -----------------------------------------------------------------------------

def validate_user(user):
    if user is not None:
        if "name" in user:
            if user["name"] != "":
                if "email" in user:
                    if user["email"].find("@") != -1:
                        return True
    return False

Problems:
Hard to read
Deep nesting instead of early returns
No clear separation of validation steps