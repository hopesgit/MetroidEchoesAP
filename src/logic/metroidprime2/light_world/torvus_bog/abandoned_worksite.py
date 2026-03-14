from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, can_use_screw_attack, can_use_grapple_beam, can_use_boost_ball, \
    can_boost_jump
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class AbandonedWorksite_ForgottenBridgeEntrance(MetroidPrime2Region):
    name = "Abandoned Worksite"
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
                # TODO: replace with can_ball_jump
                can_lay_bomb(state, player),
                can_use_screw_attack(state, player)
            ])
        )
    ]


class AbandonedWorksite_GreatBridgeEntrance(MetroidPrime2Region):
    name = "Abandoned Worksite"
    desc="Great Bridge Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Scan Panel Ledge)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: condition_or([
                # TODO: replace with can_ball_jump
                can_lay_bomb(state, player), # either navigate the morph puzzle
                can_use_grapple_beam(state, player) # or grapple from the floor to the ledge next to the morph tunnel
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Pickup Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Grapple Beam", player), # you can just grapple up there from the floor
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | BSJ to Pickup Ledge"),
                    state.has_all(["Space Jump Boots", "Morph Ball", "Morph Ball Bomb"], player)
                ]),
            ])
        )
    ]


class AbandonedWorksite_LedgeForgottenBridgeSide(MetroidPrime2Region):
    name = "Abandoned Worksite"
    desc="Ledge Forgotten Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Forgotten Bridge Entrance)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has("Space Jump Boots", player),
                can_use_screw_attack(state, player, is_nsj=True)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: state.has("Morph Ball", player)
        )
    ]


class AbandonedWorksite_LedgeGreatBridgeSide(MetroidPrime2Region):
    name = "Abandoned Worksite"
    desc="Ledge Great Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Pickup Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | NSJ BSJ to Pickup Ledge"),
                    state.has_all(["Morph Ball", "Morph Ball Bomb"], player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | NSJ SA to Pickup Ledge"),
                    can_use_screw_attack(state, player, is_nsj=True)
                ]),
                can_boost_jump(state, player, "Torvus Bog - Abandoned Worksite | Boost Jump to Pickup Ledge"),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Abandoned Worksite | Roll Jump to Pickup Ledge"),
                    state.has_all(["Morph Ball", "Space Jump Boots"], player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Forgotten Bridge Side)",
            rule=lambda state, player: state.has("Morph Ball")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Great Bridge Entrance)",
            rule=lambda state, player: True
        )
    ]


class AbandonedWorksite_PickupLedge(MetroidPrime2Region):
    name = "Abandoned Worksite"
    desc="Pickup Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Great Bridge Entrance)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Ledge Great Bridge Side)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True
        )
