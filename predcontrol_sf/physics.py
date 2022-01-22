def rectangular_weir(h: float, b: float, g=9.80, cd=1) -> float:
    """Discharge over rectangular weir given a water level over weir and width of the weir

    Args:
        h (float): Water level over weir (in m)
        b (float): Width of the weir (in ms)
        g (float, optional): Gravitational acceleration in m/s^2. Defaults to 9.80 (for southern Australia).
        cd (float, optional): Friction coefficient. Defaults to 1.

    Returns:
        float: Discharge over weir
    """
    q = 2 / 3 * cd * b * (2 * g) ** 0.5 * h ** 1.5
    return q
