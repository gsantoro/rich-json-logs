

import json
import time

from rich.console import Console
from rich.table import Table
from rich.live import Live

class ColoredLogs:
    def __init__(self, columns, in_file, out_file):
        self.columns = self.get_cols(columns)
        self.in_file = in_file
        self.out_file = out_file

    def get_cols(self, columns):
        parts = columns.split(",")
        return [col.strip() for col in parts]

    def process(self):
        table = Table(title="Leetcode")

        table.add_column("Id", justify="left", style="light_sea_green", no_wrap=True)
        table.add_column("Title", style="grey62")

        with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
            line = self.in_file.readline()
            count = 0
            while line:
                d = json.loads(line)

                obj = {}
                for col in self.columns:
                    obj[col] = d[col]

                time.sleep(0.4)
                table.add_row(*obj.values())
                count += 1

                if count > 20:
                    break

                # ans = json.dumps(obj)

                # self.out_file.write(ans)
                # self.out_file.write("\n")

                line = self.in_file.readline()

            # console = Console()
            # console.print(table)
