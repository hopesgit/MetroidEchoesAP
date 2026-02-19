from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_or, condition_and
from ... import can_lay_bomb,can_use_darkburst, can_use_sonic_boom

from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_ControllerAccess(MetroidPrime2Region):
    name="Controller Access"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Upper)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_and([
                        can_use_darkburst(state, player),
                        can_use_sonic_boom(state, player)
                        # I couldn't get it to work with lightburst, but it probably does
                        # doesn't work with power bombs
                        # I couldn't get screw attack to get me lodged in the slot either
                    ])
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Energy Controller",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    state.has("Morph Ball", player),
                    condition_and([
                        can_use_darkburst(state, player),
                        can_use_sonic_boom(state, player)
                        # same as above
                    ])
                ])
            ])
        )
    ]
