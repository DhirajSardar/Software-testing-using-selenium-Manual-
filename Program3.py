def calculate_commission(sales_amount, commission_rate):
    if sales_amount < 0:
        return "Invalid sales amount"
    elif commission_rate < 0 or commission_rate > 1:
        return "Invalid commission rate"
    else:
        commission = sales_amount * commission_rate
        return commission

# Test Cases
test_cases = [
    {"sales_amount": 1000, "commission_rate": 0.1, "expected_commission": 100},
    {"sales_amount": 2000, "commission_rate": 0.2, "expected_commission": 400},
    {"sales_amount": 500, "commission_rate": 0.05, "expected_commission": 25},
    {"sales_amount": -100, "commission_rate": 0.1, "expected_commission": "Invalid sales amount"},
    {"sales_amount": 1000, "commission_rate": 1.1, "expected_commission": "Invalid commission rate"},
    {"sales_amount": 0, "commission_rate": 0.1, "expected_commission": 0},
]

# Execute Test Cases
for test_case in test_cases:
    sales_amount = test_case["sales_amount"]
    commission_rate = test_case["commission_rate"]
    expected_commission = test_case["expected_commission"]
    actual_commission = calculate_commission(sales_amount, commission_rate)
    if actual_commission == expected_commission:
        print(f"Test Case Passed: Sales Amount={sales_amount}, Commission Rate={commission_rate}, Expected Commission={expected_commission}")
    else:
        print(f"Test Case Failed: Sales Amount={sales_amount}, Commission Rate={commission_rate}, Expected Commission={expected_commission}, Actual Commission={actual_commission}")
