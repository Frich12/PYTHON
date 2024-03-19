def fibonacci_sequence(n):
    sequence =[0,1]
    if n<=2:
        return sequence[:n]
    for _ in range(2,n):
        next_term = sequence[-1]+ sequence[-2]
        sequence.append(next_term)
        return sequence
    

def main():
    n=int(input("Enter the number of terms for the fibonacci sequence:"))
    if n<= 0:
        print("Invalid input. Please enter a positive integer.")
        return
    fibonacci =fibonacci_sequence
    print("Fibonacci sequence:",fibonacci)

if __name__ == "__main__":
    main()