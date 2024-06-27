from typing import Union, Any
from eqlink.utilities.constructors import PayloadConstructor
from eqlink.utilities.parsers import Parse
from eqlink.utilities.general import EqRequest
import pandas as pd


class CoreAnalytics:
    """This class contains all simple JobsEQ Analytics.

    This class serves as a container for every simple JobsEq analytic, such as
    the snapshot, diversity, and awards analytics. In the future clusters and
    other simple features might be added to this class.

    Attributes:
      token: str
        A string containing the JobsEq authentication token.
    """

    def __init__(self, token):
        self.token = token

    def occupation_snapshot(
        self,
        region: str = "0",
        region_type: int = 10,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        occ_level: str = "2",
        hist_years: str = "5",
        proj_years: str = "1",
        model: int = 0,
        ownlevel: str = "10",
        exclude_prelim: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Occupation Snapshot Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/occupation-snapshot/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          occ_level: str
            The sub-level of the query, for example, if you query a 2-digit soc
            and then set occ_level to 3-digit, you'll receive all 3-digit SOC
            codes under that 2-digit code.
          hist_years: str
            The number of years the historical data will look back.
          proj_years: str
            The number of years from now the model will attempt to estimate.
          model: int
            The model that the analytic will use to estimate the returned data.
          ownlevel: str
            The type of employment, such as private (10), federal, or local.
          exclude_prelim: bool
            This exclude's Chmura's preliminary employment estimates.
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

        analytic_id = "346c9b58-4636-4b92-9521-be86a0868f76"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(
            histYears=hist_years,
            projYears=proj_years,
            occLevel=occ_level,
            model=model,
            ownLevel=ownlevel,
            excludePrelim=exclude_prelim,
        )

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def occupation_wages(
        self,
        region: str = "0",
        region_type: int = 10,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        occ_level: str = "2",
        hourly: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Occupation Wages Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/occupation-wages/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          occ_level: str
            The sub-level of the query, for example, if you query a 2-digit soc
            and then set occ_level to 3-digit, you'll receive all 3-digit SOC
            codes under that 2-digit code.
          hourly: bool
            Selects whether wages are returned as annual or hourly figures
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

        analytic_id = "070d4e17-cf3a-4d52-8071-48be8bea4325"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(occLevel=occ_level, hourly=hourly)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def occupation_gaps(
        self,
        region: str = "0",
        region_type: int = 10,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        soc_level: str = "2",
        years: str = "10",
        knowledgeOnly: bool = True,
        tableShowMore: bool = True,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Occupation Gaps Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/occupation-gaps/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          occ_level: str
            The sub-level of the query, for example, if you query a 2-digit soc
            and then set occ_level to 3-digit, you'll receive all 3-digit SOC
            codes under that 2-digit code.
          knowledgeOnly: bool
            Controls if only occupations which require degrees are returned.
          tableShowMore: bool
            Controls whether or not to return the expanded column.
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

        analytic_id = "f0b719b4-308b-4c5c-b689-baa6b909d5f3"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(
            socLevel=soc_level,
            years=years,
            knowledgeOnly=knowledgeOnly,
            tableShowMore=tableShowMore,
            displayType="Table",
        )

        print(constructor.send_to_json())

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def industry_snapshot(
        self,
        region: str = "0",
        region_type: int = 10,
        ind_code: str = "0",
        ind_type: int = 0,
        hist_years: int = 5,
        proj_years: int = 1,
        ind_level: str = "2",
        model: int = 0,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Industry Snapshot Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/industry-snapshot/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          hist_years: str
            The number of years the historical data will look back.
          proj_years: str
            The number of years from now the model will attempt to estimate.
          ind_level: str
            The sub-level of the query, for example, if you query a 2-digit
            NAICS and then set occ_level to 3-digit, you'll receive all 3-digit
            NAICS codes under that 2-digit code.
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

        analytic_id = "9d7913e1-8395-48ec-98b6-a5476cc9c2f3"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(
            histYears=hist_years, projYears=proj_years, indLevel=ind_level, model=model
        )

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def what_if(
        self,
        region: str = "0",
        region_type: int = 10,
        ind_code: str = "31",
        ind_type: int = 2,
        firm_size: int = 100,
        expansion_contraction: str = "Expansion",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the What If Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/what-if/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          firm_size: int
            The total employees of the hypothetical firm.
          expansion_contraction: str
            A string that defines the mode to run the analytic in, either
            'expansion' or 'contraction'.
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

        analytic_id = "8d554e48-8940-4d0f-958b-067c462340ca"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(firmSize=firm_size, type=expansion_contraction)
        constructor.nest_payload("whatIf")
        constructor.add_by_keyword(mode="WhatIf")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def shift_share(
        self,
        region: str = "0",
        region_type: int = 10,
        ind_code: str = "31",
        ind_type: int = 2,
        years: str = "10",
        own_level: str = "10",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Shift Share Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/shift-share/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          years: str
            The number of years (1-10) for the analysis.
          own_level: str
            The type of employment, such as private (10), federal, or local.
          as_frame: bool
            This value controls the return type of this function, setting
            to True returns a dataframe, False (default) returns a dictionary.

        Returns:
          Either a Pandas DataFrame containing the parsed JobsEq response, or
          a parsed Python Dictionary containing the parsed JobsEq response as
          the type of this variable depends on the as_frame parameter.
        """

        analytic_id = "9dfd4380-fe28-458f-9dcf-d2f1c4750358"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(years=years, ownLevel=own_level)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def industry_diversity(
        self,
        region: str = "0",
        region_type: int = 10,
        ind_code: str = "0",
        ind_type: int = 0,
        naics_level: str = "0",
        demographic: str = "L",
        sub_demographic: str = "L",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Industry Diversity Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/industry-diversity/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          ind_code: str
            The NAICS code of the region to be queried, supplied as a string.
          ind_type: int
            The JobsEQ type of the NAICS code provided.
          naics_level: str
            The sub-level of the query, for example, if you query a 2-digit
            NAICS and then set NAICS_level to 3-digit, you'll receive all 3-digit
            NAICS codes under that 2-digit code.
          demographic: str
            The first demographic option to look into, ex: Age, Education,
            Gender, Race, Ethnicity, or All
          sub_demographic: str
            The second demographic option to look into, the options for this
            parameter depend on the demographic option presented in the first
            demographic parameter.
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

        analytic_id = "4c03b549-365e-487f-941f-ccde3df884a3"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_industry(ind_code, ind_type)
        constructor.add_by_keyword(
            naicsLevel=naics_level, demo1=demographic, demo2=sub_demographic
        )

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def occupation_diversity(
        self,
        region: str = "0",
        region_type: int = 10,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        demographic_catagory: str = "A",
        occ_level: str = "6",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Occupation Diversity Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/occupation-diversity/

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
          demographic: str
            The demographic option to look into, ex: Age, Education,
            Gender, Race, Ethnicity, or All
          occ_level: str
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

        analytic_id = "7993e1f6-b66f-4a15-a876-3d93731affa8"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(
            category=demographic_catagory, displayMode="Table", occLevel=occ_level
        )

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def awards(
        self,
        region: str = "0",
        region_type: int = 10,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        school=None,
        model=0,
        showDetailed=True,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Awards Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/Awards/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          school: str
            The Ipeds code associated with the program to be queried.
          model: int
            The model that the analytic will use to estimate the returned data.
          showDetailed: bool
            Adds additional descriptive columns to the output.
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

        analytic_id = "feea06ae-4562-470b-afee-acc328f991ec"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(
            school=school, model=model, showDetailed=showDetailed
        )

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def willing_and_able(
        self,
        region: str = "1714",
        region_type: int = 2,
        soc_code: str = "11-1011",
        soc_type: int = 7,
        employermode: bool = False,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Willing and Able Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/willing-able/

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
          employermode: bool
            Enables or disables employer mode, which changes the perspective of
            the tool from an employee looking for a career change to an employer
            looking at potential employee's for a career change to a position,
            rather than from a position.
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

        analytic_id = "b71bc7d7-18c4-4c03-b4a0-fccbe9c5cd64"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)
        constructor.add_occupation(soc_code, soc_type)
        constructor.add_by_keyword(employermode=employermode, mode="Table")
        constructor.nest_payload("WillingAndAble")
        constructor.add_by_keyword(type="WillingAndAble")

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def job_and_talent_locator(
        self, soc_code: str = "00-0000", soc_type: int = 0, as_frame: bool = False
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Job and Talent Locator Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/job-talent-locator/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          soc_code: str
            The SOC code of the region to be queried, supplied as a string.
          soc_type: int
            The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
          school: str
            The Ipeds code associated with the program to be queried.
          model: int
            The model that the analytic will use to estimate the returned data.
          showDetailed: bool
            Adds additional descriptive columns to the output.
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

        analytic_id = "a3c057c9-49e2-4876-84c2-a198b3f84198"

        constructor = PayloadConstructor()

        constructor.add_occupation(soc_code, soc_type)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)

    def Military_Exits(
        self,
        region: str = "0",
        region_type: int = 10,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Military Exits Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/military-exits/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
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

        analytic_id = "960cf539-83f8-42a5-b640-886806c90e08"

        constructor = PayloadConstructor()

        constructor.add_region(region, region_type)

        response = EqRequest.run_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.core_analytic(response, as_frame)
