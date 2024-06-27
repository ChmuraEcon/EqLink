from typing import Union, Any
from eqlink.utilities.constructors import PayloadConstructor
from eqlink.utilities.parsers import Parse
from eqlink.utilities.general import EqRequest
import pandas as pd


class IndustryOccupationMixCompound:
    """A container for JobsEq's Industry/Occupation Mix endpoints.

    This class serves as a container for JobsEq's Labor and Wage trends
    analytic. Since this analytic contains multiple endpoints/options, it has
    been split into several methods. Help for the analytic and its endpoints
    can be found here: https://help.eqsuite.com/analytics/industry-occupation-mix/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self):
        return f"Bearer {self.token}"

    def occupation_mix(
        self,
        region: str = "1",
        region_type: int = 4,
        soc_code: str = "11-1011",
        soc_type: int = 7,
        years: str = "10",
        model: int = 0,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Occupation Mix endpoint of Industry/Occupation Mix.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/industry-occupation-mix/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          years: str
            The number of years (1-10) for the analysis.
          model: int
            The model that the analytic will use to estimate the returned data.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "fa6e2fbe-0f68-498e-80a6-55a6c1b020cd"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(years=years, model=model)
        constructor.nest_payload("indDist")
        constructor.add_by_keyword(queryType="IndDist", datasetKey="OccDist")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def industry_mix(
        self,
        region: str = "1",
        region_type: int = 4,
        ind_code: str = "31",
        ind_type: int = 2,
        occlevel: str = "7",
        years: str = "10",
        model: int = 0,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Industry Mix endpoint of Industry/Occupation Mix.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/industry-occupation-mix/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          occLevel: str
            The sub-level of the query, for example, if you query a 2-digit soc
            and then set occ_level to 3-digit, you'll receive all 3-digit SOC
            codes under that 2-digit code.
          years: str
            The number of years (1-10) for the analysis.
          model: int
            The model that the analytic will use to estimate the returned data.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "fa6e2fbe-0f68-498e-80a6-55a6c1b020cd"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(years=years, model=model, occLevel=occlevel)
        constructor.nest_payload("occDist")
        constructor.add_by_keyword(queryType="OccDist", datasetKey="OccDist")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)


class LaborWageTrendsCompound:
    """A container for JobsEq's Labor and Wage Trends endpoints.

    This class serves as a container for JobsEq's Labor and Wage trends
    analytic. Since this analytic contains multiple endpoints/options, it has
    been split into several methods. Help for the analytic and its endpoints
    can be found here: https://help.eqsuite.com/analytics/labor-wage-trends/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self):
        return f"Bearer {self.token}"

    def employment_trends(
        self,
        region: str = "1",
        region_type: int = 4,
        ind_code: str = "31",
        ind_type: int = 2,
        ownLevel: str = "10",
        yoyChange: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Employment Trends endpoint of Labor and Wage Trends.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/labor-wage-trends/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          ownLevel: str
            The type of employment, such as private (10), federal, or local.
          yoyChange: bool
            Toggle whether or not employment is displayed as a year over year %.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "be01565c-5935-42a6-b89a-dccc511935d3"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(ownLevel=ownLevel, yoyChange=yoyChange)
        constructor.nest_payload("employment")
        constructor.add_by_keyword(dataset="Employment", datasetKey="employment")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.labor_wage_trends(response, as_frame)

    def total_wage_trends(
        self,
        region: str = "1",
        region_type: int = 4,
        ind_code: str = "31",
        ind_type: int = 2,
        ownLevel: str = "10",
        seasonallyAdjusted: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Total Wage endpoint of Labor and Wage Trends.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/labor-wage-trends/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          ownLevel: str
            The type of employment, such as private (10), federal, or local.
          seasonallyAdjusted: bool
            Toggle whether or not wages are seasonally adjusted.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "be01565c-5935-42a6-b89a-dccc511935d3"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(
            ownLevel=ownLevel, seasonallyAdjusted=seasonallyAdjusted
        )
        constructor.nest_payload("totalWages")
        constructor.add_by_keyword(dataset="TotalWages", datasetKey="totalWages")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.labor_wage_trends(response, as_frame)

    def cost_of_living_trends(
        self,
        region: str = "1",
        region_type: int = 4,
        ind_code: str = "31",
        ind_type: int = 2,
        ownLevel: str = "10",
        yoyChange: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Cost of Living endpoint of Labor and Wage Trends.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/labor-wage-trends/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          ownLevel: str
            The type of employment, such as private (10), federal, or local.
          yoyChange: bool
            Toggle whether or not COL is displayed as a year over year %.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "be01565c-5935-42a6-b89a-dccc511935d3"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(ownLevel=ownLevel, yoyChange=yoyChange)
        constructor.nest_payload("averageWages")
        constructor.add_by_keyword(dataset="AvgWages", datasetKey="averageWages")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def average_wage_trends(
        self,
        region: str = "1",
        region_type: int = 4,
        ind_code: str = "31",
        ind_type: int = 2,
        ownLevel: str = "10",
        yoyChange: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Average Wage Trends endpoint of Labor and Wage Trends.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/labor-wage-trends/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          ownLevel: str
            The type of employment, such as private (10), federal, or local.
          yoyChange: bool
            Toggle whether or not avg wage is displayed as a year over year %.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "be01565c-5935-42a6-b89a-dccc511935d3"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(ownLevel=ownLevel, yoyChange=yoyChange)
        constructor.nest_payload("averageWages")
        constructor.add_by_keyword(dataset="AvgWages", datasetKey="averageWages")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.labor_wage_trends(response, as_frame)

    def unemployment_rate_trends(
        self,
        region: str = "1",
        region_type: int = 4,
        ind_code: str = "31",
        ind_type: int = 2,
        seasonallyAdjusted: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Unemployment Rates endpoint of Labor and Wage Trends.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/labor-wage-trends/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          seasonallyAdjusted: bool
            Toggle whether or not wages are seasonally adjusted.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "be01565c-5935-42a6-b89a-dccc511935d3"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(seasonallyAdjusted=seasonallyAdjusted)
        constructor.nest_payload("unemployment")
        constructor.add_by_keyword(dataset="Unemployment", datasetKey="unemployment")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.labor_wage_trends(response, as_frame)

    def establishment_trends(
        self,
        region: str = "1",
        region_type: int = 4,
        ind_code: str = "31",
        ind_type: int = 2,
        ownLevel: str = "10",
        yoyChange: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Establishment Trends endpoint of Labor and Wage Trends.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/labor-wage-trends/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          ownLevel: str
            The type of establishments, such as private (10), federal, or local.
          yoyChange: bool
            Toggle whether # establishments is displayed as a year over year %.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "be01565c-5935-42a6-b89a-dccc511935d3"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(ownLevel=ownLevel, yoyChange=yoyChange)
        constructor.nest_payload("establishments")
        constructor.add_by_keyword(
            dataset="Establishments", datasetKey="establishments"
        )

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.labor_wage_trends(response, as_frame)


class SupplyChainCompound:
    """A container for JobsEq's Supply Chain endpoints.

    This class serves as a container for JobsEq's Labor and Wage trends
    analytic. Since this analytic contains multiple endpoints/options, it has
    been split into several methods. Help for the analytic and its endpoints
    can be found here: https://help.eqsuite.com/analytics/supply-chain/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self):
        return f"Bearer {self.token}"

    def suppliers(
        self,
        region: str = "0",
        region_type: int = 10,
        ind_code: str = "31",
        ind_type: int = 2,
        indLevel: str = "6",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Suppliers endpoint of Supply Chain.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/supply-chain/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          indLevel: str
            The sub-level of the query, for example, if you query a 2-digit
            NAICS and then set occ_level to 3-digit, you'll receive all 3-digit
            NAICS codes under that 2-digit code.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "d2adef1d-7f93-48dc-8b33-7084c117db7b"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(indLevel=indLevel)
        constructor.nest_payload("supplier")
        constructor.add_by_keyword(dataset="Suppliers", datasetKey="supplier")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def buyers(
        self,
        region: str = "0",
        region_type: int = 10,
        ind_code: str = "31",
        ind_type: int = 2,
        indLevel: str = "6",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Buyers endpoint of Supply Chain.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/supply-chain/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          indLevel: str
            The sub-level of the query, for example, if you query a 2-digit
            NAICS and then set occ_level to 3-digit, you'll receive all 3-digit
            NAICS codes under that 2-digit code.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "d2adef1d-7f93-48dc-8b33-7084c117db7b"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(indLevel=indLevel)
        constructor.nest_payload("buyer")
        constructor.add_by_keyword(dataset="Buyers", datasetKey="buyer")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def gaps(
        self,
        region: str = "1",
        region_type: int = 4,
        indLevel: str = "6",
        dispType: str = "All",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Buyers endpoint of Supply Chain.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/supply-chain/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          indLevel: str
            The sub-level of the query, for example, if you query a 2-digit
            NAICS and then set occ_level to 3-digit, you'll receive all 3-digit
            NAICS codes under that 2-digit code.
          dispType:
            Toggles between the 'Refined' and 'All' options for inds to display
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "d2adef1d-7f93-48dc-8b33-7084c117db7b"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_by_keyword(indLevel=indLevel, dispType=dispType)
        constructor.nest_payload("gap")
        constructor.add_by_keyword(dataset="Gaps", datasetKey="gap")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)


class DemographicProfileCompound:
    """A container for JobsEq's Demographic Profile endpoints.

    This class serves as a container for JobsEq's Labor and Wage trends
    analytic. Since this analytic contains multiple endpoints/options, it has
    been split into several methods. Help for the analytic and its endpoints
    can be found here: https://help.eqsuite.com/analytics/demographic-profile/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self):
        return f"Bearer {self.token}"

    def current(
        self,
        region: str = "1",
        region_type: int = 4,
        table_type: str = "Summary",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Current Demographics endpoint of Demographic Profile.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/demographic-profile/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          table_type: str
            Controls which table is displayed, such as 'Summary' or 'Census'.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "98529f7c-deb9-421f-9ab2-9fa910d2dffc"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_by_keyword(tableType=table_type, mode="Current")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.demo_current(response, as_frame)


class SkillGapsCompound:
    """A container for JobsEq's Skill Gaps endpoints.

    This class serves as a container for JobsEq's Labor and Wage trends
    analytic. Since this analytic contains multiple endpoints/options, it has
    been split into several methods. Help for the analytic and its endpoints
    can be found here: https://help.eqsuite.com/analytics/skill-gaps/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self):
        return f"Bearer {self.token}"

    def by_skill(
        self,
        region: str = "1",
        region_type: int = 4,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        filter: str = "Hard",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the 'By Skill' endpoint of Skill Gaps.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/skill-gaps/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          filter: str
            Sets the query to inspect either 'Hard' or 'Soft' skills.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "148c7d96-36e5-446d-a9b8-f4078bd19d74"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(filter=filter, displayType="Table")
        constructor.nest_payload("bySkill")
        constructor.add_by_keyword(gapType="BySkill", datasetKey="BySkill")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def by_occupation(
        self,
        region: str = "1",
        region_type: int = 4,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        skill_code: str = "4242",
        skill_type: int = 67,
        occLevel: str = "7",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the 'By Occupation' endpoint of Skill Gaps.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/skill-gaps/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          skill_code: str
            The JobsEq skill code of the skill to be queried, this is often
            easiest to obtain by capturing a response body from JobsEq itself.
          skill_type: int
            The type code of the skill entered for 'skill_code':
            0 for certifications and 1 for skill.
          occLevel: str
            The sub-level of the query, for example, if you query a 2-digit soc
            and then set occ_level to 3-digit, you'll receive all 3-digit SOC
            codes under that 2-digit code.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "148c7d96-36e5-446d-a9b8-f4078bd19d74"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_skill(skill_code, skill_type)
        constructor.add_by_keyword(occLevel=occLevel, displayType="Table")
        constructor.nest_payload("byOccupation")
        constructor.add_by_keyword(gapType="ByOccupation", datasetKey="BySkill")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def by_region(
        self,
        region: str = "1",
        region_type: int = 4,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        skill_code: str = "4242",
        skill_type: int = 67,
        displayType: str = "Table",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the 'By Region' endpoint of Skill Gaps.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/skill-gaps/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          filter: str
            Sets the query to inspect either 'Hard' or 'Soft' skills.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "148c7d96-36e5-446d-a9b8-f4078bd19d74"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_skill(skill_code, skill_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(displayType=displayType)
        constructor.nest_payload("supply")
        constructor.add_by_keyword(gapType="Supply", datasetKey="BySkill")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)


class MapsCompound:
    """A container for JobsEq's Maps endpoints.

    This class serves as a container for JobsEq's Labor and Wage trends
    analytic. Since this analytic contains multiple endpoints/options, it has
    been split into several methods. Help for the analytic and its endpoints
    can be found here: https://help.eqsuite.com/analytics/maps/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self):
        return f"Bearer {self.token}"

    def awards_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        cipSoc_code: str = "00.0000",
        cipSoc_type: int = 150,
        awardLevel: str = "0",
        excludeOnlineSchools: bool = False,
        ncesYear: str = "2021",
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Awards endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          cipSoc_code: str
            The CIP or SOC code to be queried, inputting a CIP code shows the
            program awards by region, whereas inputting a SOC code shows the
            program awards crosswalked to SOC occupational codes.
          cipSoc_type: int
            The type code assocated with the CIP or SOC code queried, the best
            way to find this code is usually to capture the type from a JobsEq
            webapp response.
          awardLevel: str
            Controls which level of award is given, highschool, associates,
            bachelors, ect.
          excludeOnlineSchools: bool
            Toggles whether or not online degrees are included in the analytic.
          ncesYear: str
            Controls which year of nces data is queried by the analytic.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_cipsoc(cipSoc_code, cipSoc_type)
        constructor.add_by_keyword(
            awardLevel=awardLevel,
            excludeOnlineSchools=excludeOnlineSchools,
            ncesYear=ncesYear,
        )
        constructor.nest_payload("awardsMap")
        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="awards", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def commute_map(
        self,
        region: str = "1",
        region_type: int = 4,
        region_filter: str = "0",
        region_filter_type: int = 10,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        commuteDirection: str = "ToRegion",
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Commuting endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          commuteDirection: str
            Controls whether the data is show 'FromRegion' or 'ToRegion'.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(commuteDirection=commuteDirection)
        constructor.nest_payload("commuteMap")
        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="commute", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def demographics_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        demoVariable: str = "3",
        showValueAs: str = "Percentages",
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Demographics endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          demoVariable: str
            Controls which variable is queried by the analytic, these are best
            found by capturing the response body of a JobsEq Request.
          showValueAs:
            Controls whether the data is shown as 'Percentages' or 'Values'
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_by_keyword(demoVariable=demoVariable, showValueAs=showValueAs)
        constructor.nest_payload("demographicsMap")
        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="demographic", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def employment_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        emplChangeType: str = "LastYear",
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Employment endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          emplChangeType: str
            Controls if the Employment change type is 'LastYear' or 'LastQtr'.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_by_keyword(emplChangeType=emplChangeType)
        constructor.nest_payload("employmentMap")
        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="empl", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def gdp_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        gdpYear: str = "2021",
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the GDP endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          gdpYear: str
            Controls which GPD year is queried, default is set to 2021.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_by_keyword(gdpYear=gdpYear)
        constructor.nest_payload("gdpMap")
        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="gdp", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def industry_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        ind_code: str = "31",
        ind_type: int = 2,
        type: str = "Empl",
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Industry endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          type: str
            Control whether the query displays 'Empl', 'LQ', or 'Establishment'.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(type=type)
        constructor.nest_payload("industryMap")
        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="industry", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def occupation_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        occConcentrationType: str = "EmployedWork",
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Occupation endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          soc_code: str
           The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          occConcentrationType: str
            Controls the occupation concentration type of the query, either
            'EmployedWork', 'EmployedWork', 'UnemployedResidence', 'LQ',
            and 'Commute'.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(occConcentrationType=occConcentrationType)
        constructor.nest_payload("occMap")
        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="occ", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def rti_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the RTI endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          soc_code: str
           The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_rti_occupation(soc_code, soc_type)
        constructor.nest_payload("rtiMap")
        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="rti", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def rural_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Rural endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="rural", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def underemployemnt_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Rural endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="underempl", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)

    def unemployment_map(
        self,
        region_filter: str = "0",
        region_filter_type: int = 10,
        regionLevel: str = "1",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Rural endpoint of Maps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/maps/

        Args:
          region_filter: str
            Sets the visable region for the map, or in this case the region
            that all sub regions will fall within.
          region_filter_type: int
            This is the region type that corresponds to the region code in the
            region filter.
          regionLevel: str
            The subregion level to be queried, so for example setting this
            variable to 1 will show all counties in the region selected.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "434d0060-62a0-4164-916c-c1a78e44c827"

        constructor = PayloadConstructor()

        constructor.add_regionFilter(region_filter, region_filter_type)
        constructor.add_by_keyword(type="unempl", regionLevel=regionLevel)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.maps(response, as_frame)


class EconomicImpactCompound:
    """A container for JobsEq's Economic Impact endpoints.

    This class serves as a container for JobsEq's Economic Impact analytic.
    Since this analytic contains multiple endpoints/options, it has been split
    into several methods. Help for the analytic and its endpoints can be found
    here: https://help.eqsuite.com/analytics/economic-impact/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self):
        return f"Bearer {self.token}"

    def employment(
        self,
        impact_region: str = "1",
        impact_region_type: int = 4,
        event_region=None,
        event_region_type=None,
        ind_code: str = "31",
        ind_type: int = 2,
        eventSize: str = "140",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Employment endpoint of Economic Impact Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/economic-impact/

        Args:
          impact_region: str
            The region of interest, which the event will be impacting.
          impact_region_type: int
            The region type of the impact region, for example 1 == County.
          event_region: str
            The region code of the optional event region, this is the area
            the event is acutally occuring in that may impact your region,
            assuming that region is different from your impact region.
          event_region_type: str
            The region type of the optional event region specified.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          eventSize: str
            The size of the event specified in either Millions of USD
            or Employment.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "58a2d8fc-bb40-4e4d-b78e-f719fa1a361e"

        constructor = PayloadConstructor()

        constructor.add_impact_region(impact_region, impact_region_type)
        if event_region is not None or event_region_type is not None:
            constructor.add_event_region(event_region, event_region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(eventSize=eventSize, eventSizeType="Employment")

        print(constructor.send_to_json())

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def sales_output(
        self,
        impact_region: str = "1",
        impact_region_type: int = 4,
        event_region=None,
        event_region_type=None,
        ind_code: str = "31",
        ind_type: int = 2,
        eventSize: str = "20",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Sales Output endpoint of Economic Impact Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link: https://help.eqsuite.com/analytics/economic-impact/

        Args:
          impact_region: str
            The region of interest, which the event will be impacting.
          impact_region_type: int
            The region type of the impact region, for example 1 == County.
          event_region: str
            The region code of the optional event region, this is the area
            the event is acutally occuring in that may impact your region,
            assuming that region is different from your impact region.
          event_region_type: str
            The region type of the optional event region specified.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          eventSize: str
            The size of the event specified in either Millions of USD
            or Employment.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "58a2d8fc-bb40-4e4d-b78e-f719fa1a361e"

        constructor = PayloadConstructor()

        constructor.add_impact_region(impact_region, impact_region_type)
        if event_region is not None or event_region_type is not None:
            constructor.add_event_region(event_region, event_region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(eventSize=eventSize, eventSizeType="SaleOutput")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)


class AwardsGapCompound:
    """A container for JobsEq's Awards Gap endpoints.

    This class serves as a container for JobsEq's Awards Gap analytic.
    Since this analytic contains multiple endpoints/options, it has been split
    into several methods. Help for the analytic and its endpoints can be found
    here: https://help.eqsuite.com/analytics/award-gaps/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self):
        return f"Bearer {self.token}"

    def program(
        self,
        region: str = "1714",
        region_type: int = 2,
        cip_code: str = "00.0000",
        cip_type: int = 0,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Program endpoint of the Awards Gaps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/award-gaps/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          cip_code: str
            The CIP code of the program to be queried.
          cip_type: int
            The CIP type corresponding to the program to be queried.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "ae95e9c6-de90-492c-a7e3-d07e8ea89d2b"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_cip(cip_code, cip_type)
        constructor.nest_payload("program")
        constructor.add_by_keyword(dataset="Program", datasetKey="program")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def occupation(
        self,
        region: str = "1714",
        region_type: int = 2,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        socLevel: str = "7",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Occupation endpoint of the Award Gaps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/award-gaps/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
            demographic parameter.
          soc_code: str
           The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          socLevel: str
            The sub-level of the query, for example, if you query a 2-digit soc
            and then set occ_level to 3-digit, you'll receive all 3-digit SOC
            codes under that 2-digit code.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.

        Raises:
          Nothing
        """

        analytic_id = "ae95e9c6-de90-492c-a7e3-d07e8ea89d2b"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(socLevel=socLevel)
        constructor.nest_payload("occupation")
        constructor.add_by_keyword(dataset="Occupation", datasetKey="occupation")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)
