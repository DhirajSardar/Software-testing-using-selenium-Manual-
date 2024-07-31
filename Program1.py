# 1)Design, develop, code and run the program in any suitable language to solve the
# commission problem. Analyse it from the perspective of boundary value testing, derive
# different test cases, execute these test cases and discuss the test results.
# UNIT TESTING
def calculate_commission(fans, pumps, bodies):
 total_sales = (fans * 45) + (pumps * 30) + (bodies * 25)
 if total_sales <= 1000:
  commission = total_sales * 0.10
 elif total_sales <= 1800:
  commission = 1000 * 0.10 + (total_sales - 1000) * 0.15
 else:
  commission = 1000 * 0.10 + 800 * 0.15 + (total_sales - 1800) * 0.20
 return commission
# Test cases
test_cases = [
 {"fans": 1, "pumps": 1, "bodies": 1, "expected_commission": 10.0}, # minimum sales
 {"fans": 70, "pumps": 80, "bodies": 90, "expected_commission": 1260.0}, # maximum sales
 {"fans": 10, "pumps": 10, "bodies": 10, "expected_commission": 120.0}, # sales around $1000
 {"fans": 20, "pumps": 20, "bodies": 20, "expected_commission": 360.0}, # sales around $1800
 {"fans": 5, "pumps": 5, "bodies": 5, "expected_commission": 60.0}, # sales below $1000
 {"fans": 35, "pumps": 35, "bodies": 35, "expected_commission": 840.0}, # sales above $1800
 {"fans": 0, "pumps": 0, "bodies": 0, "expected_commission": 0.0}, # zero sales
]
for test_case in test_cases:
 fans = test_case["fans"]
 pumps = test_case["pumps"]
 bodies = test_case["bodies"]
 expected_commission = test_case["expected_commission"]
 commission = calculate_commission(fans, pumps, bodies)
 print(f"Test case: fans={fans}, pumps={pumps}, bodies={bodies}")

 print(f"Expected commission: ${expected_commission:.2f}")
 print(f"Actual commission: ${commission:.2f}")
 if commission == expected_commission:
  print("Test passed!")
 else:
  print("Test failed!")
 print()