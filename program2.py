def next_date(year, month, day):
    # Validate year
    if not (1 <= year <= 9999):
        raise ValueError("Invalid year")
    
    # Validate month
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    
    # Validate day
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    
    # Define days in each month
    days_in_month = [31, 28 + (1 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 0), 
                      31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if the day is valid for the given month
    if day > days_in_month[month - 1]:
        raise ValueError("Invalid day for the given month")
    
    # Compute next date
    if day < days_in_month[month - 1]:
        return year, month, day + 1
    elif month == 12:
        return year + 1, 1, 1
    else:
        return year, month + 1, 1

# Test cases
print("Valid dates:")
print(next_date(2022, 6, 15))  # Expected output: (2022, 6, 16)
print(next_date(2022, 6, 30))  # Expected output: (2022, 7, 1)
print(next_date(2022, 12, 31)) # Expected output: (2023, 1, 1)
print(next_date(2020, 2, 28))  # Expected output: (2020, 2, 29) (Leap year)
print(next_date(2019, 2, 28))  # Expected output: (2019, 3, 1) (Non-leap year)

print("\nInvalid dates:")
try:
    print(next_date(0, 6, 15))  # Expected output: Error
except ValueError as e:
    print(e)

try:
    print(next_date(2022, 13, 15))  # Expected output: Error
except ValueError as e:
    print(e)

try:
    print(next_date(2022, 6, 32))  # Expected output: Error
except ValueError as e:
    print(e)
