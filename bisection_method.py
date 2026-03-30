def square_root_bisection(number, tolerance=0.01, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    low = 0
    high = max(1,number)

    for i in range(max_iterations):
        root = (low+high)/2
        if abs(high - low) < tolerance:
            print(f"The square root of {number} is approximately {root}")
            return root
        
        if root*root < number:
            low = root
        else:
            high = root

    print(f"Failed to converge within {max_iterations} iterations")
    return None

print(square_root_bisection(1))
print(square_root_bisection(0))
print(square_root_bisection(81, 1e-3, 50))
print(square_root_bisection(225, 1e-7, 10))
print(square_root_bisection(9))
