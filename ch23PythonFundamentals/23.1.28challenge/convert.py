def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    
    if type(unit_in) is not str:
      return f"Invalid unit {unit_in}"
    elif type(unit_out) is not str:
      return f"Invalid unit {unit_out}"
    elif type(temp) is not int:
      return "Temp must be an integer!"
    if (unit_in == 'c' or unit_in == 'C') and (unit_out == 'f' or unit_out == 'F'):
      return (temp - 32) / 1.8
    elif (unit_in == 'f' or unit_in == 'F') and (unit_out == 'c' or unit_out == 'C'):
      return (temp * 1.8) + 32
    else: return "Invalid Inputs!"




print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

