def safe_divide(numerator, denominator):
  """
  Performs division with error handling for division by zero and non-numeric inputs.

  Args:
      numerator: The numerator value.
      denominator: The denominator value.

  Returns:
      str: A message indicating successful division or an error message.
  """
  try:
    # Attempt to convert arguments to floats
    numerator = float(numerator)
    denominator = float(denominator)
  except ValueError:
    return "Error: Please enter numeric values only."

  try:
    # Perform division and return the result
    result = numerator / denominator
    return f"The result of the division is {result:.2f}"
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
