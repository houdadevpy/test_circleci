print ("Hello World")
def check_fun():
  a = 5
  if a > 3:
    return True
  else:
    return False
def horrendous_function(x, y):
    """
    This function calculates the sum of two numbers,
    then multiplies the result by 2,
    then divides it by the product of the two numbers,
    then adds 10 to the final result.
    It's terribly convoluted and inefficient.
    """
    result = (x + y) * 2
    result /= x * y
    result += 10
    return result

test = check_fun()
