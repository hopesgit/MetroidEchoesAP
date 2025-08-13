from BaseClasses import MultiWorld, ItemClassification
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or


class PathOfRoots_AboveCage(MetroidPrime2Region):
    name="Path of Roots"
    desc="Above Cage"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Middle)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Lagoon Side)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Great Bridge Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Grapple Beam", player),
                state.has("Screw Attack", player)
            ])
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self
            ),
        ]


class PathOfRoots_GreatBridgeLedge(MetroidPrime2Region):
    name="Path of Roots"
    desc="Great Bridge Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Beach)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Above Cage)",
            rule=lambda state, player: condition_or([
                state.has("Grapple Beam", player),
                state.has("Screw Attack", player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Middle)",
            rule=lambda state, player: True
        )
    ]


class PathOfRoots_LagoonSide(MetroidPrime2Region):
    name="Path of Roots"
    desc="Lagoon Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Beach)",
            door=DoorCover.Dark,
            rule=lambda state, player: state.has("Dark Beam", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Middle)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]


class PathOfRoots_Middle(MetroidPrime2Region):
    name="Path of Roots"
    desc="Middle"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Lagoon Side)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Great Bridge Ledge)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        )
    ]
