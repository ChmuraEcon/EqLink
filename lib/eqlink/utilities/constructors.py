import json
from typing import Optional, Dict


class PayloadConstructor:
    def __init__(self):
        self.payload = {}

    def __repr__(self):
        payload = json.dumps(self.payload)

        return payload

    def add_region(self, region: str, region_type: int):
        data = {"region": {"code": region, "type": region_type}}
        self.payload = self.payload | data

        return

    def add_regions(self, region: str, region_type: int):
        data = {"regions": [{"code": region, "type": region_type}]}
        self.payload = self.payload | data

        return

    def add_regionFilter(self, region: str, region_type: int):
        data = {"regionFilter": {"code": region, "type": region_type}}
        self.payload = self.payload | data

        return

    def add_occupation(self, soc_code: str, soc_type: int):
        data = {"occupation": {"code": soc_code, "type": soc_type}}
        self.payload = self.payload | data

        return

    def add_occupations(self, soc_code: str, soc_type: int):
        data = {"occupations": [{"code": soc_code, "type": soc_type}]}
        self.payload = self.payload | data

        return

    def add_rti_occupation(self, soc_code: str, soc_type: int):
        data = {"rtiOccupation": {"code": soc_code, "type": soc_type}}
        self.payload = self.payload | data

        return

    def add_industry(self, ind_code: str, ind_type: int):
        data = {"industry": {"code": ind_code, "type": ind_type}}
        self.payload = self.payload | data

        return

    def add_cip(self, cip_code: str, cip_type: int):
        data = {"cip": {"code": cip_code, "type": cip_type}}
        self.payload = self.payload | data

        return

    def add_cipsoc(self, cip_code: str, cip_type: int):
        data = {"cipSoc": {"code": cip_code, "type": cip_type}}
        self.payload = self.payload | data

        return

    def add_skill(self, skill_code: str, skill_type: int):
        data = {"skill": {"code": skill_code, "type": skill_type}}
        self.payload = self.payload | data

        return

    def add_by_keyword(self, **kwargs):
        data = kwargs
        self.payload = self.payload | data

        return

    def add_impact_region(self, impact_region: str, impact_region_type: int):
        data = {"impactRegion": {"code": impact_region, "type": impact_region_type}}
        self.payload = self.payload | data

        return

    def add_event_region(self, event_region: str, event_region_type: int):
        data = {"eventRegion": {"code": event_region, "type": event_region_type}}
        self.payload = self.payload | data

        return

    def add_rti_filter(self, field, key, filtertype):
        data = {"filters": [{"field": field, "key": key, "filterType": filtertype}]}
        self.payload = self.payload | data

        return

    def add_rti_filter_empty(self):
        data: Dict[str, list[str]] = {"filters": []}
        self.payload = self.payload | data

        return

    def nest_payload(self, nest_key):
        data = {nest_key: self.payload}
        self.payload = data

        return

    def send_to_json(self):
        payload = json.dumps(self.payload)

        return payload


class DataFetchConstructor:
    def __init__(self):
        self.payload = {}

    def __repr__(self):
        payload = json.dumps(self.payload)

        return payload

    def add_df_regions(self, region, region_type, sub_region_level):
        if not sub_region_level:
            sub_region_level = region_type

        payload = {
            "regions": [
                {
                    "parent": {"code": region, "type": region_type},
                    "level": sub_region_level,
                }
            ]
        }

        self.payload |= payload

        return

    def add_df_occupations(self, soc_code, soc_type, sub_soc_level):
        if not sub_soc_level:
            sub_soc_level = soc_type

        payload = {
            "occupations": [
                {"parent": {"code": soc_code, "type": soc_type}, "level": sub_soc_level}
            ]
        }

        self.payload |= payload

        return

    def add_df_fields(
        self,
        fields: Optional[list[str]],
        fields_timepoint: Optional[list[Dict[str, object]]],
    ):
        payload: Dict[str, list[Dict[str, object]]] = {"fields": []}

        if fields:
            for field in fields:
                payload["fields"].append({"field": field})

        if fields_timepoint:
            for field_dict in fields_timepoint:
                payload["fields"].append(field_dict)

        self.payload |= payload

        return

    def add_by_keyword(self, **kwargs):
        data = kwargs
        self.payload = self.payload | data

        return

    def send_to_json(self):
        payload = json.dumps(self.payload)

        return payload
