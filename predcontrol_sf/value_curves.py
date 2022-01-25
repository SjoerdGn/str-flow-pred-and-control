from .physics import rectangular_weir
from .data import (
    handle_float_or_array_like,
    check_non_negative_discharge,
    return_discharge,
)
import numpy as np


def value_curve_farmer_1(discharge: float) -> float:
    """Returns the discharge - value curve of farmer 1

    Args:
        discharge (float): m^3/s water that is let into
                           farmer 1's property

    Returns:
        float: value (ficticious) of said discharge
    """
    d = handle_float_or_array_like(discharge)
    check_non_negative_discharge(d)

    value = np.ones_like(d)
    value[d <= 10] = 2 * d[d <= 10]
    value[d > 10] = 35 - d[d > 10] * 1.5

    return return_discharge(discharge, value)


def value_curve_farmer_2(discharge: float) -> float:
    """Returns the discharge - value curve of farmer 2

    Args:
        discharge (float): m^3/s water that is let into
                           farmer 2's property

    Returns:
        float: value (ficticious) of said discharge
    """
    d = handle_float_or_array_like(discharge)
    check_non_negative_discharge(d)

    value = np.ones_like(d)
    value[d <= 15] = d[d <= 15] ** 1.5 / 3
    value[np.logical_and(d > 15, d <= 30)] = (
        30 - d[np.logical_and(d > 15, d <= 30)]
    ) ** 1.5 / 3
    value[d > 30] = -5
    return return_discharge(discharge, value)


def discharge_curve_farmer_1(
    level_river: float, level_weir: float, width_weir=2.0, cd=1.0, g=9.8
) -> float:
    """The discharge curve from the weir for farmer 1

    Args:
        level_river (float): Water level in the river in m (Aus)
        level_weir (float): Setting of the weir in m (Aus)
        width_weir (float, optional): Width of the weir in m. Defaults to 2.0.
        cd (float, optional): Weir coefficient. Defaults to 1.0.
        g (float, optional): Gravitational acceleration. Defaults to 9.8.

    Returns:
        float: discharge over weir
    """
    lr = handle_float_or_array_like(level_river)
    lw = handle_float_or_array_like(level_weir)

    level_over_weir = lr - lw
    discharge = rectangular_weir(level_over_weir, width_weir, g=g, cd=cd)
    discharge[np.iscomplex(discharge)] = 0.0
    discharge = discharge.real
    if type(lr) == int or float or len(discharge) == 1:
        discharge = discharge[0]
    return discharge


def translation_curve(
    input: float, out_min: float, out_max: float, in_min=-1.0, in_max=1.0
) -> float:
    """Translate from activation function to model input

    Args:
        input (float): Input from model
        out_min (float): Output (setting control) minimum value
        out_max (float): Output (setting control) maximum value
        in_min (float, optional): Activation function minimum. Defaults to -1.0.
        in_max (float, optional): Activation function maximum. Defaults to 1.0.

    Returns:
        float: optimal control value according to net
    """
    output = (input-in_min) / (in_max-in_min) * (out_max-out_min) + out_min
    return output


def penalty_curve_low_discharge(discharges_river, discharges_users):
    """Return penalties when discharge is low and too much intake from rivers

    Args:
        discharges_river (float or array like): Discharge(s) river
        discharges_users (float or array like): Discharge(s) taken from river

    Returns:
        numpy.array: Penalties from too much intake
    """
    dr = handle_float_or_array_like(discharges_river)
    du = handle_float_or_array_like(discharges_users)

    penalties = np.zeros_like(dr)
    penalties[np.logical_and(dr < 120, du > 14)] = 20
    if type(discharges_river) == int or float or len(penalties) == 1:
        penalties = penalties[0]
    return penalties
    
    # If discharge_river < 100:

