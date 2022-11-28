
import sys
from rich_json_logs.log import ColoredLogs
import click
from rich_json_logs.highlighter import LogHighlighter, LogTheme

@click.command()
@click.option("-i", "--input-path", help="Input path")
@click.option("-c", "--columns", default="@timestamp, log.level, message", help="Columns to filter")
@click.option("--live/--no-live", default=False, help="Live streaming or static with pager")
@click.option("--sleep", default=0.4, help="Time to sleep between adding rows to live streaming")
def main(input_path, columns, live, sleep):    
    highlighter = LogHighlighter()
    theme = LogTheme
    
    if input_path is None:
        input_file = sys.stdin
    else:
        input_file = open(input_path, 'r')

    log = ColoredLogs("Logs", columns, input_file, highlighter, theme)
    
    if live:
        log.live_table(sleep)
    else:
        log.table_with_pager()

if __name__ == '__main__':
    main()