from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_boost_ball, has_missile_count, \
    can_activate_dark_portal, can_use_screw_attack, can_use_charged_power_beam, can_use_spider_ball
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class CatacombsAccess_Catacombs_Side(MetroidPrime2Region):
    name="Catacombs Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Door Across From Portal)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (Hydrodynamo Station Side)",
            rule=lambda state, player: True
        )
    ]


class CatacombsAccess_HydrodynamoStation(MetroidPrime2Region):
    name="Hydrodynamo Station Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (East Door Ledge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (Catacombs Side)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Catacombs Access | Instant Unmorph DBJ")
                ])
            ])
        )
    ]
