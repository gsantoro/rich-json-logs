
import sys
from rich_json_logs.log import ColoredLogs
import click
from rich_json_logs.highlighter import LogHighlighter, LogTheme

@click.command()
@click.option("-i", "--input-path", help="Input path")
@click.option("-c", "--columns", default="@timestamp, log.level, message", help="Columns to filter")
def main(input_path, columns):    
    highlighter = LogHighlighter()
    theme = LogTheme
    
    if input_path is None:
        input_file = sys.stdin
    else:
        input_file = open(input_path, 'r')

    log = ColoredLogs("Logs", columns, input_file, highlighter, theme)
    log.process()

if __name__ == '__main__':
    main()
