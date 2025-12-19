from .temple_grounds.agon_transport_access import *
from .temple_grounds.collapsed_tunnel import *
from .temple_grounds.command_chamber import *
from .temple_grounds.communication_area import *
from .temple_grounds.dynamo_chamber import *
from .temple_grounds.fortress_transport_access import *
from .temple_grounds.gfmc_compound import *
from .temple_grounds.grand_windchamber import *
from .temple_grounds.hall_of_eyes import *
from .temple_grounds.hall_of_honored_dead import *
from .temple_grounds.hive_access_tunnel import *
from .temple_grounds.hive_chamber_a import *
from .temple_grounds.hive_chamber_b import *
from .temple_grounds.hive_chamber_c import *
from .temple_grounds.hive_save_station import *
from .temple_grounds.hive_storage import *
from .temple_grounds.hive_transport_area import *
from .temple_grounds.hive_tunnel import *
from .temple_grounds.industrial_site import *
from .temple_grounds.landing_site import *
from .temple_grounds.meeting_grounds import *
from .temple_grounds.path_of_eyes import *
from .temple_grounds.path_of_honor import *
from .temple_grounds.sacred_bridge import *
from .temple_grounds.sacred_path import *
from .temple_grounds.service_access import *
from .temple_grounds.storage_cavern_a import *
from .temple_grounds.storage_cavern_b import *
from .temple_grounds.temple_assembly_site import *
from .temple_grounds.temple_transport_a import TempleTransportA as TempleGrounds_TempleTransportA
from .temple_grounds.temple_transport_b import TempleTransportB as TempleGrounds_TempleTransportB
from .temple_grounds.temple_transport_c import TempleTransportC as TempleGrounds_TempleTransportC
from .temple_grounds.torvus_transport_access import TorvusTransportAccess as TempleGrounds_TorvusTransportAccess
from .temple_grounds.transport_to_agon_wastes import TransportToAgonWastes as TempleGrounds_TransportToAgonWastes
from .temple_grounds.transport_to_torvus_bog import TransportToTorvusBog as TempleGrounds_TransportToTorvusBog
from .temple_grounds.transport_to_sanctuary_fortress import TransportToSanctuaryFortress as TempleGrounds_TransportToSanctuaryFortress
from .temple_grounds.trooper_security_station import *
from .temple_grounds.windchamber_gateway import *
from .temple_grounds.windchamber_tunnel import *
from .torvus_bog.abandoned_worksite import *
from .torvus_bog.catacombs import *
from .torvus_bog.catacombs_access import *
from .torvus_bog.controller_access import *
from .torvus_bog.forgotten_bridge import *
from .torvus_bog.fortress_transport_access import *
from .torvus_bog.gathering_access import *
from .torvus_bog.gathering_hall import *
from .torvus_bog.great_bridge import *
from .torvus_bog.grove_access import *
from .torvus_bog.hydrochamber_storage import *
from .torvus_bog.hydrodynamo_shaft import *
from .torvus_bog.hydrodynamo_station import *
from .torvus_bog.main_hydrochamber import *
from .torvus_bog.meditation_vista import *
from .torvus_bog.path_of_roots import *
from .torvus_bog.plaza_access import *
from .torvus_bog.portal_chamber import *
from .torvus_bog.ruined_alcove import *
from .torvus_bog.save_station_a import *
from .torvus_bog.save_station_b import *
from .torvus_bog.temple_access import *
from .torvus_bog.temple_transport_access import *
from .torvus_bog.torvus_energy_controller import *
from .torvus_bog.torvus_grove import *
from .torvus_bog.torvus_lagoon import *
from .torvus_bog.torvus_map_station import *
from .torvus_bog.torvus_plaza import *
from .torvus_bog.torvus_temple import *
from .torvus_bog.training_access import *
from .torvus_bog.training_chamber import *
from .torvus_bog.transit_tunnel_east import *
from .torvus_bog.transit_tunnel_south import *
from .torvus_bog.transit_tunnel_west import *
from .torvus_bog.transport_to_agon_wastes import *
from .torvus_bog.transport_to_temple_grounds import *
from .torvus_bog.transport_to_sanctuary_fortress import *
from .torvus_bog.underground_transport import *
from .torvus_bog.underground_tunnel import *


