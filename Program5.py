

def calculate_commission(sales_amount):
    """
    Calculate the commission earned by a salesperson based on their sales amount.
    
    Args:
        sales_amount (float): The sales amount.
        
    Returns:
        float: The commission earned.
    """
    if sales_amount <= 1000:
        commission_rate = 0.05
    elif 1001 <= sales_amount <= 5000:
        commission_rate = 0.07
    else:
        commission_rate = 0.10

    commission = sales_amount * commission_rate
    return commission

def main():
    sales_amount = float(input("Enter the sales amount: $"))
    commission = calculate_commission(sales_amount)
    print(f"The commission earned is: ${commission:.2f}")

if __name__ == "__main__":
    main()
