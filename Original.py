import sys

"""
Estimated Lease Payment Calculator Parameters

selling_price: Selling price of the car.
residual: The estimated value of the car at the end of the lease.
money_factor: The financing rate, expressed as a money factor.
incentives: Any rebates or incentives that reduce the cost.
lease_term: The duration of the lease in months.
monthly_payment: The calculated payment of the car based on the parameters set. 
"""


def calculate_lease_payment(selling_price, residual, money_factor, incentives, lease_term):

    base_cost = selling_price - residual
    interest = money_factor * (selling_price + residual)
    adjusted_cost = base_cost + interest - incentives
    monthly_payment = adjusted_cost / lease_term
    return monthly_payment


# Example Parameters
selling_price = 40000
residual = 18000
money_factor = 0.00125
incentives = 2000
lease_term = 36

monthly_payment = calculate_lease_payment(selling_price, residual, money_factor, incentives, lease_term)
print(f"Estimated Monthly Lease Payment: ${monthly_payment:.2f}")
