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
    """Menu for user in console."""
    while True:
        print("Car Lease Payment Calculator")
        print("1) New lease payment")
        print("2) Past lease payments")
        print("3) Quit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            calculate_flow()
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


if __name__ == "__main__":
    main()
