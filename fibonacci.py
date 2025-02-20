def fibonacci(n):
  """Return the n-th Fibonacci number using recursion."""
  if n <= 0:
      raise ValueError("n must be a positive integer.")
  elif n == 1:
      return 0
  elif n == 2:
      return 1
  else:
      return fibonacci(n - 1) + fibonacci(n - 2)

def main():
  print(" Hello,welcome to the Fibonacci Sequence program!")

  while True:
      try:
          n = int(input("How many Fibonacci terms would you like to generate? "))
          if n <= 0:
              print("Please use a positive integer.")
              continue
          break
      except ValueError:
          print("Invalid input. Please enter a positive integer.")

  print(f"Generating the Fibonacci sequence up to the {n}-th term:")
  for i in range(1, n + 1):
      sequence = fibonacci(i)
      print(f"Term {i}: {sequence}")

if __name__ == "__main__":
  main()