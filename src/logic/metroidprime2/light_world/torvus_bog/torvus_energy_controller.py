from BaseClasses import MultiWorld, ItemClassification
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


class TorvusBog_TorvusEnergyController(MetroidPrime2Region):
    name="Torvus Energy Controller"
    exits_ = [
        MetroidPrime2Exit(
            destination="Controller Access",
            door=DoorCover.Any,
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Torvus Energy Returned",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Torvus Energy Controller | Energy Returned",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has("Dark Torvus Bog - Dark Torvus Energy Controller | Energy Recovered"),
                parent=self,
            ),
            MetroidPrime2Location(
                name="Pickup (Emerald Translator)",
                can_access=lambda state, player: True,
                parent=self
            )
        ]
