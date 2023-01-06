# run through the operator code
from electrolyzer.operator import Operator


power_ac_in = 3.25e6  # [3.25 MW as W]

power_dc_plus, power_dc_minus = Operator.convert_ac_to_dc(power_ac_in)

print("Power +:", power_dc_plus)

print("Power -:", power_dc_minus)
