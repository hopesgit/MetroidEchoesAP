from .....Enums import DoorCover
from .....Regions import MetroidPrime2Region, MetroidPrime2Exit

class RuinedAlcove(MetroidPrime2Region):
    name = "Ruined Alcove"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Lagoon (Ruined Alcove Ledge)",
            door=DoorCover.Light,
            rule=lambda state, player: state.has("Light Beam")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Forgotten Bridge (Shallows)",
            door=DoorCover.Light,
            rule=lambda state, player: state.has("Light Beam")
        )
    ]
