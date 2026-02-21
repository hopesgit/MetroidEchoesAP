"""A room characterized by revolving platforms located above a small pool containing a Blogg enemy.
    The room's two doors normally lead to Transport to Sanctuary on the north side and Training Hall on the south side.
    Caution: A player may get stuck here if they fall into the water and lack any movement upgrades."""

from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_or
from ... import can_lay_bomb, can_use_screw_attack
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class FortressTransportAccess_AboveWater(MetroidPrime2Region):
    """The central area, containing the revolving platforms as well as the air above the water and between the ledges."""
    name="Fortress Transport Access"
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


class FortressTransportAccess_NorthLedge(MetroidPrime2Region):
    """The taller ledge containing the door that leads to the Torvus-Sanctuary elevator."""
    name="Fortress Transport Access"
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


class FortressTransportAccess_SouthLedge(MetroidPrime2Region):
    """The shorter ledge in the room. Has a yellow door that leads back to Training Chamber."""
    name="Fortress Transport Access"
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


class FortressTransportAccess_UnderWater(MetroidPrime2Region):
    """The central pool of water, including the steps that lead to the South Ledge.
    Contains a Blogg or Dark Blogg enemy.
    Can be difficult to leave without upgrades."""
    name="Fortress Transport Access"
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
