from typing import Optional, Dict, Any, Union
import pandas as pd
import json


class Parse:

    def __init__(self) -> None:
        pass

    @staticmethod
    def core_analytic(response, as_frame: Optional[bool] = False):
        table = []
        columns = response["table"]["columns"]
        rows = response["table"]["rows"]
        headers = [column["name"] for column in columns]

        for row in rows:
            row_values = []
            for value in row:
                if type(value) is not dict:
                    row_values.append(value)
                elif type(value) is dict:
                    if "displayText" in value:
                        row_values.append(value["displayText"])
                    elif "displayValue" in value:                        
                        row_values.append(value["displayValue"])
                    elif "code" in value:
                        row_values.append(value["code"])                                        
                    else:
                        raise ValueError
            table.append(row_values)

        dict_table = {}

        for header in headers:
            values = [array[headers.index(header)] for array in table]
            if header:
                dict_table[header] = values

        if as_frame:
            return pd.DataFrame.from_dict(dict_table)

        return dict_table

    @staticmethod
    def maps(response, as_frame: Optional[bool] = False):
        table = []
        columns = response["map"]["map"]["columns"]
        rows = response["map"]["map"]["rows"]
        headers = [column["name"] for column in columns]
        headers[0] = "RegionFIPS"

        if headers[1] is None:
            headers[1] = response["map"]["map"]["titleCaption"]

        for row in rows:
            row_values = []
            for value in row:
                if type(value) is not dict:
                    row_values.append(value)
                elif type(value) is dict:
                    if "displayText" in value:
                        row_values.append(value["displayText"])
                    elif "code" in value:
                        row_values.append(value["code"])
                    else:
                        def parse_nested_dict(d):
                            if "displayText" in d:
                                return d["displayText"]
                            elif "code" in d:
                                return d["code"]
                            else:
                                return {k: parse_nested_dict(v) if isinstance(v, dict) else v for k, v in d.items()}

                        row_values.append(parse_nested_dict(value))
            table.append(row_values)

        dict_table = {}

        for header in headers:
            values = [array[headers.index(header)] for array in table]
            if header:
                dict_table[header] = values

        if as_frame:
            return pd.DataFrame.from_dict(dict_table)

        return dict_table

    @staticmethod
    def demo_current(response, as_frame: Optional[bool] = False):
        vars = []
        vals = []
        prcs = []

        for section in response["table"]["sections"]:
            for row in section["rows"]:
                vars.append(row[0]["displayText"])
                vals.append(row[2]["value"])
                prcs.append(row[1])

        table = {"Demographic": vars, "Value": vals, "Percentage": prcs}

        if as_frame:
            return pd.DataFrame.from_dict(table)

        return table

    @staticmethod
    def list_availible(
        unparsed_response: bytes, analytic_prefix: str, as_frame: Optional[bool] = False
    ) -> Union[Any, pd.DataFrame]:
        analytic_list = {}

        for item in json.loads(unparsed_response):
            if analytic_prefix in ("reg", "occ", "ind"):
                analytic_list[item["c"]] = item["t"], item["d"]
            if analytic_prefix in ("cip", "dem"):
                analytic_list[item["c"]] = item["d"]
            if analytic_prefix in ("ana"):
                analytic_list[item["id"]] = item["name"]

        if as_frame:
            frame = pd.DataFrame.from_dict(analytic_list, "index")
            frame.reset_index(inplace=True)
            frame.rename(
                columns={
                    "index": f"{analytic_prefix}_code",
                    0: f"{analytic_prefix}_type",
                    1: f"{analytic_prefix}_description",
                },
                inplace=True,
            )
            return frame

        return analytic_list

    @staticmethod
    def labor_wage_trends(response, as_frame: Optional[bool] = False):
        table = {}
        headers = []

        try:
            headers = [
                "Date",
                response["chart"]["subTitle"][0] + response["chart"]["yAxis"]["title"],
            ]
        except KeyError:
            headers = ["Date", response["chart"]["title"]]

        for i in range(2):
            table[headers[i]] = [
                datarow[i] for datarow in response["chart"]["series"][0]["data"]
            ]

        if as_frame:
            frame = pd.DataFrame.from_dict(table)
            frame["Date"] = pd.to_datetime(frame["Date"], unit="ms")
            return frame

        return table

    @staticmethod
    def type_availible(
        unparsed_response: bytes, analytic_name: str, as_frame: Optional[bool] = False
    ):
        decoded_response = json.loads(unparsed_response)
        analytic_list = {}
        for item in decoded_response:
            analytic_list[item["id"]] = item["name"]
        if as_frame:
            frame = pd.DataFrame.from_dict(analytic_list, "index")
            frame.reset_index(inplace=True)
            frame.rename(
                columns={"index": f"{analytic_name}_id", 0: f"{analytic_name}_name"},
                inplace=True,
            )
            return frame

        return analytic_list

    @staticmethod
    def v2_core(response, as_frame: Optional[bool] = False):
        parsed_dict: Dict[str, list[str]] = {}
        headers = list(response["data"][0].keys())

        for header in headers:
            databody = []
            for row in response["data"]:
                databody.append(row[header])
            parsed_dict |= {header: databody}

        if as_frame:
            return pd.DataFrame.from_dict(parsed_dict)

        return parsed_dict

    @staticmethod
    def v2_core_rti_overtime(response, as_frame: Optional[bool] = False):
        parsed_dict: Dict[str, list[str]] = {}
        headers = list(response["data"][0]["series"][0].keys())

        for header in headers:
            databody = []
            for row in response["data"][0]["series"]:
                databody.append(row[header])
            parsed_dict |= {header: databody}

        if as_frame:
            df = pd.DataFrame.from_dict(parsed_dict)
            df["date"] = pd.to_datetime(df["date"], unit="ms")
            return df

        return parsed_dict

    @staticmethod
    def resumes(results, as_frame: Optional[bool] = False):
        categories = []
        labels = []
        counts = []
        values = []

        for subtable in results["tables"]:
            category = subtable["category"]
            for valueset in subtable["rows"]:
                if valueset["label"] == "Unclassified":
                    continue
                categories.append(category)
                labels.append(valueset["label"])
                counts.append(valueset["count"])
                values.append(valueset["entryWages"])

        parsed_table = {
            "Category": categories,
            "Label": labels,
            "Counts": counts,
            "Entry Wages": values,
        }

        if as_frame:
            return pd.DataFrame.from_dict(parsed_table)

        return parsed_table
