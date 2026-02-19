from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_TransportToSanctuaryFortress(MetroidPrime2Region):
    name="Transport to Sanctuary Fortress"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (North Ledge)",
            door = DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="E|Sanctuary Fortress - Transport to Torvus Bog",
            rule=lambda state, player: state.has('Scan Visor', player)
        )
    ]
