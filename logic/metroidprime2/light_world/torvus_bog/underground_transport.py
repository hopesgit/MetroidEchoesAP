from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal, \
    can_lay_bomb_or_pb, can_use_screw_attack, can_use_boost_ball, can_use_darkburst, can_use_sonic_boom
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _UndergroundTransport(MetroidPrime2Region):
    name="Underground Transport"


class UndergroundTransport_Upper(_UndergroundTransport):
    desc="Upper"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Shaft)",
            door=DoorCover.ScanVisor,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.Any,
            rule=lambda state, player: state.has("Torvus Bog - Torvus Temple (Pirates Dead)")
            # you MUST have this, or you get stuck in the doorway after the door is opened
        )
    ]


class UndergroundTransport_Shaft(_UndergroundTransport):
    desc="Shaft"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Upper)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Lower)",
            rule=lambda state, player: True
        ),
    ]


class UndergroundTransport_Lower(_UndergroundTransport):
    desc="Upper"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Shaft)",
            door=DoorCover.ScanVisor,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Above Water)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]
