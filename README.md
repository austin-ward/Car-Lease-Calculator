# Car-Lease-Calculator

Overview

This program calculates an estimated monthly lease payment for a vehicle using key parameters used by most manufacturers.
This program allows users to input values directly through the terminal, then it automatically performs the calculation, and saves each result to a CSV file for future records.
The calculator reflects how lease payments are typically estimated in a dealership environment.

# How the Lease Payment Is Calculated

The formula used is based on standard lease payment logic used in automotive finance:

Monthly Payment = (Selling Price − Residual Value) + (Money Factor × (Selling Price + Residual Value)) − Incentives / Lease Term	​

Breakdown of Each Component:

Selling Price:
The selling price of the vehicle before any incentives or rebates are applied.
This is the starting point of the lease calculation.

Residual Value:
The estimated value of the vehicle at the end of the lease term is already set by the bank. Most of the time, it's presented as a %, but in this case, it would be converted to the vehicle's remaining value after the lease term. For example, 52% of 40K would be $20,800. 
A higher residual value leads to lower monthly payments because you’re financing less depreciation.

Money Factor:
The financing rate used in leases, derived from the vehicle’s annual percentage rate (APR).
Dealerships use the formula:

Money Factor = APR / 2400

For example, an APR of 3% would equal a money factor of 0.00125.
The money factor determines how much interest you pay during the lease.

Incentives:
Rebates or manufacturer discounts are applied to lower the cost of the vehicle. (This is considered cash down.) 

Lease Term (Months):
The number of months of the lease.
Common lease terms are 24, 36, 39, or 48 months.

# Program Features

1. User inputs values through the terminal.

2. Automatic error handling for invalid numbers.

3. Clean, easy-to-read output summarizing all inputs and the final monthly payment.

4. Each calculation is saved to a CSV file (lease_records.csv) for dealership record-keeping.

5. The program can also retrieve and display recent saved records.
