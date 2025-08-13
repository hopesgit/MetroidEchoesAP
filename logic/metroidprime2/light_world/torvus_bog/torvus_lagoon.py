from BaseClasses import MultiWorld, ItemClassification

from ... import has_trick_enabled, can_use_screw_attack
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class TorvusLagoon_Beach(MetroidPrime2Region):
    name = "Torvus Lagoon"
    desc = "Beach"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Save Room Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                state.has("Screw Attack", player),
                has_trick_enabled(state, player, "Torvus Bog - Torvus Lagoon | NSJ to Save Room Ledge")
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Bridge)",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Torvus Lagoon | Gates Lowered"),
                condition_or([
                    state.has("Space Jump Boots", player),
                    state.has("Screw Attack", player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Lagoon | NSJ to Bridge")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Path of Roots (Underwater)",
            door=DoorCover.Dark,
            rule=lambda state, player: state.has("Dark Beam", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Underwater Ledge)",
            rule=lambda state, player: condition_or([
                state.has('Gravity Boost', player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Lagoon | Air Underwater"),
                    can_use_screw_attack(state, player)
                ])
            ])
        )
    ]


class TorvusLagoon_SaveRoomLedge(MetroidPrime2Region):
    name = "Torvus Lagoon"
    desc = "Save Room Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Save Station A",
            door=DoorCover.Missile,
            rule=lambda state, player: state.has("Missile Launcher", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Beach)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Lagoon - Bridge",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Torvus Lagoon | Gates Lowered"),
                condition_or([
                    state.has("Space Jump Boots", player),
                    state.has("Screw Attack", player)
                ])
            ])
        )
    ]

class TorvusLagoon_UnderwaterLedge(MetroidPrime2Region):
    name= "Torvus Lagoon"
    desc= "Underwater Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Beach",
            rule = lambda state, player: True
        )
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

class TorvusLagoon_Bridge(MetroidPrime2Region):
    name = "Torvus Lagoon"
    desc = "Bridge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Portal Chamber Ledge)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Lagoon | Bridge Lowered")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Ruined Alcove Ledge)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Lagoon | Bridge Lowered")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Beach)",
            rule=lambda state, player: True
        )
    ]

class TorvusLagoon_PortalChamberLedge(MetroidPrime2Region):
    name = "Torvus Lagoon"
    desc = "Portal Chamber Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Torvus Lagoon Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Bridge)",
            rule=lambda state, player: state.has("Scan Visor", player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Torvus Bog - Torvus Lagoon | Gates Lowered",
                can_access=lambda state, player: state.has("Scan Visor", player),
                locked_item= MetroidPrime2Item(
                    name="Torvus Bog - Torvus Lagoon | Gates Lowered",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player
                ),
                parent=self
            ),
        ]


class TorvusLagoon_RuinedAlcoveLedge(MetroidPrime2Region):
    name = "Torvus Lagoon"
    desc = "Ruined Alcove Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Bridge)",
            rule=lambda state, player: state.has("Torvus Bog - Torvus Lagoon | Gates Lowered")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Ruined Alcove",
            door=DoorCover.Dark,
            rule=lambda state, player: state.has("Dark Beam", player)
        )
    ]
