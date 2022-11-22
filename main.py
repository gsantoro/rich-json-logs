
import sys
from src.log import ColoredLogs
import click
from src.highlighter import LogHighlighter, LogTheme

@click.command()
@click.option("-i", "--input-path", help="Input path")
def main(input_path):    
    highlighter = LogHighlighter()
    theme = LogTheme
    
    if input_path is None:
        input_file = sys.stdin
    else:
        input_file = open(input_path, 'r')

    log = ColoredLogs("Logs", "@timestamp, log.level, message", input_file, highlighter, theme)
    log.process()

    # input_file.close()

if __name__ == '__main__':
    main()