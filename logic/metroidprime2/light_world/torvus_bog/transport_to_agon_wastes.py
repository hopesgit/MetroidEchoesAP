from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal, \
    can_lay_bomb_or_pb, can_use_screw_attack, can_use_boost_ball
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


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
