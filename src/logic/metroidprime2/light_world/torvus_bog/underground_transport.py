from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class UndergroundTransport_Upper(MetroidPrime2Region):
    name="Underground Transport"
    desc="Upper"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Shaft)",
            rule=lambda state, player: state.has("Scan Visor", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.Any,
            rule=lambda state, player: state.has("Torvus Bog - Torvus Temple (Pirates Dead)", player)
            # you MUST have this, or you get stuck in the doorway after the door is opened
        )
    ]


class UndergroundTransport_Shaft(MetroidPrime2Region):
    name="Underground Transport"
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


class UndergroundTransport_Lower(MetroidPrime2Region):
    name="Underground Transport"
    desc="Upper"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Shaft)",
            rule=lambda state, player: state.has("Scan Visor", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]