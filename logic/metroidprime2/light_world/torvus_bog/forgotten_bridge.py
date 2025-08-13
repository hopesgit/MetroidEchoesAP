from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item

# regions:
# bridge
# cage
# cliffs
# dark portal ledge
# pickup ledge
# shallows

# this room depends on activating the bomb slot in the dark world for one of its states. I'll call that
#   "Dark Torvus Bog - Dark Forgotten Bridge | Bomb Slot Activated"
# another state is activated via the spinner in the cage area. I'll call that
#   "Torvus Bog - Forgotten Bridge | Spinner Activated"

class _ForgottenBridge(MetroidPrime2Region):
    name="Forgotten Bridge"


class ForgottenBridge_Bridge(_ForgottenBridge):
    desc="Bridge" # the bridge spins, so its access rules are a little complicated
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Pickup Ledge)",
            rule=lambda state, player: condition_or([
                state.has(state, player, "Dark Torvus Bog - Dark Forgotten Bridge | Bomb Slot Activated"),
                condition_and([
                    not state.has(state, player, "Dark Torvus Bog - Dark Forgotten Bridge | Bomb Slot Activated"),
                    state.has_all(["Space Jump Boots", "Screw Attack"], player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Dark Portal Ledge)",
            rule=lambda state, player: condition_or([
                not state.has(state, player, "Dark Torvus Bog - Dark Forgotten Bridge | Bomb Slot Activated"),
                condition_and([
                    state.has(state, player, "Dark Torvus Bog - Dark Forgotten Bridge | Bomb Slot Activated"),
                    state.has_all(["Space Jump Boots", "Screw Attack"], player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Forgotten Bridge | Spinner Activated)", player),
                state.has("Space Jump Boots", player)
            ])
        ),
    ]


class ForgottenBridge_Cage(_ForgottenBridge):
    desc="Cage" # this includes the path leading to two doors along with the mechanisms that lower after the spinner is used
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: state.has("Torvus Bog - Forgotten Bridge | Spinner Activated")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Forgotten Bridge | Spinner Activated"),
                state.has_all(["Space Jump Boots", "Screw Attack"], player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule=lambda state, player: state.has("Torvus Bog - Forgotten Bridge | Spinner Activated")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Grove Access",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Entrance)",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Spinner Activated",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Forgotten Bridge | Spinner Activated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has_all(["Morph Ball", "Boost Ball"], player),
                parent=self,
            ),
        ]


class ForgottenBridge_Cliffs(_ForgottenBridge):
    desc="Cliffs" # This includes the platforms rising from the water as well as the raised area leading to the phased bomb slot and bridge
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule = lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        )
    ]


class ForgottenBridge_DarkPortalLedge(_ForgottenBridge):
    desc="Dark Portal Ledge" # access rules change depending on whether the bomb slot was activated
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Dark Forgotten Bridge (Light Portal Ledge)",
            rule=lambda state, player: can_activate_dark_portal(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            rule=lambda state, player: condition_and([
                state.has("Torvus Bog - Forgotten Bridge | Spinner Activated"),
                state.has("Space Jump Boots")
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: condition_or([
                state.has("Dark Torvus Bog - Dark Forgotten Bridge | Bomb Slot Activated"),
                state.has("Space Jump Boots")
            ])
        )
    ]


class ForgottenBridge_PickupLedge(_ForgottenBridge):
    desc="Pickup Ledge" # access rules change depending on whether the bomb slot was activated
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Forgotten Bridge Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: condition_or([
                not state.has("Dark Torvus Bog - Dark Forgotten Bridge | Bomb Slot Activated"),
                state.has_all(["Space Jump Boots", "Screw Attack"], player)
            ])
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


class ForgottenBridge_Shallows(_ForgottenBridge):
    desc="Shallows"
    exits=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: state.has("Space Jump Boots")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Ruined Alcove",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
