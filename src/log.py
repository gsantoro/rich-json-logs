import json
import time

from rich.console import Console
from rich.table import Table, Column
from rich.markup import escape

class ColoredLogs:
    def __init__(self, title, columns, input, highlighter, theme):
        self.title = title
        self.columns = self.get_cols(columns)
        self.input = input
        self.highlighter = highlighter
        self.theme = theme

    def get_cols(self, columns):
        parts = columns.split(",")
        ans = []
        for col in parts:
            col = col.strip()
            c = Column(col, justify="left", style="grey62", overflow="fold")
            ans.append(c)
        return ans

    def process(self):
        table = Table(*self.columns, title=self.title, highlight=True)

        line = self.input.readline()
        while line:
            d = json.loads(line)

            values = []
            for col in self.columns:
                v = escape(d[col.header])

                values.append(v)

            table.add_row(*values)

            line = self.input.readline()

        console = Console(highlighter=self.highlighter, theme=self.theme)
        with console.pager(styles=True):
            console.print(table)
