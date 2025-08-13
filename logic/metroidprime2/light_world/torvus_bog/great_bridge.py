from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _GreatBridge(MetroidPrime2Region):
    name = "Great Bridge"


class GreatBridge_BehindTranslatorGate(_GreatBridge):
    desc = "Behind Translator Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Map Station",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Cannon Ledge)",
            door=DoorCover.EmeraldTranslator,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Scan Visor", player),
                    state.has("Emerald Translator", player)
                ]),
                state.has("Space Jump Boots", player)
            ])
        )
    ]


class GreatBridge_Beach(_GreatBridge):
    desc = "Beach"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (North Path)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                state.has("Screw Attack", player),
                condition_and([
                    state.has("Morph Ball"),
                    state.has("Boost Ball"),
                    has_trick_enabled(state, player, "Torvus Bog - Great Bridge | Wall Boost to North Path")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Cannon Ledge)",
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                state.has("Screw Attack", player)
            ])
        )
    ]


class GreatBridge_Bridge(_GreatBridge):
    desc="Bridge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Access (Upper Great Bridge Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Cannon Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (North Path)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Beach)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Morph Ball Tunnel)",
            rule=lambda state, player: can_lay_pb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Scan Panel Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump",  player),
                state.has("Screw Attack", player)
            ])
        )
    ]


class GreatBridge_CannonLedge(_GreatBridge):
    desc="Cannon Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Beach)",
            rule = lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Behind Translator Gate)",
            door=DoorCover.EmeraldTranslator,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Torvus Bog - Great Bridge | Slope Jump over Translator Gate")
                ]),
                condition_and([
                    state.has("Scan Visor", player),
                    state.has("Emerald Translator", player) #check translator
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Bridge)",
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Torvus Bog - Great Bridge | Cannon Activated", player),
                    state.has("Morph Ball", player)
                ]),
                condition_and([
                    state.has("Space Jump Boots", player),
                    has_trick_enabled(state, player, "Torvus Bog - Great Bridge | Slope Jump over Translator Gate"),
                    has_trick_enabled(state, player, "Torvus Bog - Great Bridge | Scan Dash across Top")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Scan Panel Ledge)",
            rule=lambda state, player: state.has("Screw Attack", player)
        )
    ]

class GreatBridge_MorphBallTunnel(_GreatBridge):
    desc="Morph Ball Tunnel"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Scan Panel Ledge)",
            rule=lambda state, player: can_lay_pb(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Bridge)",
            rule=lambda state, player: can_lay_pb(state, player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Power Bomb Expansion)",
                can_access=lambda state, player: True,
                parent=self
            ),
        ]


class GreatBridge_NorthPath(_GreatBridge):
    desc="North Path"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Portal Chamber (Great Bridge Side)",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Temple Access (Lower Great Bridge Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Beach)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Cannon Ledge)",
            rule=lambda state, player: condition_or([
                state.has('Space Jump Boots', player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Great Bridge | Instant Unmorph to Cannon Ledge"),
                    can_lay_bomb(state, player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Scan Panel Ledge)",
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Torvus Bog - Great Bridge | Instant Unmorph to Scan Panel Ledge"),
                can_lay_bomb(state, player)
            ])
        )
    ]


class GreatBridge_ScanPanelLedge(_GreatBridge):
    desc="Scan Panel Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Abandoned Worksite (Great Bridge Entrance)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (North Path)",
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Bridge)",
            rule=lambda state, player: state.has_all(["Space Jump Boots", "Screw Attack"], player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Great Bridge (Morph Ball Tunnel)",
            rule=lambda state, player: can_lay_pb(state, player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Cannon Activated",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Great Bridge | Cannon Activated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            ),
        ]
