from html.parser import HTMLParser


class HTMLTable(HTMLParser):
    def __init__(self):
        self.tables = []
        self.table = None
        self.tag = None
        self.row = None
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.table = []
        elif tag == "tr":
            self.row = []
        self.tag = tag

    def handle_endtag(self, tag):
        self.tag = None
        if tag == "tr":
            self.table.append(self.row)
        elif tag == "table":
            self.tables.append(self.table)

    def handle_data(self, data):
        if self.tag == "td":
            self.row.append(data)


def read_file(filename: str):
    with open(filename, "rt", encoding="utf8") as fo:
        s = fo.read()
    parser = HTMLTable()
    parser.feed(s)
    return parser.tables[0]
