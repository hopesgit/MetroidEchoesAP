from BaseClasses import MultiWorld, ItemClassification

from Utils import condition_or, condition_and
from ... import has_trick_enabled, can_lay_bomb, can_lay_pb, can_use_screw_attack, can_use_darkburst, can_use_sonic_boom
from .....Enums import DoorCover
from .....Locations import MetroidPrime2Location
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Items import MetroidPrime2Item


# tricks:
#         "Torvus Bog - Catacombs | Clip Through Gate",
#         "Torvus Bog - Catacombs | Underwater Dash to Bomb Slot",
#         "Torvus Bog - Catacombs | Activate Bomb Slot without Bombs",

def can_clip_through_gate(state, player, inside: bool = False) -> bool:
    return condition_and([
        condition_or([
            can_use_screw_attack(state, player),
            condition_and([
                inside,
                state.has('Morph Ball', player)
            ])
        ]),
        has_trick_enabled(state, player, "Torvus Bog - Catacombs | Clip Through Gate")
    ])


def has_lowered_gate(state, player) -> bool:
    return state.has('Torvus Bog - Catacombs | Bomb Slot Activated', player)


def can_reach_bomb_slot(state, player) -> bool:
    return condition_or([
        condition_and([
            state.has('Space Jump Boots', player),
            has_trick_enabled(state, player, "Torvus Bog - Catacombs | Underwater Dash to Bomb Slot")
        ]),
        state.has('Gravity Boost', player)
    ])


def can_activate_bomb_slot(state, player) -> bool:
    return condition_and([
        state.has('Morph Ball'),
        condition_or([
            can_lay_bomb(state, player),
            condition_and([
                has_trick_enabled("Torvus Bog - Catacombs | Activate Bomb Slot without Bombs"),
                condition_or([
                    can_use_darkburst(state, player),
                    can_use_sonic_boom(state, player)
                ])
            ])
        ])
    ])


class _Catacombs(MetroidPrime2Region):
    """A room characterized by a gated-off Dark Portal suspended above a large pool of water.
    Contains a Keybearer body.
    Enemies: Bloggs in water.
    Doors: 1 Blue, 1 Black, 1 Zebra-stripe, 1 Dark Portal"""
    name="Catacombs"


class Catacombs_TransitTunnelEastEntrance(_Catacombs):
    """An isolated ledge with a blue door that connects to Transit Tunnel East."""
    desc="Transit Tunnel East Entrance"
    exits_=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel East (Catacombs Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Portal Ledge)",
            rule = lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Keybearer Ledge)",
            rule= lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Under Water)",
            rule= lambda state, player: True
        )
    ]


class Catacombs_TransitTunnelSouthEntrance(_Catacombs):
    """A connected ledge with a zebra-stripe door that connects to Transit Tunnel South."""
    desc="Transit Tunnel South Entrance"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Transit Tunnel South (Catacombs Side)",
            door=DoorCover.Annihilator,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Portal Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Ledge)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Keybearer Ledge)",
            rule=lambda state, player: True
        )
    ]


class Catacombs_KeybearerLedge(_Catacombs):
    """A ledge sandwiched between two door alcoves and the large pool in the center of the room.
    The Keybearer Luminoth body is its most notable feature. Entry: G-Sch's Testament
    Contains a black door leading to Catacombs Access.
    Contains Grenchler enemies (later visits)."""
    desc="Keybearer Ledge"
    exits_=[
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Portal Ledge)",
            rule=lambda state, player: condition_or([
                condition_and([
                    state.has('Torvus Bog - Catacombs | Bomb Slot Activated', player),
                    state.has('Space Jump Boots', player),
                ]),
                can_clip_through_gate(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (Catacombs Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Under Water)",
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Entrance)",
            rule=lambda state, player: can_use_screw_attack(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel South Entrance)",
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                state.has('Space Jump Boots', player)
            ])
        )
    ]


class Catacombs_UnderWater(_Catacombs):
    """The pool in the center of the room.
    Contains Blogg enemies (first visit) and a Bomb Slot."""
    desc="Under Water"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Keybearer Ledge)",
            rule=lambda state, player: True
        )
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.locations = [
            MetroidPrime2Location(
                name="Bomb Slot Activated",
                locked_item=MetroidPrime2Item(
                    name="Torvus Bog - Catacombs | Bomb Slot Activated",
                    classification=ItemClassification.progression,
                    code=None,
                    player=player,
                ),
                can_access=lambda state, player: condition_and([
                    can_reach_bomb_slot(state, player),
                    can_activate_bomb_slot(state, player)
                ]),
                parent=self,
            ),
        ]


class Catacombs_PortalLedge(_Catacombs):
    """An isolated ledge suspended above the central pool.
    Until the Bomb Slot is used, it is barred from entry by a wrap-around gate.
    Contains a Lore Projector. Entry: The New Terror (GC)/Recovering Energy (Wii)"""
    desc="Portal Ledge"
    exits_=[
        MetroidPrime2Exit(
            destination="P|Dark Torvus Bog - Dungeon (Portal Ledge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Under Water)",
            rule=lambda state, player: condition_and([
                has_lowered_gate(state, player),
                can_clip_through_gate(state, player, True)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Keybearer Ledge)",
            rule=lambda state, player: has_lowered_gate(state, player)
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel East Entrance",
            rule=lambda state, player: condition_and([
                can_use_screw_attack(state, player),
                has_lowered_gate(state, player)
            ])
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Transit Tunnel South Entrance",
            rule=lambda state, player: condition_and([
                can_use_screw_attack(state, player),
                has_lowered_gate(state, player)
            ])
        )
    ]
