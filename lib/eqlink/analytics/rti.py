from typing import Union, Dict, Optional, List, Any
from eqlink.utilities.constructors import PayloadConstructor
from eqlink.utilities.parsers import Parse
from eqlink.utilities.general import EqRequest
import pandas as pd
import json


class RtiFilter:
  
    def __init__(
        self,
        field: Optional[str] = None,
        key: Optional[str] = None,
        filtertype: Optional[str] = None,
    ) -> None:
        """This class is used to instantiate RtiFilter "Filter" instances.

        This class is used to instantiate RtiFilter "Filter" instances. These
        instances can be used to add filters to your RTI api queries. Bt
        adding multiple "Filter" instances you can build up complex RTI
        Queries, yeilding the same results you can expect from the JobsEQ SaaS.

        Attributes:
            field: str
              The field to be filtered by the JobsEQ RTI Analytic.
            key: str
              The key, string, soc, or other type of varible to filter by.
            filtertype: str
              The type of filter to be employed by the analytic.
        """

        self.field = field
        self.key = key
        self.filtertype = filtertype

    def __repr__(self) -> str:
        body = {
            "filters": [
                {"field": self.field, "key": self.key, "filterType": self.filtertype}
            ]
        }

        return json.dumps(body)


class RtiAnalytics:
    """This class contains all JobsEq RTI/NT-LMI Analytics.

    This class serves as a container for every RTI/NT-LMI JobsEq analytic, such
    as RTI job postings, aggregate posting analysis, and postings wage data. In
    the future resume forensics and other simple features might be added to this
    class. More information on RTI can be found here:
    https://help.eqsuite.com/analytics/rti/

    Attributes:
        token: A string containing the JobsEq authentication token
    """

    def __init__(self, token):
        self.token = token

    def job_postings(
        self,
        region: str = "0",
        region_type: int = 10,
        rti_filters: Optional[List["RtiFilter"]] = None,
        excludeStaffing: Optional[bool] = False,
        freetext: Optional[str] = None,
        timeframe: Optional[str] = "Last30Days",
        postState: str = "New",
        start: Optional[str] = None,
        end: Optional[str] = None,
        startRecord: int = 0,
        endRecord: int = 20,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Job Postings endpoint of the RTI Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/rti/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          rti_filters: List['RtiFilter']
            A list of the RtiFilter object, used to specify the filters to be
            used when running the query. See 'RtiFilter' for more information
            on how to use this feature.
          excludeStaffing: bool
            Toggles whether or not postings from staffing companies are
            returned by the endpoint.
          freetext: str
            A freetext full-text keyword filter to apply to the job
            postings. Returns only postings containing this keyword.
          timeframe: str
            A string that specifies the relative timeframe of the
            query. "Last30Days", "Last90Days", ect. More information can be
            found on the JobsEqApi help portal.
          postState: str
            Defines the state of the posts to be returned, this could be "new"
            postings durning the timeframe specified, "open" postings, or a
            number of other options.
          start: str
            The starting timestamp of the queried postings, this parameter is
            overriden by 'timeframe'.
          end: str
            The ending timestamp of the queried postings, this parameter is
            overriden by 'timeframe'.
          startRecord: int
            The index of the first posting to return from the query, useful
            for batching calls asynchronously.
          endRecord: int
            The index of the last posting to return from the query, allowing
            you to control the number of job postings returned.
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

        analytic_id = "JobPosts"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)

        filter_obj: Dict[str, Any] = {"filters": []}
        if rti_filters:
            for filter in rti_filters:
                filter_obj["filters"].append(
                    {
                        "field": filter.field,
                        "key": filter.key,
                        "filterType": filter.filtertype,
                    }
                )
        constructor.payload |= filter_obj

        constructor.add_by_keyword(
            excludeStaffing=excludeStaffing,
            freetext=freetext,
            timeframe=timeframe,
            postState=postState,
            start=start,
            end=end,
            startRecord=startRecord,
            endRecord=endRecord,
        )

        response = EqRequest.run_v2_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.v2_core(response, as_frame=as_frame)

    def job_postings_over_time(
        self,
        region: str = "0",
        region_type: int = 10,
        rti_filters: Optional[List["RtiFilter"]] = None,
        freetext: Optional[str] = None,
        timeframe: Optional[str] = "Last30Days",
        postState: str = "New",
        start: Optional[str] = None,
        end: Optional[str] = None,
        interval: str = "Daily",
        adType: str = "All",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Job Postings over time endpoint of the RTI Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/rti/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          rti_filters: List['RtiFilter']
            A list of the RtiFilter object, used to specify the filters to be
            used when running the query. See 'RtiFilter' for more information
            on how to use this feature.
          freetext: str
            A freetext full-text keyword filter to apply to the job
            postings. Returns only postings containing this keyword.
          timeframe: str
            A string that specifies the relative timeframe of the
            query. "Last30Days", "Last90Days", ect. More information can be
            found on the JobsEqApi help portal.
          postState: str
            Defines the state of the posts to be returned, this could be "new"
            postings durning the timeframe specified, "open" postings, or a
            number of other options.
          start: str
            The starting timestamp of the queried postings, this parameter is
            overriden by 'timeframe'.
          end: str
            The ending timestamp of the queried postings, this parameter is
            overriden by 'timeframe'.
          interval: str
            The timeframe used to group/aggregate postings, this can be weekly,
            monthly, or yearly.
          adType:
            Controls the types of ads aggregated in the query, all options can
            be found @ the developer portal: https://jobseq.eqsuite.com/apidocs
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

        analytic_id = "RealTimeIntelligenceOverTime"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)

        filter_obj: Dict[str, Any] = {"filters": []}
        if rti_filters:
            for filter in rti_filters:
                filter_obj["filters"].append(
                    {
                        "field": filter.field,
                        "key": filter.key,
                        "filterType": filter.filtertype,
                    }
                )
        constructor.payload |= filter_obj

        constructor.add_by_keyword(
            freetext=freetext,
            timeframe=timeframe,
            postState=postState,
            start=start,
            end=end,
            interval=interval,
            adType=adType,
        )

        response = EqRequest.run_v2_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.v2_core_rti_overtime(response, as_frame)

    def job_posting_wages(
        self,
        region: str = "0",
        region_type: int = 10,
        rti_filters: Optional[List["RtiFilter"]] = None,
        postState: str = "New",
        start: Optional[str] = "2023-01-01",
        end: Optional[str] = "2023-02-01",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Job Posting Wages endpoint of the RTI Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/rti/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          rti_filters: List['RtiFilter']
            A list of the RtiFilter object, used to specify the filters to be
            used when running the query. See 'RtiFilter' for more information
            on how to use this feature.
          postState: str
            Defines the state of the posts to be returned, this could be "new"
            postings durning the timeframe specified, "open" postings, or a
            number of other options.
          start: str
            The starting timestamp of the queried postings, this parameter is
            overriden by 'timeframe'.
          end: str
            The ending timestamp of the queried postings, this parameter is
            overriden by 'timeframe'.
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

        # Timeframe has been removed due to start and end dates not being nullable

        analytic_id = "RealTimeIntelligenceWages"

        constructor = PayloadConstructor()

        constructor.add_regions(region, region_type)

        filter_obj: Dict[str, Any] = {"filters": []}
        if rti_filters:
            for filter in rti_filters:
                filter_obj["filters"].append(
                    {
                        "field": filter.field,
                        "key": filter.key,
                        "filterType": filter.filtertype,
                    }
                )
        constructor.payload |= filter_obj

        constructor.add_by_keyword(
            postState=postState,
            start=start,
            end=end,
        )

        response = EqRequest.run_v2_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.v2_core(response, as_frame)

    def resumes(
        self,
        region: str = "0",
        region_type: int = 10,
        rti_filters: Optional[List["RtiFilter"]] = None,
        includeSummary: bool = True,
        freetext: Optional[str] = None,
        locationMode: int = 0,
        entryWages: bool = True,
        experiencedWages: bool = False,
        wageType: str = "Annual",
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Resume Forensics endpoint of the RTI Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/resume-forensics/

        Args:
          region: str
            The FIPS code of the region to be queried, supplied as a string.
          region_type: int
            The JobsEQ type of the region FIPS code provided, ex: 1 == County.
          rti_filters: List['RtiFilter']
            A list of the RtiFilter object, used to specify the filters to be
            used when running the query. See 'RtiFilter' for more information
            on how to use this feature.
          includeSummary: bool
            Toggles if the query will return a set of summary tables to give
            an overview of the resumes returned in a region.
          freetext: str
            A freetext full-text keyword filter to apply to the job
            postings. Returns only postings containing this keyword.
          locationMode: int
            Controls if the query returns the region where the resume holder
            lives, works, or attended school. 1 = Live, 2 = Work, 4 = School.
          entryWages: bool
            Controls if entry wages are returned as a column for the query.
          experiencedWages: bool
            Controls if experienced entry wages are returned as a column for the query.
          wageType: str
            Controls if wages are returned as "Annual" or "Hourly".
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

        analytic_id = "Resumes"

        constructor = PayloadConstructor()

        constructor.add_by_keyword(
            entryWages=entryWages, experiencedWages=experiencedWages, wageType=wageType
        )
        constructor.nest_payload("options")
        constructor.add_regions(region, region_type)

        filter_obj: Dict[str, Any] = {"filters": []}
        if rti_filters:
            for filter in rti_filters:
                filter_obj["filters"].append(
                    {
                        "field": filter.field,
                        "key": filter.key,
                        "filterType": filter.filtertype,
                    }
                )
        constructor.payload |= filter_obj

        constructor.add_by_keyword(
            includeSummary=includeSummary, freetext=freetext, locationMode=locationMode
        )

        response = EqRequest.run_v2_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        return Parse.resumes(response, as_frame)
