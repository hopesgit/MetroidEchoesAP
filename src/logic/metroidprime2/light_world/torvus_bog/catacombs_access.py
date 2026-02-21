from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_CatacombsAccess_CatacombsSide(MetroidPrime2Region):
    name="Catacombs Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Door Across From Portal)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (Hydrodynamo Station Side)",
            rule=lambda state, player: True
        )
    ]


class TorvusBog_CatacombsAccess_HydrodynamoStationSide(MetroidPrime2Region):
    name="Hydrodynamo Station Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (East Door Ledge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (Catacombs Side)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    can_lay_bomb(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Catacombs Access | Instant Unmorph DBJ")
                ])
            ])
        )
    ]
