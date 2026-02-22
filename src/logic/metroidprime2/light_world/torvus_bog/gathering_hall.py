from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_or, condition_and
from ... import (
    has_trick_enabled,
    can_lay_pb,
    can_lay_bomb,
    can_activate_dark_portal,
    can_use_screw_attack,
    can_use_grapple_beam,
    can_use_dark_beam,
    can_activate_bomb_slot
)
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region


# solo bomb slot: lowers the gate locking off the portal
# paired bomb slots: removes barrier around item; extends platform from wall below item ledge
# spiny platforms don't stay flipped on room reload, so they aren't room state entities
# the spiny platforms can no longer be interacted with once the water is drained


class GatheringHall_UpperDoorLedge(MetroidPrime2Region):
    name="Gathering Hall"
    desc="Upper Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Access",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Laser Platform)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Item Ledge)",
            rule=lambda state, player: condition_and([
                can_use_screw_attack(state, player),
                state.has("Torvus Bog - Gathering Hall | Paired Bomb Slots Activated", player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Cannon Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (South Door Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Bottom)",
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Spider Tracks)",
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Torvus Bog - Gathering Hall | SA to Rotating Spider Track Segments"),
                can_use_screw_attack(state, player)
            ])
        )
    ]


class GatheringHall_CannonLedge(MetroidPrime2Region):
    name="Gathering Hall"
    desc="Cannon Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (South Door Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Laser Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Upper Door Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Bottom)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Item Ledge)",
            rule=lambda state, player: condition_and([
                condition_or([
                    state.has("Space Jump Boots", player),

                ]),
                state.has("Torvus Bog - Gathering Hall | Paired Bomb Slots Activated", player)
            ])
        )
    ]


class GatheringHall_ItemLedge(MetroidPrime2Region):
    name="Gathering Hall"
    desc="Item Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (South Door Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Laser Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Upper Door Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Cannon Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Bottom)",
            rule=lambda state, player: True
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Missile Expansion)",
            can_access=lambda state, player: True
        )


class GatheringHall_LaserLedge(MetroidPrime2Region):
    name="Gathering Hall"
    desc="Laser Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Cannon Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (South Door Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player),
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Bottom)",
            rule=lambda state, player: True,
        ),
    ]


class GatheringHall_NorthDoorLedge(MetroidPrime2Region):
    name="Gathering Hall"
    desc="North Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel West (South Entrance)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Cannon Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Laser Ledge)",
            rule=lambda state, player: condition_or([
                can_use_dark_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Bottom)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (South Door Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player),
        )
    ]


class GatheringHall_SouthDoorLedge(MetroidPrime2Region):
    name="Gathering Hall"
    desc="South Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South (West Entrance)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Cannon Ledge)",
            rule=lambda state, player: condition_or([
                can_use_grapple_beam(state, player),
                can_use_screw_attack(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Laser Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Bottom)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player),
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Solo Bomb Slot Activated",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Gathering Hall | Solo Bomb Slot Activated",
                classification=ItemClassification.progression,
                code=None,
                player=player
            ),
            can_access=lambda state, player: can_activate_bomb_slot(state, player, "Torvus Bog - Gathering Hall | Activate Bomb Slot without Bombs")
        )


class GatheringHall_Bottom(MetroidPrime2Region):
    name="Gathering Hall"
    desc="Bottom"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (North Door Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                state.has("Gravity Boost", player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Spider Tracks)",
            rule=lambda state, player: condition_and([
                state.has_all(["Boost Ball", "Spider Ball", "Morph Ball Bomb"], player),
                state.has("Torvus Bog - Gathering Hall | Water Drained")
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Portal Alcove)",
            rule=lambda state, player: state.has("Torvus Bog - Gathering Hall | Solo Bomb Slot Activated")
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Water Drained",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Gathering Hall | Water Drained",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_lay_pb(state, player, 2)
        )


class GatheringHall_PortalAlcove(MetroidPrime2Region):
    name="Gathering Hall"
    desc="Portal Alcove"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Bottom)",
            rule=lambda state, player: state.has("Torvus Bog - Gathering Hall | Solo Bomb Slot Activated")
        ),
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Crypt (Portal Alcove)",
            rule=lambda state, player: can_activate_dark_portal(state, player)
        )
    ]


class GatheringHall_SpiderTracks(MetroidPrime2Region):
    name="Gathering Hall"
    desc="Spider Tracks"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Hall (Bottom)",
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Paired Bomb Slots Activated",
            locked_item=MetroidPrime2Item(
                name="Torvus Bog - Gathering Hall | Paired Bomb Slots Activated",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: condition_or([
                condition_and([
                    can_lay_bomb(state, player),
                    state.has_all(["Spider Ball", "Boost Ball"], player),
                    can_lay_pb(state, player, 2)
                ]),
                condition_and([
                    state.has_all(["Morph Ball", "Space Jump Boots", "Screw Attack"], player),
                    has_trick_enabled(state, player, "Torvus Bog - Gathering Hall | SA to Rotating Spider Track Segments"),
                    can_activate_bomb_slot(state, player, "Torvus Bog - Gathering Hall | Activate Bomb Slot without Bombs")
                ])
            ])
        )
