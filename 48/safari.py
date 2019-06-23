import os
import urllib.request

LOG = os.path.join("/tmp", "safari.logs")
PY_BOOK, OTHER_BOOK = "🐍", "."
urllib.request.urlretrieve("http://bit.ly/2BLsCYc", LOG)


def create_chart():
    with open(LOG, newline="\n") as py_log:
        reader = py_log.readlines()
        lines = [line.strip() for line in reader]

    py_index = []

    for i, line in enumerate(lines, -1):
        if "sending to slack channel" in line:
            py_index.append(i)

    books = []

    for i in py_index:
        books.append(lines[i])

    dates = sorted(set([book.split()[0].lower() for book in books]))

    print(dates)

    for date in dates:
        print(date + " ", end="")
        for book in books:
            if date == book.split()[0]:
                if "Python" in book:
                    print(PY_BOOK, end="")
                else:
                    print(OTHER_BOOK, end="")
        print()


create_chart()
