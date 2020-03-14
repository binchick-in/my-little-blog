import os
import pathlib
import markdown


def generate_post_content():
    md = markdown.Markdown(extensions = ['full_yaml_metadata', 'fenced_code'])
    current_path = pathlib.Path(__file__).parent.absolute()
    post_path = f'{current_path}/posts'
    posts_list = []

    for post_file in os.listdir(post_path):
        post_obj = {}
        post_file_path = f'{post_path}/{post_file}'
        with open(post_file_path, 'r') as f:
            post_obj['body'] = md.convert(f.read())
            post_obj.update(md.Meta)
            posts_list.append(post_obj)
    return posts_list


def generate_page_content():
    md = markdown.Markdown(extensions = ['full_yaml_metadata'])
    current_path = pathlib.Path(__file__).parent.absolute()
    pages_path = f'{current_path}/pages'
    page_list = []


    for page_file in os.listdir(pages_path):
        page_obj = {}
        page_file_path = f'{pages_path}/{page_file}'
        with open(page_file_path, 'r') as f:
            page_obj['body'] = md.convert(f.read())
            page_obj.update(md.Meta)
            page_list.append(page_obj)
    return page_list


if __name__ == '__main__':
    # print(generate_page_content())
    print(generate_post_content())