def temple_grounds_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Temple Grounds"

    return [
        # Temple Grounds - Agon Transport Access
        AgonTransportAccess(region_name, player, multiworld),

        # Temple Grounds - Collapsed Tunnel
        CollapsedTunnel_IndustrialSiteSide(region_name, player, multiworld),
        CollapsedTunnel_TempleAssemblySiteSide(region_name, player, multiworld),

        # Temple Grounds - Command Chamber
        CommandChamber(region_name, player, multiworld),

        # Temple Grounds - Communication Area
        CommunicationArea_Bottom(region_name, player, multiworld),
        CommunicationArea_ItemLedge(region_name, player, multiworld),
        CommunicationArea_Top(region_name, player, multiworld),

        # Temple Grounds - Dynamo Chamber
        DynamoChamber_BetweenItemGates(region_name, player, multiworld),
        DynamoChamber_Center(region_name, player, multiworld),
        DynamoChamber_CommunicationAreaSide(region_name, player, multiworld),
        DynamoChamber_Item(region_name, player, multiworld),
        DynamoChamber_TempleAssemblySiteSide(region_name, player, multiworld),

        # Temple Grounds - Fortress Transport Access
        FortressTransportAccess_Bottom(region_name, player, multiworld),
        FortressTransportAccess_Top(region_name, player, multiworld),

        # Temple Grounds - GFMC Compound
        GFMCCompound_AboveShip(region_name, player, multiworld),
        GFMCCompound_BehindTranslatorGate(region_name, player, multiworld),
        GFMCCompound_Center(region_name, player, multiworld),
        GFMCCompound_Cutscene(region_name, player, multiworld),
        GFMCCompound_SacredBridgeLedge(region_name, player, multiworld),
        GFMCCompound_TrooperSecurityStationSide(region_name, player, multiworld),
        GFMCCompound_WindchamberTunnelLedge(region_name, player, multiworld),

        # Temple Grounds - Grand Windchamber
        GrandWindchamber_Cannon(region_name, player, multiworld),
        GrandWindchamber_Platform(region_name, player, multiworld),
        GrandWindchamber_WindchamberGatewaySide(region_name, player, multiworld),
        GrandWindchamber_WindchamberTunnelSide(region_name, player, multiworld),

        # Temple Grounds - Hall of Eyes
        HallOfEyes_Bottom(region_name, player, multiworld),
        HallOfEyes_Top(region_name, player, multiworld),

        # Temple Grounds - Hall of Honored Dead
        HallOfHonoredDead(region_name, player, multiworld),
        HallOfHonoredDead_PathOfHonorSide(region_name, player, multiworld),

        # Temple Grounds - Hive Access Tunnel
        HiveAccessTunnel_HiveTransportAreaSide(region_name, player, multiworld),
        HiveAccessTunnel_LandingSiteSide(region_name, player, multiworld),

        # Temple Grounds - Hive Chamber A
        HiveChamberA(region_name, player, multiworld),
        HiveChamberA_DarkMissileTrooper(region_name, player, multiworld),

        # Temple Grounds - Hive Chamber B
        HiveChamberB(region_name, player, multiworld),
        HiveChamberB_BehindBombCover(region_name, player, multiworld),

        # Temple Grounds - Hive Chamber C
        HiveChamberC(region_name, player, multiworld),

        # Temple Grounds - Hive Save Station
        HiveSaveStation(region_name, player, multiworld),

        # Temple Grounds - Hive Storage
        HiveStorage(region_name, player, multiworld),

        # Temple Grounds - Hive Transport Area
        HiveTransportArea_BehindTranslatorGate(region_name, player, multiworld),
        HiveTransportArea_Bottom(region_name, player, multiworld),
        HiveTransportArea_Top(region_name, player, multiworld),

        # Temple Grounds - Hive Tunnel
        HiveTunnel(region_name, player, multiworld),

        # Temple Grounds - Industrial Site
        IndustrialSite_BehindTranslatorGate(region_name, player, multiworld),
        IndustrialSite_Center(region_name, player, multiworld),
        IndustrialSite_CollapsedTunnelLedge(region_name, player, multiworld),
        IndustrialSite_FrontOfTranslatorGate(region_name, player, multiworld),
        IndustrialSite_Gate(region_name, player, multiworld),
        IndustrialSite_HiveTransportAreaSide(region_name, player, multiworld),

        # Temple Grounds - Landing Site
        LandingSite_Bottom(region_name, player, multiworld),
        LandingSite_Top(region_name, player, multiworld),

        # Temple Grounds - Meeting Grounds
        MeetingGrounds_Bottom(region_name, player, multiworld),
        MeetingGrounds_GreatTempleSide(region_name, player, multiworld),
        MeetingGrounds_Top(region_name, player, multiworld),

        # Temple Grounds - Path of Eyes
        PathOfEyes_Center(region_name, player, multiworld),
        PathOfEyes_HallOfEyesSide(region_name, player, multiworld),
        PathOfEyes_TorvusTransportAccessSide(region_name, player, multiworld),
        PathOfEyes_TranslatorGate(region_name, player, multiworld),
        PathOfEyes_UTurn(region_name, player, multiworld),
        PathOfEyes_Waterway(region_name, player, multiworld),
        PathOfEyes_WindchamberGatewaySide(region_name, player, multiworld),

        # Temple Grounds - Path of Honor
        PathOfHonor_Bottom(region_name, player, multiworld),
        PathOfHonor_Top(region_name, player, multiworld),

        # Temple Grounds - Sacred Bridge
        SacredBridge_Center(region_name, player, multiworld),
        SacredBridge_GFMCCompoundSide(region_name, player, multiworld),
        SacredBridge_SacredPathSide(region_name, player, multiworld),

        # Temple Grounds - Sacred Path
        SacredPath_GreatTempleSide(region_name, player, multiworld),
        SacredPath_PortalLedge(region_name, player, multiworld),
        SacredPath_SacredBridgeSide(region_name, player, multiworld),

        # Temple Grounds - Service Access
        ServiceAccess_Bottom_MeetingGroundsSide(region_name, player, multiworld),
        ServiceAccess_Bottom_PathOfHonorSide(region_name, player, multiworld),
        ServiceAccess_Bottom_Tunnel(region_name, player, multiworld),
        ServiceAccess_Top_MeetingGroundsSide(region_name, player, multiworld),
        ServiceAccess_Top_PathOfHonorSide(region_name, player, multiworld),

        # Temple Grounds - Storage Cavern A
        StorageCavernA(region_name, player, multiworld),

        # Temple Grounds - Storage Cavern B
        StorageCavernB(region_name, player, multiworld),

        # Temple Grounds - Temple Assembly Site
        TempleAssemblySite_BehindLightBeamBlock(region_name, player, multiworld),
        TempleAssemblySite_BehindTranslatorGate(region_name, player, multiworld),
        TempleAssemblySite_Center(region_name, player, multiworld),
        TempleAssemblySite_CollapsedTunnelSide(region_name, player, multiworld),
        TempleAssemblySite_DynamoChamberLedge(region_name, player, multiworld),
        TempleAssemblySite_ItemLedge(region_name, player, multiworld),
        TempleAssemblySite_StorageCavernBSide(region_name, player, multiworld),

        # Temple Grounds - Temple Transport A
        TempleGrounds_TempleTransportA(region_name, player, multiworld),

        # Temple Grounds - Temple Transport B
        TempleGrounds_TempleTransportB(region_name, player, multiworld),

        # Temple Grounds - Temple Transport C
        TempleGrounds_TempleTransportC(region_name, player, multiworld),

        # Temple Grounds - Torvus Transport Access
        TempleGrounds_TorvusTransportAccess(region_name, player, multiworld),

        # Temple Grounds - Transport to Agon Wastes
        TempleGrounds_TransportToAgonWastes(region_name, player, multiworld),

        # Temple Grounds - Transport to Sanctuary Fortress
        TempleGrounds_TransportToSanctuaryFortress(region_name, player, multiworld),

        # Temple Grounds - Transport to Torvus Bog
        TempleGrounds_TransportToTorvusBog(region_name, player, multiworld),

        # Temple Grounds - Trooper Security Station
        TrooperSecurityStation_CommunicationAreaSide(region_name, player, multiworld),
        TrooperSecurityStation_GFMCCompoundSide(region_name, player, multiworld),

        # Temple Grounds - Windchamber Gateway
        WindchamberGateway_GrandWindchamberSide(region_name, player, multiworld),
        WindchamberGateway_PathOfEyesSide(region_name, player, multiworld),
        WindchamberGateway_Platform(region_name, player, multiworld),

        # Temple Grounds - Windchamber Tunnel
        WindchamberTunnel_GFMCCompoundSide(region_name, player, multiworld),
        WindchamberTunnel_GrandWindchamberSide(region_name, player, multiworld),
    ]


