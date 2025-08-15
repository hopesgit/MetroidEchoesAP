from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal, \
    can_lay_bomb_or_pb, can_use_screw_attack, can_use_boost_ball, can_use_darkburst, can_use_sonic_boom
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


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
            rule=lambda state, player: True
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
