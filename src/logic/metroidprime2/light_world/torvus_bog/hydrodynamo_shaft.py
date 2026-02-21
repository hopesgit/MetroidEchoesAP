from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, can_activate_dark_portal, can_use_screw_attack
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class HydrodynamoShaft_Top(MetroidPrime2Region):
    name="Hydrodynamo Shaft"
    desc= "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Under Movable Base)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Stairs)",
            rule=lambda state, player: True
        )
    ]


class HydrodynamoShaft_Stairs(MetroidPrime2Region):
    name="Hydrodynamo Shaft"
    desc= "Stairs"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Top)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Main)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Portal Alcove)",
            rule=lambda state, player: condition_and([
                can_use_screw_attack(state, player),
                has_trick_enabled(state, player,
                                  "Torvus Bog - Hydrodynamo Shaft | Carry Air Underwater from Hydrodynamo Station")
            ])
        )
    ]


class HydrodynamoShaft_Main(MetroidPrime2Region):
    name="Hydrodynamo Shaft"
    desc= "Main"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Stairs)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Portal Alcove)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Bottom)",
            rule=lambda state, player: True
        )
    ]


class HydrodynamoShaft_PortalAlcove(MetroidPrime2Region):
    name="Hydrodynamo Shaft"
    desc= "Portal Alcove"
    exits_ = [
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Undertemple Access (Portal Alcove)",
            rule=lambda state, player: can_activate_dark_portal(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Main)",
            rule=lambda state, player: True
        )
    ]

class HydrodynamoShaft_Bottom(MetroidPrime2Region):
    name="Hydrodynamo Shaft"
    desc= "Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Main Hydrochamber (Door Ledge)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Main)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                can_lay_bomb(state, player),
                state.has("Space Jump Boots", player)
            ])
        )
    ]
