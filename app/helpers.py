import os
import json
import pathlib
import markdown
import flask
from datetime import datetime
from flask import request

from app.models import InboundRequest
from app.models import db


def request_logger(req: flask.Request) -> bool:
    req_args = json.dumps({k: v for k, v in req.args.items()})
    new_inbound_request = InboundRequest(
        ip_addr=req.headers.get("X-Forwarded-For"),
        user_agent=req.headers.get("User-Agent"),
        referer=req.headers.get("Referer"),
        url_path=req.path,
        request_args=req_args,
        time_of_request=datetime.today(),
    )
    db.session.add(new_inbound_request)
    db.session.commit()
    return True


def generate_post_content():
    md = markdown.Markdown(extensions=["full_yaml_metadata", "fenced_code"])
    current_path = pathlib.Path(__file__).parent.absolute()
    post_path = f"{current_path}/posts"
    posts_list = []

    for post_file in os.listdir(post_path):
        post_obj = {}
        post_file_path = f"{post_path}/{post_file}"
        with open(post_file_path, "r") as f:
            post_obj["body"] = md.convert(f.read())
            post_obj.update(md.Meta)
            posts_list.append(post_obj)
    return posts_list


def generate_page_content():
    md = markdown.Markdown(extensions=["full_yaml_metadata", "fenced_code"])
    current_path = pathlib.Path(__file__).parent.absolute()
    pages_path = f"{current_path}/pages"
    page_list = []

    for page_file in os.listdir(pages_path):
        page_obj = {}
        page_file_path = f"{pages_path}/{page_file}"
        with open(page_file_path, "r") as f:
            page_obj["body"] = md.convert(f.read())
            page_obj.update(md.Meta)
            page_list.append(page_obj)
    return page_list


if __name__ == "__main__":
    # print(generate_page_content())
    print(generate_post_content())
