def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    finally:
        print("Division operation completed")
    
    if y<0:
        raise ValueError("negative input not allowed")

print(divide(4,0))




