from BaseClasses import MultiWorld, ItemClassification
from src.Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, has_missile_count, hydrodynamo_station_has_scanned_panels, underwater_movement
from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region

# tricks in this room:
# "Torvus Bog - Hydrodynamo Station | Boost Jump"
# - Cross gaps using the speed and momentum of a boost ball while underwater. Requires good unmorph timing to get an instant unmorph.
# - https://youtu.be/7I2Jl824CMI

# "Torvus Bog - Hydrodynamo Station | Underwater Dash"
# - Dash while entering the water, preserving your momentum by taking advantage of the underwater physics.
# - https://youtu.be/IUcPDkHKd0I
# - https://youtu.be/nY4U_0Uyn0M

# "Torvus Bog - Hydrodynamo Station | Air Underwater"
# - Trick the game into thinking you are not in the water when you are. This allows for standard movement.
# - You can activate Air Underwater by causing a camera transition while entering the water. This is almost always done by morphing.
# - https://youtu.be/g7DeBeDMpeU

# "Torvus Bog - Hydrodynamo Station | Seeker Skip"
# - Break the Seeker locks using Missiles and Screw Attack.
# - Requires Air Underwater since you can't Screw Attack underwater normally.
# - https://youtu.be/ALjnm411Ldk

class HydrodynamoStation_AboveWater(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc="Above Water"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Underground Transport (Lower)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: True
        ),
    ]


class HydrodynamoStation_Top(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc = "Top"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top Door Ledge)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: True
        ),
    ]


class HydrodynamoStation_TopDoorLedge(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc = "Top Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Save Station B",
            door=DoorCover.Missile,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top)",
            rule=lambda state, player: state.has("Space Jump Boots", player)
        ),
    ]


class HydrodynamoStation_ThreeDoors(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc = "Three Doors"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Door Ledge)",
            rule=lambda state, player: condition_or([
                    state.has("Gravity Boost", player),
                    condition_and([
                        state.has("Torvus Bog - Hydrodynamo Station | Scanned North Panel", player),
                        condition_or([
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player)
                    ]),
                ])
            ])
        ), # summary: if you have gravity boost, you're fine. If you have scanned the panel and can either DBJ or
             # have SJB, you're fine
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (West Door Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Torvus Bog - Hydrodynamo Station | Scanned West Panel", player),
                    condition_or([
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player)
                    ]),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (East Door Ledge)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                condition_and([
                    state.has("Torvus Bog - Hydrodynamo Station | Scanned East Panel", player),
                    condition_or([
                        can_lay_bomb(state, player),
                        state.has("Space Jump Boots", player)
                    ]),
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Cannon)",
            rule=lambda state, player: not hydrodynamo_station_has_scanned_panels(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Scan Ledge)",
            rule=lambda state, player: True
        )
    ]


class HydrodynamoStation_NorthDoorLedge(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc = "North Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                state.has("Space Jump Boots", player),
                state.has("Torvus Bog - Hydrodynamo Station | Scanned North Panel", player)
            ])  # this jump is very tight; it's doable with nothing, but I think that's unlikely for most players
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Cannon)",
            rule=lambda state, player: not hydrodynamo_station_has_scanned_panels(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Scan Ledge)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Training Access (South)",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has("Seeker Missile Launcher", player),
                    has_missile_count(state, player, 6)
                ]),
                condition_and([
                    has_missile_count(state, player, 5),
                    state.has("Screw Attack", player),
                    has_trick_enabled(state, player, "Torvus Bog - Hydrodynamo Station | Air Underwater"),
                    has_trick_enabled(state, player, "Torvus Bog - Hydrodynamo Station | Seeker Skip")
                ])
            ])
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Pickup (Missile Expansion)",
                can_access=lambda state, player: True,
                parent=self
            ),
        ]


class HydrodynamoStation_WestDoorLedge(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc = "West Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                state.has("Space Jump Boots", player),
                state.has("Torvus Bog - Hydrodynamo Station | Scanned West Panel", player)
            ]) #this jump is very tight; it's doable with nothing, but I think that's unlikely for most players
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Cannon)",
            rule=lambda state, player: not hydrodynamo_station_has_scanned_panels(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Door Ledge)",
            rule=lambda state, player: underwater_movement(state, player, "Torvus Bog - Hydrodynamo Station | Underwater Dash")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (East Door Ledge)",
            rule=lambda state, player: underwater_movement(state, player, "Torvus Bog - Hydrodynamo Station | Underwater Dash")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Gathering Access (East)",
            door=DoorCover.Light,
            rule=lambda state, player: True
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Scanned West Panel",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Hydrodynamo Station | Scanned West Panel",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            ),
        ]


class HydrodynamoStation_EastDoorLedge(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc = "East Door Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Water)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                state.has("Space Jump Boots", player),
                state.has("Torvus Bog - Hydrodynamo Station | Scanned East Panel", player)
            ])  # this jump is very tight; it's doable with nothing, but I think that's unlikely for most players
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Cannon)",
            rule=lambda state, player: not hydrodynamo_station_has_scanned_panels(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (West Door Ledge)",
            rule=lambda state, player: underwater_movement(state, player, "Torvus Bog - Hydrodynamo Station | Underwater Dash")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Door Ledge)",
            rule=lambda state, player: underwater_movement(state, player, "Torvus Bog - Hydrodynamo Station | Underwater Dash")
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (West)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Scanned East Panel",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Hydrodynamo Station | Scanned East Panel",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            ),
        ]


class HydrodynamoStation_Cannon(MetroidPrime2Region): # the movable base removes this section
    name="Hydrodynamo Station"
    desc = "Cannon"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Top)",
            rule=lambda state, player: state.has("Morph Ball", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (North Scan Ledge)",
            rule=lambda state, player: True
        )
    ]


class HydrodynamoStation_NorthScanLedge(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc="North Scan Ledge"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: True  # just fall down
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Three Doors)",
            rule=lambda state, player: state.has("Gravity Boost", player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Cannon)",
            rule=lambda state, player: condition_and([
                not hydrodynamo_station_has_scanned_panels(state, player),
                condition_or([
                    not state.has("Torvus Bog - Hydrodynamo Station | Scanned North Panel", player),
                    state.has("Space Jump Boots", player),
                    state.has("Gravity Boost", player)
                ])
            ])
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Scanned North Panel",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Hydrodynamo Station | Scanned North Panel",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: state.has("Scan Visor", player),
                parent=self,
            ),
        ]


class HydrodynamoStation_AboveMovableBase(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc = "Above Movable Base"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Cannon)",
            rule=lambda state, player: condition_or([
                state.has("Gravity Boost", player),
                condition_and(
                    state.has("Morph Ball", player), # the bubble jets at the bottom of the room push you up while morphed if you don't have gravity boost
                    not hydrodynamo_station_has_scanned_panels(state, player)
                )
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Under Movable Base)",
            rule=lambda state, player: hydrodynamo_station_has_scanned_panels(state, player)
        ),
    ]


class HydrodynamoStation_UnderMovableBase(MetroidPrime2Region):
    name="Hydrodynamo Station"
    desc = "Under Movable Base"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Shaft (Top)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (Above Movable Base)",
            rule=lambda state, player: hydrodynamo_station_has_scanned_panels(state, player)
        ),
    ]
