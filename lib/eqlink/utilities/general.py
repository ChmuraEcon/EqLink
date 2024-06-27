from typing import Optional, Union, Dict, List, Any
import requests as rq
import json


class EqRequest:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_token(username: str, password: str) -> Any:

        endpoint = "http://jobseq.eqsuite.com/token"
        paramstr = (
            f"grant_type=password&username={username}&password={password}".encode(
                "utf-8"
            )
        )
        headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

        request = rq.PreparedRequest()
        request.prepare(method="POST", url=endpoint, headers=headers, data=paramstr)

        with rq.session() as session:
            response = session.send(request)

        return json.loads(response.content)["access_token"]

    @staticmethod
    def send_request(
        auth_token: str,
        method: str,
        target: str,
        type_filter: Optional[Union[int, List[int]]] = None,
        data: Optional[Dict[str, str]] = {},
    ) -> rq.Response:

        url = f"http://jobseq.eqsuite.com/api/External/{target}"
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json",
        }
        if type_filter:
            url += f"?type={type_filter}"
        request = rq.PreparedRequest()

        if data is not None:
            request.prepare(method=method, url=url, headers=headers, data=data)
        else:
            request.prepare(method=method, url=url, headers=headers)
        try:
            with rq.session() as session:
                response = session.send(request)
        except rq.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
        except rq.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except rq.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except rq.exceptions.RequestException as err:
            print(f"Other Error {err}")
        if response.status_code == 401:
            raise rq.HTTPError(f"Code {response.status_code}: Bad Token")
        elif response.status_code != 200:
            raise rq.HTTPError(f"{response.status_code}: Bad Request")

        return response

    @staticmethod
    def run_analytic(
        auth_token: str,
        analytic_id: str,
        request_body: Dict[str, str],
    ) -> Any:

        response = EqRequest.send_request(
            auth_token, "POST", f"runanalytic?id={analytic_id}", data=request_body
        )

        return json.loads(response.content)

    @staticmethod
    def run_v2_analytic(
        auth_token: str,
        v2_endpoint: str,
        request_body: Dict[str, str],
    ) -> Any:

        response = EqRequest.send_request(
            auth_token, "POST", v2_endpoint, data=request_body
        )

        return json.loads(response.content)
