"""
A room characterized by a large spinning bridge in the center of the room. It contains:
- One phased Bomb Slot
- One Spinner
- One caged area
- One Dark Portal
- One Super Missile Cover door
- One Missile Cover door
- One white door
- Grenchler or Dark Pirate Commando enemies

Logic assumes that the bomb slot in Dark Forgotten Bridge has already been activated.
"""

from BaseClasses import MultiWorld, ItemClassification
from ... import has_trick_enabled, can_lay_bomb, can_activate_dark_portal, can_use_screw_attack, can_use_boost_ball
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and


class ForgottenBridge_Bridge(MetroidPrime2Region):
    """The bridge. It rotates."""
    name="Forgotten Bridge"
    desc="Bridge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Pickup Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Dark Portal Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player, is_nsj=False)
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


class ForgottenBridge_Cage(MetroidPrime2Region):
    """A path between two side rooms that is not open to the rest of the room until a Spinner is used in this subregion.
    Also includes the platforms that lower after the Spinner has been operated."""
    name="Forgotten Bridge"
    desc="Cage"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: condition_or([
                state.has("Torvus Bog - Forgotten Bridge | Spinner Activated"),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Forgotten Bridge | BSJ into Cage"),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player)
                ])
            ])
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

        self.add_location(
            name="Spinner Activated",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Forgotten Bridge | Spinner Activated",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_use_boost_ball(state, player)
        )


class ForgottenBridge_Cliffs(MetroidPrime2Region):
    """Includes all the ledges leading up from the water to the phased bomb slot and bridge."""
    name="Forgotten Bridge"
    desc="Cliffs"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            rule = lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Bridge)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cage)",
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Torvus Bog - Forgotten Bridge | BSJ into Cage"),
                can_lay_bomb(state, player),
                state.has("Space Jump Boots", player)
            ])
        )
    ]


class ForgottenBridge_DarkPortalLedge(MetroidPrime2Region):
    name="Forgotten Bridge"
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
            rule=lambda state, player: state.has("Space Jump Boots", player)
        )
    ]


class ForgottenBridge_PickupLedge(MetroidPrime2Region):
    name="Forgotten Bridge"
    desc="Pickup Ledge"
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
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True,
        )


class ForgottenBridge_Shallows(MetroidPrime2Region):
    name="Forgotten Bridge"
    desc="Shallows"
    exits=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Cliffs)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots"),
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Forgotten Bridge | Bomb Jump Between Platforms")
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Forgotten Bridge | Air Underwater"),
                    state.has("Gravity Boost", player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Ruined Alcove",
            door=DoorCover.Light,
            rule=lambda state, player: True
        )
    ]
