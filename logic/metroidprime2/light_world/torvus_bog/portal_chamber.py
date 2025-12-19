from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import can_activate_dark_portal, can_lay_bomb, can_use_boost_ball, has_trick_enabled
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_PortalChamber_Center(MetroidPrime2Region):
    name="Portal Chamber"
    desc="Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Portal Chamber | Center",
            door=DoorCover.Dark, # do portals count as doors?
            rule=lambda state, player: can_activate_dark_portal(state, player)
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


class TorvusBog_PortalChamber_GreatBridgeSide(MetroidPrime2Region):
    name = "Portal Chamber"
    desc = "Great Bridge Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (North Path)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Morph Ball Tunnel)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Portal Chamber | Wall Boost")
                ])
            ])
        )
    ]


class TorvusBog_PortalChamber_MorphBallTunnel(MetroidPrime2Region):
    name = "Portal Chamber"
    desc = "Morph Ball Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Great Bridge Side)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Portal Chamber | Wall Boost")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Torvus Lagoon Side)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Portal Chamber | Wall Boost")
                ])
            ])
        )
    ]


class TorvusBog_PortalChamber_TorvusLagoonSide(MetroidPrime2Region):
    name="Portal Chamber"
    desc="Torvus Lagoon Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Morph Ball Tunnel)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    can_use_boost_ball(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Portal Chamber | Wall Boost")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Portal Chamber Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
