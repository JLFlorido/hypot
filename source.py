# Requirements

# 2 inputs, positive, integers or float (is it digit?)
# 1 output, float
# external library? No external libraries
# Create a function - calcalte hypot = sqrt(a^2 + b^2)
' Create a square root function
def take_inputs()
  # Lines asking for inputs
  # Lines checking the input is digit, else returning error
  return a, b
  
def hypotenuse(a,b)
  return sqrt(a^2 + b^2)

if __name__ == "__main__":
  a, b = take_inputs()
  hypot = hypotenuse(a,b)
  print(f"The resulting hypotenuse is {hypot}")
