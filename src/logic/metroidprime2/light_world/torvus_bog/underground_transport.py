from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


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
