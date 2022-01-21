

def value_curve_farmer_1(discharge: float) -> float:
    if discharge > 10:
        return 60-discharge*4
    else:
        return 2*discharge

def value_curve_farmer_2(discharge: float) -> float:
    if discharge < 15:
        return discharge ** 1.8 / 3
    elif discharge >= 15 and discharge <= 30:
        return (30-discharge) ** 1.8 / 3
    else:
        return -30

class User:
    def __init__(self, value_curve):
        self.value_curve = value_curve

    def return_value(self, discharge):
        return self.value_curve(discharge)

class Control:
    pass


