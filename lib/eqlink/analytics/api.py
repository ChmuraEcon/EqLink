from typing import Union, Dict, Optional, List, Any
from eqlink.utilities.parsers import Parse
from eqlink.utilities.general import EqRequest
import pandas as pd
import json


class ApiSpecificTools:
    def __init__(self, token) -> None:
        self.token = token

    def list_availible(
        self,
        category: str,
        category_type: Optional[Union[int, List[int]]] = 0,
        as_frame: Optional[bool] = False,
    ) -> Union[pd.DataFrame, Dict[str, str]]:

        response = EqRequest.send_request(self.token, "GET", category, category_type)

        return Parse.list_availible(response.content, category[:3], as_frame)

    def list_availible_types(
        self,
        category: str,
        as_frame: Optional[bool] = False,
    ) -> Union[Any, pd.DataFrame]:

        request_target = f"{category}Types"

        response = EqRequest.send_request(self.token, "GET", request_target)

        return Parse.type_availible(response.content, request_target, as_frame)

    def list_availible_schools(
        self,
        region_code: str,
        region_type: Optional[Union[int, List[int]]] = 0,
        as_frame: Optional[bool] = False,
    ) -> Union[Any, pd.DataFrame]:

        response = EqRequest.send_request(
            self.token, "GET", f"SchoolsForRegion?type={region_type}&code={region_code}"
        )

        if as_frame:
            pd.DataFrame.from_dict(json.loads(response.content))

        return json.loads(response.content)
