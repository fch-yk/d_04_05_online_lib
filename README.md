# Library

The program parses [tululu.org](https://tululu.org/) library and creates its own offline website.

## Prerequisites

Python 3.10 or higher required.

## Installing

- Download the project files
- Run:

```bash
pip install -r requirements.txt
```

## Running scripts

### Parsing

- Run:

```bash
python parse_tululu_category.py
```

- It's possible to input the start and end book ID.
For example, to download books with IDs from 21 to 23, run:

```bash
python parse_tululu_category.py --start_page 21 --end_page 24
```

- You can input destination folder and JSON books catalog file paths,
skip downloading images or texts; to find out more, run:

```bash
python parse_tululu_category.py -h
```

### Creating a website

- Run:

```bash
python render_website.py
```

- You can specify the number of books per page:

```bash
python render_website.py --books_per_page 9
```

The number of books per page by default is 15.

- To find out more, run:

```bash
python send-minechat.py -h
```

- You can go to an [example of the working site](https://yefimkorshever.github.io/d_04_05_site/).



## Project goals

The project was created for educational purposes.
It's a lesson for python and web developers at [Devman](https://dvmn.org).
