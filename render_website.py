import json
import os

import more_itertools
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


def rebuild_site():
    catalog_path = 'books_catalog.json'
    with open(catalog_path, 'r', encoding="UTF-8") as catalog_file:
        books_catalog = json.load(catalog_file)

    for book_card in books_catalog:
        book_card['img_src'] = ''.join(['.', book_card['img_src']])

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    pages_path = 'pages'
    os.makedirs(pages_path, exist_ok=True)
    books_per_page = 10
    pages = more_itertools.chunked(books_catalog, books_per_page)
    columns_number = 2
    for page_number, page in enumerate(pages, start=1):
        book_cards_number = len(page)
        chunk_number = book_cards_number // columns_number
        chunk_number += book_cards_number % columns_number
        books_columns = more_itertools.chunked(page, chunk_number)
        template = env.get_template('template.html')
        rendered_page = template.render(books_columns=books_columns)

        file_name = f'index{page_number}.html'
        file_path = os.path.join(pages_path, file_name)
        with open(file_path, 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    rebuild_site()
    server = Server()
    server.watch('./template.html', rebuild_site)
    server.serve(root='.')


if __name__ == '__main__':
    main()
