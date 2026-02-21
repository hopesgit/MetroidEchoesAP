from BaseClasses import MultiWorld, ItemClassification
from ... import can_use_screw_attack
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class MeditationVista_Entrance(MetroidPrime2Region):
    name = "Meditation Vista"
    desc = "Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Grove (Center)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Gloom Vista",
            rule=lambda state, player: state.has("Scan Visor", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Meditation Vista (Floating Platform)",
            door=DoorCover.Any,
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
    ]


class MeditationVista_FloatingPlatform(MetroidPrime2Region):
    name="Meditation Vista"
    desc="Floating Platform"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Meditation Vista (Entrance)",
            rule=lambda state, player: True
        )
    ]


    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Energy Tank)",
                can_access=lambda state, player: state.has("Morph Ball", player),
                parent=self
            )
        ]
