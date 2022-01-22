

class User:
    def __init__(self, value_curve, discharge_curve=None):
        self.value_curve = value_curve
        self.discharge_curve = discharge_curve
    
    def _calculate_discharge(self, ):
        # TODO
        pass

    def return_value(self, discharge: float, level: float) -> float:
        # TODO
        discharge = self._calculate_discharge()
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
