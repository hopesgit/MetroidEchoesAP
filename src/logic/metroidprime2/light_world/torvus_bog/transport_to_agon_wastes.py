from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_TransportToAgonWastes(MetroidPrime2Region):
    name="Transport to Agon Wastes"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.Seeker,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="E|Agon Wastes - Transport to Torvus Bog",
            rule=lambda state, player: state.has("Scan Visor", player)
        )
    ]