def torvus_bog_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Torvus Bog"
    return [
        # Torvus Bog - Abandoned Worksite
        AbandonedWorksite_ForgottenBridgeEntrance(region_name, player, multiworld),
        AbandonedWorksite_GreatBridgeEntrance(region_name, player, multiworld),
        AbandonedWorksite_LedgeForgottenBridgeSide(region_name, player, multiworld),
        AbandonedWorksite_LedgeGreatBridgeSide(region_name, player, multiworld),
        AbandonedWorksite_MorphBallTunnel(region_name, player, multiworld),
        AbandonedWorksite_PickupLedge(region_name, player, multiworld),

        # Torvus Bog - Catacombs
        Catacombs_KeybearerLedge(region_name, player, multiworld),
        Catacombs_PortalLedge(region_name, player, multiworld),
        Catacombs_TransitTunnelEastEntrance(region_name, player, multiworld),
        Catacombs_TransitTunnelSouthEntrance(region_name, player, multiworld),
        Catacombs_UnderWater(region_name, player, multiworld),

        # Torvus Bog - Catacombs Access
        CatacombsAccess_Catacombs_Side(region_name, player, multiworld),
        CatacombsAccess_HydrodynamoStation(region_name, player, multiworld),

        # Torvus Bog - Controller Access
        TorvusBog_ControllerAccess(region_name, player, multiworld),

        # Torvus Bog - Forgotten Bridge
        ForgottenBridge_Bridge(region_name, player, multiworld),
        ForgottenBridge_Cage(region_name, player, multiworld),
        ForgottenBridge_Cliffs(region_name, player, multiworld),
        ForgottenBridge_DarkPortalLedge(region_name, player, multiworld),
        ForgottenBridge_PickupLedge(region_name, player, multiworld),
        ForgottenBridge_Shallows(region_name, player, multiworld),

        # Torvus Bog - Fortress Transport Access
        TorvusBog_FortressTransportAccess_AboveWater(region_name, player, multiworld),
        TorvusBog_FortressTransportAccess_NorthLedge(region_name, player, multiworld),
        TorvusBog_FortressTransportAccess_SouthLedge(region_name, player, multiworld),
        TorvusBog_FortressTransportAccess_UnderWater(region_name, player, multiworld),

        # Torvus Bog - Gathering Access
        GatheringAccess(region_name, player, multiworld),

        # Torvus Bog - Gathering Hall
        GatheringHall_Bottom(region_name, player, multiworld),
        GatheringHall_CannonLedge(region_name, player, multiworld),
        GatheringHall_ItemLedge(region_name, player, multiworld),
        GatheringHall_LaserLedge(region_name, player, multiworld),
        GatheringHall_NorthDoorLedge(region_name, player, multiworld),
        GatheringHall_PortalAlcove(region_name, player, multiworld),
        GatheringHall_SouthDoorLedge(region_name, player, multiworld),
        GatheringHall_SpiderTracks(region_name, player, multiworld),
        GatheringHall_UpperDoorLedge(region_name, player, multiworld),

        # Torvus Bog - Great Bridge
        GreatBridge_Beach(region_name, player, multiworld),
        GreatBridge_BehindTranslatorGate(region_name, player, multiworld),
        GreatBridge_Bridge(region_name, player, multiworld),
        GreatBridge_CannonLedge(region_name, player, multiworld),
        GreatBridge_MorphBallTunnel(region_name, player, multiworld),
        GreatBridge_NorthPath(region_name, player, multiworld),
        GreatBridge_ScanPanelLedge(region_name, player, multiworld),

        # Torvus Bog - Grove Access
        GroveAccess(region_name, player, multiworld),

        # Torvus Bog - Hydrochamber Storage
        HydrochamberStorage(region_name, player, multiworld),

        # Torvus Bog - Hydrodynamo Shaft
        HydrodynamoShaft_Bottom(region_name, player, multiworld),
        HydrodynamoShaft_Main(region_name, player, multiworld),
        HydrodynamoShaft_PortalAlcove(region_name, player, multiworld),
        HydrodynamoShaft_Stairs(region_name, player, multiworld),
        HydrodynamoShaft_Top(region_name, player, multiworld),

        # Torvus Bog - Hydrodynamo Station
        HydrodynamoStation_AboveMovableBase(region_name, player, multiworld),
        HydrodynamoStation_AboveWater(region_name, player, multiworld),
        HydrodynamoStation_Cannon(region_name, player, multiworld),
        HydrodynamoStation_EastDoorLedge(region_name, player, multiworld),
        HydrodynamoStation_NorthDoorLedge(region_name, player, multiworld),
        HydrodynamoStation_NorthScanLedge(region_name, player, multiworld),
        HydrodynamoStation_ThreeDoors(region_name, player, multiworld),
        HydrodynamoStation_Top(region_name, player, multiworld),
        HydrodynamoStation_TopDoorLedge(region_name, player, multiworld),
        HydrodynamoStation_UnderMovableBase(region_name, player, multiworld),
        HydrodynamoStation_WestDoorLedge(region_name, player, multiworld),

        # Torvus Bog - Main Hydrochamber
        MainHydrochamber_LowerDoor(region_name, player, multiworld),
        MainHydrochamber_Main(region_name, player, multiworld),
        MainHydrochamber_PortalLedge(region_name, player, multiworld),
        MainHydrochamber_SpiderTrack(region_name, player, multiworld),
        MainHydrochamber_Top(region_name, player, multiworld),

        # Torvus Bog - Meditation Vista
        MeditationVista_Entrance(region_name, player, multiworld),
        MeditationVista_FloatingPlatform(region_name, player, multiworld),

        # Torvus Bog - Path of Roots
        PathOfRoots_AboveCage(region_name, player, multiworld),
        PathOfRoots_GreatBridgeLedge(region_name, player, multiworld),
        PathOfRoots_LagoonSide(region_name, player, multiworld),
        PathOfRoots_Middle(region_name, player, multiworld),

        # Torvus Bog - Plaza Access
        TorvusBog_PlazaAccess_ForgottenBridgeEntrance(region_name, player, multiworld),
        TorvusBog_PlazaAccess_HalfPipe(region_name, player, multiworld),
        TorvusBog_PlazaAccess_Maze(region_name, player, multiworld),
        TorvusBog_PlazaAccess_MorphBallTunnelForgottenBridgeSide(region_name, player, multiworld),
        TorvusBog_PlazaAccess_MorphBallTunnelTorvusPlazaSide(region_name, player, multiworld),
        TorvusBog_PlazaAccess_TorvusPlazaEntrance(region_name, player, multiworld),

        # Torvus Bog - Portal Chamber
        TorvusBog_PortalChamber_Center(region_name, player, multiworld),
        TorvusBog_PortalChamber_GreatBridgeSide(region_name, player, multiworld),
        TorvusBog_PortalChamber_MorphBallTunnel(region_name, player, multiworld),
        TorvusBog_PortalChamber_TorvusLagoonSide(region_name, player, multiworld),

        # Torvus Bog - Ruined Alcove
        RuinedAlcove(region_name, player, multiworld),

        # Torvus Bog - Save Station A
        TorvusBog_SaveStationA(region_name, player, multiworld),

        # Torvus Bog - Save Station B
        TorvusBog_SaveStationB(region_name, player, multiworld),

        # Torvus Bog - Temple Access
        TorvusBog_TempleAccess_LowerGreatBridgeEntrance(region_name, player, multiworld),
        TorvusBog_TempleAccess_LowerTorvusTempleEntrance(region_name, player, multiworld),
        TorvusBog_TempleAccess_MorphBallTunnel(region_name, player, multiworld),
        TorvusBog_TempleAccess_PickupTube(region_name, player, multiworld),
        TorvusBog_TempleAccess_Upper(region_name, player, multiworld),

        # Torvus Bog - Temple Transport Access
        TorvusBog_TempleTransportAccess(region_name, player, multiworld),

        # Torvus Bog - Torvus Energy Controller
        TorvusEnergyController(region_name, player, multiworld),

        # Torvus Bog - Torvus Grove
        TorvusGrove_BehindBreakableWall(region_name, player, multiworld),
        TorvusGrove_Center(region_name, player, multiworld),
        TorvusGrove_ConnectorLedge(region_name, player, multiworld),
        TorvusGrove_CurvedLedge(region_name, player, multiworld),
        TorvusGrove_IsolatedLedge(region_name, player, multiworld),
        TorvusGrove_UpperDoorLedge(region_name, player, multiworld),

        # Torvus Bog - Torvus Lagoon
        TorvusLagoon_Beach(region_name, player, multiworld),
        TorvusLagoon_Bridge(region_name, player, multiworld),
        TorvusLagoon_PortalChamberLedge(region_name, player, multiworld),
        TorvusLagoon_RuinedAlcoveLedge(region_name, player, multiworld),
        TorvusLagoon_SaveRoomLedge(region_name, player, multiworld),
        TorvusLagoon_UnderwaterLedge(region_name, player, multiworld),

        # Torvus Bog - Torvus Map Station
        TorvusMapStation(region_name, player, multiworld),

        # Torvus Bog - Torvus Plaza
        TorvusPlaza_CannonLedge(region_name, player, multiworld),
        TorvusPlaza_Entrance(region_name, player, multiworld),
        TorvusPlaza_HalfPipe(region_name, player, multiworld),
        TorvusPlaza_ItemLedge(region_name, player, multiworld),
        TorvusPlaza_SpiderChallenge(region_name, player, multiworld),
        TorvusPlaza_SpiderTrack(region_name, player, multiworld),

        # Torvus Bog - Torvus Temple
        TorvusTemple_Arena(region_name, player, multiworld),
        TorvusTemple_OutOfBounds(region_name, player, multiworld),
        TorvusTemple_Underground(region_name, player, multiworld),
        TorvusTemple_UndergroundTransportEntrance(region_name, player, multiworld),
        TorvusTemple_Upper(region_name, player, multiworld),

        # Torvus Bog - Training Access
        TrainingAccess(region_name, player, multiworld),

        # Torvus Bog - Training Chamber
        TrainingChamber_BehindStatue(region_name, player, multiworld),
        TrainingChamber_Center(region_name, player, multiworld),
        TrainingChamber_EastCagedArea(region_name, player, multiworld),
        TrainingChamber_LedgeBelowSouthDoor(region_name, player, multiworld),
        TrainingChamber_NorthDoorLedge(region_name, player, multiworld),
        TrainingChamber_SouthDoorLedge(region_name, player, multiworld),
        TrainingChamber_SpiderTracks(region_name, player, multiworld),
        TrainingChamber_StatuePlatform(region_name, player, multiworld),
        TrainingChamber_WestCagedArea(region_name, player, multiworld),

        # Torvus Bog - Transit Tunnel East
        TransitTunnelEast_CatacombsSide(region_name, player, multiworld),
        TransitTunnelEast_TrainingChamberSide(region_name, player, multiworld),

        # Torvus Bog - Transit Tunnel South
        TransitTunnelSouth_CatacombsSide(region_name, player, multiworld),
        TransitTunnelSouth_GatheringHallSide(region_name, player, multiworld),
        TransitTunnelSouth_MorphBallPuzzle(region_name, player, multiworld),

        # Torvus Bog - Transit Tunnel West
        TransitTunnelWest_NorthSide(region_name, player, multiworld),
        TransitTunnelWest_SouthSide(region_name, player, multiworld),

        # Torvus Bog - Transport to Agon Wastes
        TorvusBog_TransportToAgonWastes(region_name, player, multiworld),

        # Torvus Bog - Transport to Sanctuary Fortress
        TorvusBog_TransportToSanctuaryFortress(region_name, player, multiworld),

        # Torvus Bog - Transport to Temple Grounds
        TorvusBog_TransportToTempleGrounds(region_name, player, multiworld),

        # Torvus Bog - Underground Transport
        UndergroundTransport_Lower(region_name, player, multiworld),
        UndergroundTransport_Shaft(region_name, player, multiworld),
        UndergroundTransport_Upper(region_name, player, multiworld),

        # Torvus Bog - Underground Tunnel
        UndergroundTunnel_AfterFalls(region_name, player, multiworld),
        UndergroundTunnel_Tunnel(region_name, player, multiworld),
    ]
