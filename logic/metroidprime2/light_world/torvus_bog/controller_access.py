from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_pb, can_lay_bomb, can_use_dark_beam, can_activate_dark_portal, \
    can_lay_bomb_or_pb, can_use_screw_attack, can_use_boost_ball, can_use_darkburst, can_use_sonic_boom
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


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
