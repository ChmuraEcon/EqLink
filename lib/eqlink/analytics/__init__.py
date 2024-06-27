"""
This submodule contains the classes that group the functions mapped to JobsEq API
endpoints.

End users of the package can and should ignore all the submodules found within this
submodule, since all the endpoints are collected into the JobsEqConnection Class.
"""

from .core import CoreAnalytics
from .api import ApiSpecificTools
from .rti import RtiAnalytics, RtiFilter
from .tablebuilders import DataFetch, DfField
from .compound import (
    IndustryOccupationMixCompound,
    LaborWageTrendsCompound,
    SupplyChainCompound,
    DemographicProfileCompound,
    SkillGapsCompound,
    MapsCompound,
    EconomicImpactCompound,
    AwardsGapCompound
)

__all__ = [
    "CoreAnalytics",
    "ApiSpecificTools",
    "RtiAnalytics",
    "RtiFilter",
    "DataFetch",
    "IndustryOccupationMixCompound",
    "LaborWageTrendsCompound",
    "SupplyChainCompound",
    "DemographicProfileCompound",
    "SkillGapsCompound",
    "MapsCompound",
    "EconomicImpactCompound",
    "DfField",
    "AwardsGapCompound"
]
