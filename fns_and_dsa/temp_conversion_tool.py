FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  """Converts a temperature in Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit.

  Returns:
      The temperature  
 converted to Celsius.
  """
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """Converts a temperature in Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius.

  Returns:
      The temperature converted to Fahrenheit.
  """
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  """Prompts the user for temperature conversion and displays the result."""
  while True:
    try:
      # Get user input for temperature and unit
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      if unit not in ("C", "F"):
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

      # Call appropriate conversion function based on unit
      if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        converted_unit = "F"
      else:
        converted_temp = convert_to_celsius(temperature)
        converted_unit = "C"

      # Display the converted temperature
      print(f"{temperature:.1f}°{unit} is {converted_temp:.1f}°{converted_unit}")
      break

    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
