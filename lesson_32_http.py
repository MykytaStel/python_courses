import json
from typing import Optional
from requests import Response, get

URL = "https://api.pushshift.io/reddit/comment/search/"
UNDEFINED = 'undefined'


def get_response(url) -> Optional[Response]:
    try:
        return get(url)
    except ConnectionError:
        print(f"Can't connect to {url}")
        return


def get_from_payload(data: dict, param_string: str, def_param: str) -> str:
    return data.get(param_string, def_param)


def parse_data(payload_data: dict) -> dict:
    time = get_from_payload(payload_data, 'created_utc', UNDEFINED)
    text = get_from_payload(payload_data, 'body', UNDEFINED)
    return {time: text}


def save_to_file(payload: dict, file_name: str) -> None:
    with open(file_name, 'w+') as f:
        if 'data' not in payload:
            return

        for data in payload['data']:
            json.dump(parse_data(data), f, sort_keys=True, indent=4)


def handle_payload(response: Optional[Response]) -> None:
    if not response:
        print("Empty response")
    elif response.status_code != 200:
        print("Status is not 200")

    try:
        payload = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        print(f'Error is - {response.text}')

    save_to_file(payload, 'comments.json')


if __name__ == '__main__':
    result = get_response(URL)
    handle_payload(result)

