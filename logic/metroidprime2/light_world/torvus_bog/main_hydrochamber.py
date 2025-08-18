from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_boost_ball, has_missile_count, \
    can_activate_dark_portal, can_use_screw_attack, can_use_charged_power_beam, can_use_spider_ball
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


def _spider_track_open(state, player) -> bool:
    condition_or([
        not state.has("Torvus Bog - Hydrochamber Storage | Item Collected", player),
        condition_and([
            state.has("Torvus Bog - Main Hydrochamber | Alpha Blogg Dead", player),
            state.has("Torvus Bog - Hydrochamber Storage | Item Collected", player)
        ])
    ])


class _MainHydrochamber(MetroidPrime2Region):
    name = "Main Hydrochamber"


class MainHydrochamber_Top(_MainHydrochamber):
    name="Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrochamber Shaft (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Main)",
            rule=lambda state, player: True
        ),
    ]


class MainHydrochamber_Main(_MainHydrochamber):
    name="Main"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Spider Track)",
            rule=lambda state, player: _spider_track_open(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Top)",
            # options: main (has grav boost, has beaten boss or didn't pick up item in storage)
            rule=lambda state, player: condition_or([
                # boss is dead
                condition_and([
                    _spider_track_open(state, player),
                    state.has("Gravity Boost", player),
                    condition_or([
                        state.has('Space Jump Boots', player), # vanilla strats
                        condition_and([ # instant unmorph strats
                            has_trick_enabled(state, player,
                                              "Torvus Bog - Main Hydrochamber | Climb to Top Post-Alpha Blogg (NSJ)"),
                            state.has('Morph Ball', player),
                        ])
                    ])
                ]),
                # sticky samus strats
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Main Hydrochamber | Climb Central Pillar (NSJ)"),
                    state.has("Gravity Boost", player),
                    not state.has("Torvus Bog - Hydrochamber Storage | Item Collected", player)
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Lower Door)",
            rule=lambda state, player: _spider_track_open(state, player)
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Alpha Blogg Dead",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Main Hydrochamber | Alpha Blogg Dead",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True, # todo: combat logic
                # the boss here is easier with the following items:
                # - Dark Beam w/ Charge
                # - Gravity Boost
                # - Space Jump Boots
                # - x E-tanks
                # - Screw Attack
                parent=self,
            ),
        ]


class MainHydrochamber_LowerDoor(_MainHydrochamber):
    name="Lower Door"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Lower Door)",
            rule=lambda state, player: _spider_track_open(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrochamber Storage",
            rule=lambda state, player: True
        ),
    ]


class MainHydrochamber_SpiderTrack(_MainHydrochamber):
    name="Spider Track"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Portal Ledge)",
            rule=lambda state, player: condition_or([
                can_use_spider_ball(state, player),
                condition_and([
                    can_lay_bomb(state, player),
                    state.has('Space Jump Boots', player),
                    has_trick_enabled(state, player, "Torvus Bog - Main Hydrochamber | BSJ to skip Spider Track")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Main)",
            rule=lambda state, player: _spider_track_open(state, player)
        ),
    ]


class MainHydrochamber_PortalLedge(_MainHydrochamber):
    name="Portal Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Undertemple (Portal Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Main)",
            rule=lambda state, player: _spider_track_open(state, player)
        ),
    ]
