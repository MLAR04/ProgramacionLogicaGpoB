def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        return memo[n]

# Ejemplo de uso
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci de ({n}) = {fibonacci_memo(n)}")
