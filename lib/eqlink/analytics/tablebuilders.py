from typing import Union, Dict, Optional, List, Any
from eqlink.utilities.constructors import DataFetchConstructor
from eqlink.utilities.general import EqRequest
import pandas as pd
import json


class DfField:

    def __init__(
        self,
        field: str,
        date: Optional[str] = None,
        interval: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> None:
        """This class is used to instantiate DfField "Field" instances.

        This class is used to instantiate DfField "Field" instances. These
        instances can be used to add fields to your DataFetch api queries. Bt
        adding multiple "Field" instances you can build up complex DataFetch
        tables, yeilding the same results you can expect from the JobsEQ SaaS.

        Attributes:
            field: str
                The field to be accessed by this instance of the DfField class,
                ex: 'empl_placeOfWork'.
            date: str
                The date to be used to by this field, ex: '2020-01-01'.
            interval: str
                The interval in which the data will be accessed,
                ex: 'Quarterly'
            offset: int
                The date offset used by the DataFetch class to build large
                tables.
        """

        self.field = field
        self.date = date
        self.interval = interval
        self.offset = offset

    def __repr__(self) -> str:
        body: Dict[str, Any] = {
            "field": self.field,
            "timePoints": [{"date": self.date, "interval": self.interval}],
        }

        if self.offset:
            body["timePoints"][0]["offset"] = self.offset

        return json.dumps(body)


class DataFetch:
    """This class contains all JobsEQ DataFetch Analytics.

    This class serves as a container for every JobsEq DataFetch analytic, such
    as Occupation DataFetch. In the future Demographic DataFetch and other
    DataFetch features might be added to this class.

    Attributes:
        token: str
            A string containing the JobsEq authentication token.
    """

    def __init__(self, token):
        self.token = token

    def occupation(
        self,
        region: str = "0",
        region_type: int = 10,
        sub_region_level: Optional[int] = None,
        soc_code: str = "00-0000",
        soc_type: int = 0,
        sub_soc_level: Optional[int] = 2,
        fields: List["DfField"] = [
            DfField("empl_placeOfWork", "2020-01-01", "Quarterly")
        ],
        pageKey: Optional[int] = None,
        pageSize: int = 1000,
        as_frame: bool = False,
    ) -> Union[Any, pd.DataFrame]:
        """Runs the Occupation DataFetch Analytic.

        Further documentation on this analytic, its datasources, and the
        underlying model can be found at the following documentation
        link https://help.eqsuite.com/analytics/data-fetch/

        Args:
            region: str
                The FIPS code of the region to be queried, supplied as a string.
            region_type: int
                The JobsEQ type of the region FIPS code provided, ex: 1 == County.
            soc_code: str
                The SOC code of the region to be queried, supplied as a string.
            soc_type: int
                The JobsEQ type of the SOC code provided, ex: 7 == detailed group.
            sub_soc_level: str
                The sub-level of the query, for example, if you query a 2-digit soc
                and then set occ_level to 3-digit, you'll receive all 3-digit SOC
                codes under that 2-digit code.
            fields: list of DfField
                The fields to be returned by the query, as defined by the DfField
                instances contained in the fields list.
            pageKey: int
                An optional control for the key of the query, sets the starting
                row for query offsets.
            pageSize: int
                A control for the size of the return, limited to 100 by
                default.
            as_frame: bool
                This value controls the return type of this function, setting
                to True returns a dataframe, False (default) returns a dictionary.

        Returns:
            A list containing datafetch responses.

        Raises:
            Not implimented error: For dataframes.
        """

        analytic_id = "Datafetch/Occupation"

        constructor = DataFetchConstructor()

        constructor.add_df_regions(region, region_type, sub_region_level)
        constructor.add_df_occupations(soc_code, soc_type, sub_soc_level)

        filter_obj: Dict[str, Any] = {"fields": []}
        if fields:
            for filter in fields:
                if filter.date or filter.interval:
                    body: Dict[str, Any] = {
                        "field": filter.field,
                        "timepoints": [
                            {"date": filter.date, "interval": filter.interval}
                        ],
                    }

                if not filter.date or not filter.interval:
                    body = {
                        "field": filter.field,
                        "timepoints": [],
                    }

                if filter.offset:
                    body["timePoints"][0]["offset"] = filter.offset

                filter_obj["fields"].append(body)

        constructor.payload |= filter_obj

        constructor.add_by_keyword(pageKey=pageKey, pageSize=pageSize)

        response = EqRequest.run_v2_analytic(
            self.token, analytic_id, constructor.send_to_json()
        )

        if as_frame:
            return pd.DataFrame.from_dict(response["data"])

        return response["data"]
