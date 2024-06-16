
import math
def is_number(x):
  try:
    float(x)
    return True
  except ValueError:
    return False
def activation_function(x, activation_name):
  if not is_number(x):
    print("x must be a number")
    return
  x = float(x)
  if activation_name == "sigmoid":
    return 1 / (1 + math.exp(-x))
  elif activation_name == "relu":
    return max(0, x)
  elif activation_name == "elu":
    alpha = 0.01
    return x if x >= 0 else alpha * (math.exp(x) - 1)
  else:
    print(f"{activation_name} is not supported")
    return
x = input("Input x: ")
activation_name = input("Input activation Function (sigmoid, relu, elu): ")
result = activation_function(x, activation_name)
if result is not None:
  print(f"{activation_name}: f({x}) = {result: .2f}")