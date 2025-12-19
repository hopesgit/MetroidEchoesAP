from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, can_use_screw_attack, can_use_darkburst, can_use_sunburst, \
    can_use_sonic_boom, can_use_boost_ball, can_use_spider_ball
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _TrainingChamber(MetroidPrime2Region):
    name="Training Chamber"


class TrainingChamber_WestCagedArea(_TrainingChamber):
    desc="West Caged Area"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West (North Side)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Center)",
            rule=lambda state, player: state.has('Gravity Boost', player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Statue Platform)",
            rule = lambda state, player: condition_and([ # you can stand on the open section of gate and triple jump to the statue platform
                state.has('Gravity Boost', player),
                can_use_screw_attack(state, player)
            ])
        )
    ]


class TrainingChamber_EastCagedArea(_TrainingChamber):
    desc="East Caged Area"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East (North Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Center)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Statue Platform)",
            rule = lambda state, player: condition_and([ # you can stand on the open section of gate and triple jump to the statue platform
                state.has('Gravity Boost', player),
                can_use_screw_attack(state, player)
            ])
        )
    ]


class TrainingChamber_Center(_TrainingChamber):
    # When it comes to the rotating tunnel, I'm not sure how to account for it. If its position can be tracked, that would be helpful.
    # Otherwise, I intend to treat it as:
    # - East and West Caged Areas can only connect to the center via Gravity Boost
    # - The Center can connect outward using the spinner mechanism, but only after the Bloggs are dead
    desc="Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (West Gated Area)",
            rule=lambda state, player: condition_and([
                state.has('Gravity Boost', player),
                state.has('Torvus Bog - Training Chamber | Bloggs Dead')
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (East Gated Area)",
            rule=lambda state, player: condition_and([
                state.has('Gravity Boost', player),
                state.has('Torvus Bog - Training Chamber | Bloggs Dead', player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Ledge Below South Door)",
            rule=lambda state, player: condition_or([
                state.has('Gravity Boost', player),
                state.has('Morph Ball', player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Behind Statue)",
            rule=lambda state, player: state.has("Torvus Bog - Training Chamber | Statue Moved", player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Bloggs Dead",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Training Chamber | Bloggs Dead",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: True,
                parent=self,
            ),
        ]


class TrainingChamber_StatuePlatform(_TrainingChamber):
    desc="Statue Platform"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Center)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (East Gated Area)",
            rule=lambda state, player: state.has_any(['Space Jump', 'Gravity Boost'], player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (West Gated Area)",
            rule=lambda state, player: state.has_any(['Space Jump', 'Gravity Boost'], player)
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Statue Moved",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Training Chamber | Statue Moved",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Torvus Bog - Training Chamber | Activate Bomb Slot without Bombs"),
                        condition_or([
                            can_use_darkburst(state, player),
                            can_use_sunburst(state, player),
                            can_use_sonic_boom(state, player),
                        ]),
                        state.has("Morph Ball", player)
                    ])
                ]),
                parent=self,
            ),
        ]


class TrainingChamber_SouthDoorLedge(_TrainingChamber):
    desc="South Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Ledge Below South Door)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Access",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Access (Statue Platform)",
            rule=lambda state, player: condition_and([
                state.has_all(['Space Jump Boots', 'Scan Visor'], player),
                has_trick_enabled(state, player, "Torvus Bog - Training Chamber | Extended Dash to Bomb Slot")
            ])
        )
    ]


class TrainingChamber_LedgeBelowSouthDoor(_TrainingChamber):
    desc="Ledge Below South Door"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Center)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Statue Platform)",
            rule=lambda state, player: condition_or([
                can_use_screw_attack(state, player),
                condition_and([

                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (South Door Ledge)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has('Space Jump Boots', player),
                state.has('Gravity Boost', player)
            ])
        )
    ]


class TrainingChamber_BehindStatue(_TrainingChamber):
    desc="Behind Statue"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (North Door Ledge)",
            rule=lambda state, player: can_use_spider_ball(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Center)",
            rule=lambda state, player: state.has('Torvus Bog - Training Chamber | Statue Moved')
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: state.has("Torvus Bog - Training Chamber | Statue Moved"),
                parent=self
            ),
        ]


class TrainingChamber_NorthDoorLedge(_TrainingChamber):
    desc="North Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (South Ledge)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Behind Statue)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Center)",
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Training Chamber | Bypass Statue with SJ"),
                    state.has('Space Jump Boots', player)
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Training Chamber | Bypass Statue with Boost"),
                    can_use_boost_ball(state, player),
                    can_use_spider_ball(state, player)
                ])
            ])
        )
    ]


class TrainingChamber_SpiderTracks(_TrainingChamber):
    desc="Spider Tracks"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Statue Platform)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (Center)",
            rule=lambda state, player: True
        )
    ]
