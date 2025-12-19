from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, can_lay_pb, can_use_screw_attack
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


class _FortressTransportAccess(MetroidPrime2Region):
    """A room characterized by revolving platforms located above a small pool containing a Blogg enemy.
    The room's two doors normally lead to Transport to Sanctuary on the north side and Training Hall on the south side.
    Caution: A player may get stuck here if they fall into the water and lack any movement upgrades."""
    name="Fortress Transport Access"


class TorvusBog_FortressTransportAccess_AboveWater(_FortressTransportAccess):
    """The central area, containing the revolving platforms as well as the air above the water and between the ledges."""
    desc = "Above Water"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Under Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (North Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (North Ledge)",
            rule=lambda state, player: True
        )
    ]


class TorvusBog_FortressTransportAccess_NorthLedge(_FortressTransportAccess):
    """The taller ledge containing the door that leads to the Torvus-Sanctuary elevator."""
    desc = "North Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transport to Sanctuary Fortress",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West (Under Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]


class TorvusBog_FortressTransportAccess_SouthLedge(_FortressTransportAccess):
    """The shorter ledge in the room. Has a yellow door that leads back to Training Chamber."""
    desc="South Ledge"
    exits_=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Chamber (North Door Ledge)",
            door=DoorCover.PowerBomb,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Under Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Above Water)",
            rule=lambda state, player: True #but it's easier to cross the platforms with space jump or screw
        ),
    ]


class TorvusBog_FortressTransportAccess_UnderWater(_FortressTransportAccess):
    """The central pool of water, including the steps that lead to the South Ledge.
    Contains a Blogg or Dark Blogg enemy.
    Can be difficult to leave without upgrades."""
    desc = "Under Water"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (South Ledge)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has('Space Jump Boots', player),
                state.has('Gravity Boost', player),
                can_use_screw_attack(state, player) # this method requires some finicky movement in NSJ, but you can do it
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Fortress Transport Access (Above Water)",
            rule=lambda state, player: condition_or([
                state.has('Gravity Boost', player),
                state.has('Space Jump Boots', player),
                can_use_screw_attack(state, player) # this method requires some finicky movement in NSJ, but you can do it
            ])
        )
    ]
