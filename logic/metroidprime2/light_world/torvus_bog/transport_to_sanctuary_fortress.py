from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, can_lay_pb, can_use_screw_attack
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item

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
