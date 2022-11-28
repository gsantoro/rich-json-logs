import json
import time

from rich.console import Console
from rich.table import Table, Column
from rich.live import Live
from rich.markup import escape

from jsonpath_ng import parse
from rich.prompt import Prompt

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
            col_name = col.strip()
            c = Column(col_name,
                       justify="left",
                       style="grey62",
                       overflow="fold")
            ans.append(c)
        return ans
    
    def parse_jsonpath(self, header, d):
        try:
            jsonpath_expression = parse(header)
            match = jsonpath_expression.find(d)
            v = escape(match[0].value)
            return v
        except Exception as e:
            return "-"
        
    def rows(self):
        line = self.input.readline()
        while line:
            try:
                d = json.loads(line)
                
                values = []
                for col in self.columns:
                    if str(col.header).startswith("$"):
                        v = self.parse_jsonpath(col.header, d)
                    elif col.header not in d:
                        v = "-"
                    else:
                        v = escape(d[col.header])
                    values.append(v)
                yield values
            except Exception as e:
                row = len(self.columns) * ["-"]
                row[-1] = line.strip()
                yield row
            line = self.input.readline()
        yield None

    def build_console(self):
        console = Console(highlighter=self.highlighter,
                          theme=self.theme,
                          force_terminal=True)
        return console
    
    def build_table(self):
        table = Table(*self.columns,
                      title=self.title,
                      highlight=True)
        return table

    def table_with_pager(self):
        table = self.build_table()
        console = self.build_console()
        
        for row in self.rows():
            if not row:
                break
            table.add_row(*row)
        
        with console.pager(styles=True):
            console.print(table)

    def live_table(self, sleep):        
        table = self.build_table()
        console = self.build_console()
        
        with Live(table, auto_refresh=False,
                  console=console,
                  vertical_overflow="visible") as l:    
            for row in self.rows():
                if not row:
                    break
                table.add_row(*row)
                time.sleep(sleep)
                l.refresh()
