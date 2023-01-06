"""This module provides unit tests for `Operator`."""

from electrolyzer.operator import Operator


# from electrolyzer.operator import Operator


def test_convert_ac_to_dc():

    """
    Should test formula to convert AC power source to DC power required for Electrolyzer

    """

    power_ac_in = 3.25e6  # [3.25MW as Watts]

    power_dc_plus, power_dc_minus = Operator.convert_ac_to_dc(power_ac_in)

    # estimate within a 5% tolerance
    tol = 0.05

    expected_dc_plus = 2702802.48769  # Watts
    expected_dc_minus = -21735984.30588  # Watts

    assert abs(power_dc_plus - expected_dc_plus) < abs(tol * power_dc_plus)
    assert abs(power_dc_minus - expected_dc_minus) < abs(tol * power_dc_minus)


def test_curtail_power():
    """TODO: This method is still being implemented."""
    pass
