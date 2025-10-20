import sys
import csv
import os
from datetime import datetime

"""
Estimated Lease Payment Calculator Parameters

selling_price: Selling price of the car.
residual: The estimated value of the car at the end of the lease.
money_factor: The financing rate, expressed as a money factor.
incentives: Any rebates or incentives that reduce the cost.
lease_term: The duration of the lease in months.
monthly_payment: The calculated payment of the car based on the parameters set. 
"""
"""
Additions to program for CINF308 Midterm SUNY at Albany | Fall 2025
1) Terminal input fields for each parameter
2) Error handling for invalid inputs
3) Save each calculated payment to a CSV file for record keeping
4) Simple retrieval of saved records
5) Cleaner and more detailed output of figures

CSV File: lease_records.csv
CSV File Columns: Time, Selling Price, Residual, Money Factor, Incentives, Term, Monthly Payment

"""


def main():
    # Menu for user in console.
    while True:
        print("Car Lease Payment Calculator")
        print("1) New lease payment")
        print("2) Past lease payments")
        print("3) Quit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            calculation()
        elif choice == "2":
            display_records()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.\n")


def calculate_lease_payment(selling_price, residual, money_factor, incentives, lease_term):
    """
    Calculate estimated monthly lease payment.
    Parameters are expected as numeric types (floats except lease_term as int).
    """
    base_cost = selling_price - residual
    interest = money_factor * (selling_price + residual)
    adjusted_cost = base_cost + interest - incentives
    monthly_payment = adjusted_cost / lease_term
    return round(monthly_payment, 2)

def calculation():
    # Option 1 on the menu to collect points of data to perform the lease calculation.
    print("\nEnter Lease Figures:")

    selling_price = input_float(" Selling Price ($): ", min_value=0.0)
    residual = input_float("  Residual value ($): ", min_value=0.0)
    money_factor = input_float("  Money factor (e.g., 0.00125): ", min_value=0.0)
    incentives = input_float("  Total incentives/rebates ($): ", min_value=0.0)
    lease_term = input_int("  Lease term (months): ", min_value=12)

    # Calc logic firewall
    if residual > selling_price:
        print("Residual cannot be greater than selling price.")

    monthly_payment = calculate_lease_payment(
        selling_price, residual, money_factor, incentives, lease_term
    )

    # Structured Calculation Output
    print("Lease Payment Summary")
    print("------------------------------------------")
    print(f" Selling Price: ${selling_price:,.2f}")
    print(f" Residual Value: ${residual:,.2f}")
    print(f" Money Factor: {money_factor:.6f}")
    print(f" Incentives: ${incentives:,.2f}")
    print(f" Lease Term: {lease_term} months")
    print("------------------------------------------")
    print(f" Estimated Payment: ${monthly_payment:,.2f} / month")


def input_float(prompt_text, min_value=None):
    # Error Handling
    while True:
        raw = input(prompt_text).strip()
        try:
            val = float(raw)
            if min_value is not None and val < min_value:
                print(f"Value must be ≥ {min_value}.")
                continue
            return val
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


if __name__ == "__main__":
    main()
