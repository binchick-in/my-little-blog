import os
import pathlib
import markdown


def generate_page_content():
    md = markdown.Markdown(extensions = ['full_yaml_metadata'])
    current_path = pathlib.Path(__file__).parent.absolute()
    pages_path = f'{current_path}/pages'
    page_objects = {}


    for page_file in os.listdir(pages_path):
        page_file_path = f'{pages_path}/{page_file}'
        with open(page_file_path, 'r') as f:
            md_body = md.convert(f.read())
            md_meta = md.Meta
            md_path = md_meta.get('path')
        page_objects.setdefault(md_path, {})
        page_objects[md_path]['meta'] = md_meta
        page_objects[md_path]['body'] = md_body

    return page_objects


if __name__ == '__main__':
    print(generate_page_content())
