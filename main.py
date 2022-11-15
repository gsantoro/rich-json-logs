
import sys
from src.log import ColoredLogs
import os


log_file = "data/algorithms.json"
stdout = sys.stdout


with open(log_file, 'r') as f_in:
    log = ColoredLogs("id, title", f_in, stdout)
    log.process()
