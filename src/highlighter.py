from rich.highlighter import RegexHighlighter
from rich.theme import Theme


class LogHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "logs."
    highlights = [r"(?P<error>(warn|error))|(?P<info>(info))"]

LogTheme = Theme({
    "logs.error": "red1",
    "logs.info": "sky_blue3",
})
