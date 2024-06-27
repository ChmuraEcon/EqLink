from typing import Union, Any
from eqlink.utilities import EqRequest
import pandas as pd
from eqlink.analytics import (
    CoreAnalytics,
    ApiSpecificTools,
    RtiAnalytics,
    DataFetch,
    IndustryOccupationMixCompound,
    LaborWageTrendsCompound,
    SupplyChainCompound,
    DemographicProfileCompound,
    SkillGapsCompound,
    MapsCompound,
    EconomicImpactCompound,
    AwardsGapCompound
)


class JobsEqConnection:
    """
    An object representing your connection to the JobsEq API server.

    Attributes:
        username: str
            Your Chmura/JobsEq username.
        password: str
            Your Chmura/JobsEq password.

    Sub-Modules:
        core contains all "Core" JobsEq Analytics:
            Occupation Snapshot, Occupation Wages, Occupation Gaps,
            Industry Snapshot, What if, Economic Impact, Shift Share,
            Industry Diversity, Occupation Diversity, Awards,
            Award Gaps (Program), Awards Gaps (Occupation), Willing and Able,
            Job And Talent Locator, and Military Exits.\n

        api contains all "Api-Specific" JobsEq Analytics:
            List Availible, List Availible Types, and List Availible Schools.\n

        industry_occupation_mix contains all "Industry Occupation Mix" related
        Analytics:
            Occupation mix (IO_mix) and Industry Mix (IO_Mix).\n

        labor_wage_trends contains all "Labor and Wage Trends" related
        Analytics:
            Employment Trends, Total Wage Trends, Cost of Living Trends,
            Average Wage Trends, Unemployment Rate Trends, and Establishment
            Trends.\n

        supply_chain contains all "Supply Chain" related Analytics:
            (Supply Chain) Suppliers, (Supply Chain) Buyers,
            and (Supply Chain) Gaps.\n

        demographic_profile contains all "Demographic Profile" related
        Analytics:
            (Current) Demographic Summary.\n

        skill_gaps contains all "Skill Gaps" related Analytics:
            (Skill Gaps) By Skill, (Skill Gaps) By Occupation, and (Skill Gaps)
            By Region.\n

        maps contains all "Maps" related Analytics:
            Awards (Map), Commute (Map), Demographics (Map), Employment (Map),
            Gdp (Map), Industry (Map), Occupation (Map), Rti (Map),
            Rural (Map), Underemployemnt (Map), and Unemployment (Map)\n

        rti contains all "Rti" related Analytics:
            Job Postings, Job Postings (Over Time), Job Postings (Wages),
            and Resume Forensics\n

        datafetch contains all "Datafetch" related Analytics:
            Occuaption DataFetch\n
    """

    def __init__(self, username, password):
        self.token = EqRequest.get_token(username, password)
        self.core = CoreAnalytics(self.token)
        self.api = ApiSpecificTools(self.token)
        self.industry_occupation_mix = IndustryOccupationMixCompound(self.token)
        self.labor_wage_trends = LaborWageTrendsCompound(self.token)
        self.supply_chain = SupplyChainCompound(self.token)
        self.demographic_profile = DemographicProfileCompound(self.token)
        self.skill_gaps = SkillGapsCompound(self.token)
        self.maps = MapsCompound(self.token)
        self.economic_impact = EconomicImpactCompound(self.token)
        self.awards_gap = AwardsGapCompound(self.token)
        self.rti = RtiAnalytics(self.token)
        self.datafetch = DataFetch(self.token)

    def __repr__(self):
        return f"Bearer {self.token}"

    def run_analytic_by_id(
        self, analytic_id: str, request_body
    ) -> Union[Any, pd.DataFrame]:

        response = EqRequest.run_analytic(self.token, analytic_id, request_body)

        return response

    def run_analytic_by_uri(
        self, v2endpoint: str, request_body
    ) -> Union[Any, pd.DataFrame]:

        response = EqRequest.run_v2_analytic(self.token, v2endpoint, request_body)

        return response
