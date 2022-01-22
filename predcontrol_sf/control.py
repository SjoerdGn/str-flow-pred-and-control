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


class User:
    def __init__(self, value_curve, method: str):
        self.value_curve = value_curve
        self.method = method

    def return_value(self, discharge: float) -> float:
        return self.value_curve(discharge)


class Control:
    def __init__(self, users: list):
        self.users = users
        pass

    def return_combined_value(self, discharges):
        value = 0
        for user, discharge in zip(self.users, discharges):
            value += user.return_value(discharge)
        return value


# every week the thing is put in place
