def greet_user():
    print("Welcome to code")

greet_user()

def display_student_info(name, university="KBTU"):
    print(f"Student {name} studies at {university}.")

display_student_info("Yerkhan")
display_student_info("Dana", " Meta University")

def calculate_discount(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price

price_with_discount = calculate_discount(25000, 10)
print(f"The final price after discount is: ${price_with_discount}")

def calculate_total_sales(*sales):
    total = sum(sales)
    print(f"Total sales amount: ${total}")

def print_car_details(**details):
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

calculate_total_sales(21500, 15000, 17000)
print_car_details(brand="Changan Deepal", model="S09 Ultra", year=2026, type="SUV")

add_tax = lambda price: price + (price * 0.12)
print(f"Price with tax: {add_tax(100)}")

multiply_dimensions = lambda length, width: length * width
print(f"Area is: {multiply_dimensions(4, 5)}")