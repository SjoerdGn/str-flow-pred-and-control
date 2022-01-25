import numpy as np
import neat


class User:
    def __init__(self, value_curve, discharge_curve=None):
        self.value_curve = value_curve
        self.discharge_curve = discharge_curve

    def _calculate_discharge(
        self, discharge: float, level_river: float, level_weir: float
    ) -> float:
        if self.discharge_curve is not None:
            discharge = self.discharge_curve(level_river, level_weir)
        return discharge

    def return_value(
        self, discharge: float, level_river: float, level_weir: float
    ) -> float:
        discharge = self._calculate_discharge(discharge, level_river, level_weir)
        return self.value_curve(discharge)


class Control:
    def __init__(self, users: list):
        self.users = users

    def return_combined_value(
        self, level_river, discharge_river, discharges_users, levels_weirs, penalty_func
    ):
        value = 0
        discharges_users_after = np.zeros(len(level_river))
        for user, discharge_user, level_weir in zip(
            self.users, discharges_users, levels_weirs
        ):
            value += user.return_value(discharge_user, level_river, level_weir)
            discharges_users_after += user._calculate_discharge(
                discharge_user, level_river, level_weir
            )

        penalties = penalty_func(discharge_river, discharges_users_after)
        value -= penalties
        return value

    def return_total_value(
        self, level_river, discharge_river, discharges_users, levels_weirs, penalty_func
    ):
        combined_value = self.return_combined_value(
            level_river, discharge_river, discharges_users, levels_weirs, penalty_func
        )
        return np.sum(combined_value)


class TrainedController:
    def __init__(self, genome, config):
        self.net = neat.nn.FeedForwardNetwork.create(genome, config)

    def output_raw(self, input):
        return self.net.activate(input)

    def output_def(
        self,
        input,
        index,
        translation_curve,
        out_min: float,
        out_max: float,
        in_min=-1.0,
        in_max=1.0,
    ):
        raw_output = self.output_raw(input)
        control_value = translation_curve(
            raw_output[index], out_min, out_max, in_min=in_min, in_max=in_max
        )
        return control_value
