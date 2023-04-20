from dino_runner.utils.constants import HELLI_ICON, HELLI_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Helly(PowerUp):
    def __init__(self):
        self.image = HELLI_ICON
        self.type = HELLI_TYPE
        super().__init__(self.image, self.type)
