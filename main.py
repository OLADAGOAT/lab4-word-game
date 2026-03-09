def fibonacci(n):
    """
    Recursively calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Test the recursive Fibonacci function
    print("Fibonacci sequence:")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
