def calculate_factorial(n):
  """Calculate the factorial of a given number n using a for loop."""
  factorial = 1
  for i in range(1, n + 1):
      factorial *= i
  return factorial

def main():
  print("Welcome to the Factorial Calculation program!")

  while True:
      try:
          number = int(input("Please enter a positive integer to calculate its factorial: "))
          if number < 0:
              print("The number must be a positive integer. Please try again.")
              continue
          break
      except ValueError:
          print("Invalid input. Please enter a positive integer.")

  result = calculate_factorial(number)
  print(f"The factorial of {number} is {result}.")

if __name__ == "__main__":
  main()