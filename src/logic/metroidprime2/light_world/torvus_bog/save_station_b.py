from BaseClasses import MultiWorld, ItemClassification
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_SaveStationB(MetroidPrime2Region):
    name="Save Station B"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
