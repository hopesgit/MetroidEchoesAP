from .... import has_trick_enabled, can_lay_bomb
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and


class TempleTransportB(MetroidPrime2Region):
    name = "Temple Transport B"
    exits_ = [
        MetroidPrime2Exit(
            door=DoorCover.Opened,
            destination="E|Great Temple - Temple Transport B",
            rule=lambda state, player: state.has("Scan Visor", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Behind Translator Gate)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Temple Assembly Site (Cutscene)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Temple Grounds - Temple Transport B | OOB to Temple Assembly Site"),
                # expects that the player has never touched the trigger for the Temple Assembly Site dark splinter cutscene
                not state.has("Temple Grounds - Temple Assembly Site | Cutscene Watched", player),
                # expects the player to have bombs to execute a BSJ out of the elevator room
                can_lay_bomb(state, player),
                # expects the player to have SJ to get enough height to go out of the elevator room
                state.has("Space Jump Boots", player),
            ]),
        ),
    ]
