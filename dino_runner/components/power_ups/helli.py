from dino_runner.utils.constants import HELLI_TYPE, DINO_HELLI_ICON
from dino_runner.components.power_ups.power_up import PowerUp


class Helli(PowerUp):
    def __init__(self):
        self.image = DINO_HELLI_ICON
        self.type = HELLI_TYPE
        super().__init__(self.image, self.type)