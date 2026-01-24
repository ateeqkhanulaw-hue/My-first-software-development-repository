def fibonacci_recursive(n):
    """
    Calculates Fibonacci number using RECURSION.
    
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    Each number is the sum of the two before it.
    """
    # BASE CASES - stops recursion
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # RECURSIVE CASE - function calls itself
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_loop(n):
    """Calculates Fibonacci using a loop (for comparison)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def display_sequence(count):
    """Displays Fibonacci sequence up to count numbers."""
    print(f"\nFirst {count} Fibonacci numbers:")
    for i in range(count):
        print(fibonacci_recursive(i), end=" ")
    print()


def main():
    """Main function."""
    print("\n=== FIBONACCI CALCULATOR ===")
    print("Using Recursion\n")
    
    while True:
        print("\n1. Calculate Fibonacci number")
        print("2. Display Fibonacci sequence")
        print("3. Compare recursive vs loop")
        print("4. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            try:
                n = int(input("Enter position (0-30): "))
                if n > 30:
                    print("Warning: Large numbers are slow with recursion!")
                result = fibonacci_recursive(n)
                print(f"Fibonacci({n}) = {result}")
            except ValueError:
                print("Enter a valid number.")
        
        elif choice == "2":
            try:
                count = int(input("How many numbers? (1-20): "))
                display_sequence(min(count, 20))
            except ValueError:
                print("Enter a valid number.")
        
        elif choice == "3":
            print("\n--- Comparison ---")
            for n in [5, 10, 15, 20]:
                rec_result = fibonacci_recursive(n)
                loop_result = fibonacci_loop(n)
                print(f"Fib({n}): Recursive={rec_result}, Loop={loop_result}")
        
        elif choice == "4":
            print("Goodbye! 👋")
            break
        
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()