from .physics import rectangular_weir


def value_curve_farmer_1(discharge: float) -> float:
    """Returns the discharge - value curve of farmer 1

    Args:
        discharge (float): m^3/s water that is let into
                           farmer 1's property

    Returns:
        float: value (ficticious) of said discharge
    """
    if discharge > 10:
        return 60 - discharge * 4
    else:
        return 2 * discharge


def value_curve_farmer_2(discharge: float) -> float:
    """Returns the discharge - value curve of farmer 2

    Args:
        discharge (float): m^3/s water that is let into
                           farmer 2's property

    Returns:
        float: value (ficticious) of said discharge
    """
    if discharge < 15:
        return discharge ** 1.8 / 3
    elif discharge >= 15 and discharge <= 30:
        return (30 - discharge) ** 1.8 / 3
    else:
        return -30


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

    level_over_weir = level_river - level_weir
    discharge = rectangular_weir(level_over_weir, width_weir, g=g, cd=cd)
    return discharge