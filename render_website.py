import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


def rebuild_site():
    catalog_path = 'books_catalog.json'
    with open(catalog_path, 'r', encoding="UTF-8") as catalog_file:
        books_catalog = json.load(catalog_file)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(books_catalog=books_catalog)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    rebuild_site()
    server = Server()
    server.watch('./template.html', rebuild_site)
    server.serve(root='.')


if __name__ == '__main__':
    main()
