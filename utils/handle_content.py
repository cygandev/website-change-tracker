from urllib.parse import urlparse

import requests
from requests_ip_rotator import ApiGateway


def request_page_content(url: str, headers: dict) -> str:
    """Makes request to an url and returns its content

    Args:
        url (str): url of webpage
        headers (dict): request header

    Returns:
        str: text content of webpage
    """
    with requests.get(url, headers=headers) as r:
        r.raise_for_status()
        page_content = r.text
    return page_content


def request_page_content_hide_ip(
    url: str, headers: dict, aws_regions: list = ["eu-central-1"]
) -> str:
    """Makes request to an url and returns its content.
        Uses AWS API Gateway as proxy, resulting in different IP each request.
        Requires AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID as ENV variables.

    Args:
        url (str): url of webpage
        headers (dict): request header
        aws_regions (list, optional): AWS region to use for IP pool. Defaults to ["eu-central-1"].

    Returns:
        str: text content of webpage
    """

    url_schema = urlparse(url).scheme
    url_home = urlparse(url).netloc
    url_base = f"{url_schema}://{url_home}"
    with ApiGateway(url_base, regions=aws_regions) as g:
        session = requests.Session()
        session.mount(url_base, g)
        response = session.get(url, headers=headers)
        response.raise_for_status()
        return response.text


def write_page_content(file_path: str, page_content: str) -> None:
    """Writes text to a file.

    Args:
        file_path (str): file path
        page_content (str): text to be written to file

    Returns:
        _type_: _description_
    """
    with open(file_path, "w") as f:
        f.write(page_content)
        return None


def read_page_content(file_path: str) -> None:
    """Returns content of a file

    Args:
        file_path (str): file path

    Returns:
        _type_: content of file as text
    """
    with open(file_path, "r") as f:
        content = f.read()
        return content
