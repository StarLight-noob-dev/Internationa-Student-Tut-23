__author__ = "727995, Calderon"


def celsius_to_fahrenheit():
    """Ask for an input repesenting a termperature on Celsius and return the corresponding
    value in Fahrenheit
    """

    # input
    celsius = float(input("Enter temperature in Celsius: "))

    # calculation
    fahr = celsius * (9/5) + 32

    # output
    print(f"The temperature in Fahrenheit is: {fahr}")


def calculate_price():

    # inputs
    price = float(input("Enter the price of the product: "))
    number = int(input("Enter the amount of the product: "))

    discount = 0.0

    # discount logic
    if number >= 100:
        discount = 0.15
    elif number >= 10:
        discount = 0.07
    elif number >= 5:
        discount = 0.05

    # calculation
    total = price * number
    total -= (total * discount)

    # outputs
    if discount == 0:
        print("You got no discount this time")
    else:
        print(f"You got a {int(discount * 100)}% discount on this purchase.")

    print(f"The total price is {total:.2f}")

if __name__ == "__main__":
    celsius_to_fahrenheit()
    calculate_price()
