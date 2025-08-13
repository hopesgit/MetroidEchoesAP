from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _AbandonedWorksite(MetroidPrime2Region):
    name = "Abandoned Worksite"


class AbandonedWorksite_ForgottenBridgeEntrance(_AbandonedWorksite):
    desc="Forgotten Bridge Entrance"
    exits=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Pickup Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Forgotten Bridge Side)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has_all(["Space Jump Boots", "Screw Attack"], player)
            ])
        )
    ]


class AbandonedWorksite_GreatBridgeEntrance(_AbandonedWorksite):
    desc="Lower Great Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Scan Panel Ledge)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player), # either navigate the morph puzzle
                state.has("Grapple Beam", player) # or grapple from the floor to the ledge next to the morph tunnel
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Pickup Ledge)",
            rule=lambda state, player: state.has("Grapple Beam") # you can just grapple up there from the floor
        ),
    ]


class AbandonedWorksite_LedgeForgottenBridgeSide(_AbandonedWorksite):
    desc="Ledge Forgotten Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Forgotten Bridge Entrance)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has("Space Jump Boots", player),
                state.has("Screw Attack", player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Morph Ball Tunnel)",
            rule=lambda state, player: state.has("Morph Ball")
        )
    ]


class AbandonedWorksite_LedgeGreatBridgeSide(_AbandonedWorksite):
    desc="Ledge Great Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Pickup Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Grapple Beam", player),
                state.has_all(["Space Jump Boots", "Screw Attack"], player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | BSJ to Pickup Ledge"),
                    state.has_all(["Space Jump Boots", "Morph Ball", "Morph Ball Bomb"], player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | NSJ BSJ to Pickup Ledge"),
                    state.has_all(["Morph Ball", "Morph Ball Bomb"], player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | NSJ SA to Pickup Ledge"),
                    state.has("Screw Attack", player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | Boost Jump to Pickup Ledge"),
                    state.has_all(["Morph Ball", "Boost Ball"], player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | Roll Jump to Pickup Ledge"),
                    state.has_all(["Morph Ball", "Space Jump Boots"], player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Morph Ball Tunnel)",
            rule=lambda state, player: state.has("Morph Ball")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Great Bridge Entrance)",
            rule=lambda state, player: True
        )
    ]


class AbandonedWorksite_MorphBallTunnel(_AbandonedWorksite):
    desc="Morph Ball Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Forgotten Bridge Side)",
            rule=lambda state, player: True
        )
    ]


class AbandonedWorksite_PickupLedge(_AbandonedWorksite):
    desc="Pickup Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Great Bridge Entrance)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: condition_or([
                state.has("Grapple Beam", player),
                state.has_all(['Space Jump Boots', "Screw Attack"], player)
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
