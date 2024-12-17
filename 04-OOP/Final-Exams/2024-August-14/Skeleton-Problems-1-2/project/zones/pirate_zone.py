from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):

    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    @staticmethod
    def zone_type():
        return "Pirate"
