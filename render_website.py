import argparse
import functools
import json
import math
import os

import more_itertools
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


def create_args_parser():
    description = 'The program creates a website'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--books_per_page',
                        metavar='[books per page]',
                        help='The number of books on a page, 15 by default',
                        default=15,
                        type=int,
                        )

    return parser


def rebuild_site(books_per_page):
    catalog_path = 'books_catalog.json'
    with open(catalog_path, 'r', encoding="UTF-8") as catalog_file:
        books_catalog = json.load(catalog_file)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    pages_path = 'pages'
    os.makedirs(pages_path, exist_ok=True)
    pages = more_itertools.chunked(books_catalog, books_per_page)
    pages_number = math.ceil(len(books_catalog) / books_per_page)
    columns_number = 2
    for page_number, page in enumerate(pages, start=1):
        chunk_number = math.ceil(len(page) / columns_number)
        books_columns = more_itertools.chunked(page, chunk_number)
        template = env.get_template('template.html')
        rendered_page = template.render(
            books_columns=books_columns,
            page_number=page_number,
            pages_number=pages_number,
        )

        file_name = f'index{page_number}.html'
        file_path = os.path.join(pages_path, file_name)
        with open(file_path, 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    args_parser = create_args_parser()
    args = args_parser.parse_args()
    rebuild_site_handler = functools.partial(
        rebuild_site,
        books_per_page=args.books_per_page,
    )
    rebuild_site_handler()
    server = Server()
    server.watch('./template.html', rebuild_site_handler)
    server.serve(root='.')


if __name__ == '__main__':
    main()
