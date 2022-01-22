

class User:
    def __init__(self, value_curve, discharge_curve=None):
        self.value_curve = value_curve
        self.discharge_curve = discharge_curve
    
    def _calculate_discharge(self, discharge: float, level_river: float, level_weir: float) -> float:
        if self.discharge_curve is not None:
            discharge = self.discharge_curve(level_river, level_weir)
        return discharge

    def return_value(self, discharge: float, level_river: float, level_weir: float) -> float:
        discharge = self._calculate_discharge(discharge, level_river, level_weir)
        return self.value_curve(discharge)


class Control:
    def __init__(self, users: list):
        self.users = users
        pass

    def return_combined_value(self, level_river, discharges, levels_weirs):
        value = 0
        for user, discharge, level_weir in zip(self.users, discharges, levels_weirs):
            value += user.return_value(discharge, level_river, level_weir)
        return value


# every week the thing is put in place
