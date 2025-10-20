# Car-Lease-Calculator
Lease Payment Calculator
Overview

This program calculates an estimated monthly lease payment for a vehicle using key parameters commonly used in automotive finance.
It allows users to input values directly through the terminal, automatically performs the calculation, and saves each result to a CSV file for dealer records.
The calculator reflects how lease payments are typically estimated in a dealership environment.

How the Lease Payment Is Calculated

The formula used is based on standard lease payment logic used in automotive finance:

Monthly Payment = (Selling Price − Residual Value) + (Money Factor × (Selling Price + Residual Value)) − Incentives / Lease Term	​

Breakdown of Each Component:

Selling Price:
The negotiated price of the vehicle before any incentives or rebates are applied.
This is the starting point of the lease calculation.

Residual Value:
The estimated value of the vehicle at the end of the lease term, usually set by the leasing company.
It represents what the car is expected to be worth after depreciation.
A higher residual value leads to lower monthly payments because you’re financing less depreciation.

Money Factor:
The financing rate used in leases, derived from the vehicle’s annual percentage rate (APR).
Dealerships use the formula:

Money Factor = APR / 2400
	
For example, an APR of 3% would equal a money factor of 0.00125.
The money factor determines how much interest you pay during the lease.

Incentives:
Rebates, discounts, or manufacturer credits applied to lower the cost of the vehicle.
These reduce the total lease payment amount.

Lease Term (Months):
The number of months over which the lease is paid.
Common terms are 24, 36, or 48 months.

# Program Features

1. User inputs values through the terminal.

2. Automatic error handling for invalid numbers.

3. Clean, easy-to-read output summarizing all inputs and the final monthly payment.

4. Each calculation is saved to a CSV file (lease_records.csv) for dealership record-keeping.

5. The program can also retrieve and display recent saved records.
