from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal, \
    can_use_boost_ball, can_use_spider_ball, can_use_screw_attack
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item

#regions:
# - entrance
# - half-pipe
# - spider track
# - spider challenge
# - cannon ledge
# - item ledge

# tricks:
# "Torvus Bog - Torvus Plaza | STE SA to Item",
# "Torvus Bog - Torvus Plaza | Boost-only/Cannonball",
# "Torvus Bog - Torvus Plaza | BSJ to Entrance",


class _TorvusPlaza(MetroidPrime2Region):
    name="Torvus Plaza"


class TorvusPlaza_Entrance(_TorvusPlaza):
    desc="Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Half-Pipe)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Spider Track)",
            rule=lambda state, player: condition_or([
                # normal conditions
                state.has_all(["Morph Ball", "Spider Ball", "Boost Ball"], player),
                # using SA
                condition_and([
                    state.has_all(["Space Jump Boots", "Screw Attack"], player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | STE SA to Item")
                ]),
                # using Boost
                condition_and([
                    state.has_all(["Morph Ball", "Boost Ball"], player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | Boost-only/Cannonball")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Plaza Access (Torvus Plaza Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
    ]


class TorvusPlaza_HalfPipe(_TorvusPlaza):
    desc = "Half-Pipe"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Entrance)",
            rule=lambda state, player: condition_or([
                can_use_boost_ball(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | Instant Unmorph BSJ to Entrance"),
                    can_lay_bomb(state, player)
                ]),
                can_use_screw_attack(state, player) # you can screw from the back of the room to the middle of the entrance ledge easily
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Plaza (Spider Track)",
            rule = lambda state, player: condition_and([
                can_use_boost_ball(state, player),
                condition_or([
                    state.has("Spider Ball", player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | Boost-only/Cannonball")
                ])
            ])
        )
    ]


class TorvusPlaza_SpiderTrack(_TorvusPlaza):
    desc="Spider Track" # this includes the standable tree area near the back of the room.
    # It's the beginning of the track, ending just before the Sporb
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Half-Pipe)",
            rule=lambda state, player: True #you can simply just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Spider Challenge)",
            rule=lambda state, player: condition_or([
                condition_and([
                    can_lay_bomb(state, player),
                    can_use_spider_ball(state, player)
                    # boost makes it easier but isn't required for the expected path
                ]),
                condition_and([
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | STE SA to Item")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Item Ledge)",
            rule=lambda state, player: condition_and([
                #boost-only requires BSJ
                has_trick_enabled(state, player, "Torvus Bog - Torvus Plaza | Boost-only/Cannonball"),
                can_lay_bomb(state, player),
                state.has("Space Jump Boots", player)
            ])
        )
    ]

class TorvusPlaza_SpiderChallenge(_TorvusPlaza):
    desc="Spider Challenge" # this includes the more difficult parts of the track, from the sporb area to the cannon ledge
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Entrance)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Half-Pipe)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Spider Track)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Cannon Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Item Ledge)",
            rule=lambda state, player: condition_or([
                can_use_screw_attack(state, player),
                can_use_spider_ball(state, player)
            ])
        ),
    ]


class TorvusPlaza_CannonLedge(_TorvusPlaza):
    desc="Cannon Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Entrance)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Half-Pipe)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Item Ledge)",
            rule=lambda state, player: True  # the cannon is already activated
        ),
    ]


class TorvusPlaza_ItemLedge(_TorvusPlaza):
    desc="Item Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Arena (Half-Pipe)",
            rule=lambda state, player: True
        ),
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
