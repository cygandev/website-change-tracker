import requests


def request_page_content(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/92.0.4515.107 Safari/537.36"
    }
    with requests.get(url, headers=headers) as r:
        page_content = r.text
    return page_content


def write_page_content(file_path: str, page_content: str) -> None:
    with open(file_path, "w") as f:
        f.write(page_content)
        return None


def read_page_content(file_path: str) -> None:
    with open(file_path, "r") as f:
        content = f.read()
        return content
