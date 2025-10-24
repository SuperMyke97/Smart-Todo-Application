import re
import fire
from date_parser import date_parsing

DATE_PATTERN = re.compile(r"([0-9]{4}-[0-1][0-9]-[0-3][0-9])|(tomorrow)|(next\s?week\s\w+)", re.I)
FREQUENCY_PATTERN = re.compile(r"every\s?(?P<freq>\w+)", re.I)
DURATION_PATTERN = re.compile(r"(\d+(min|hr|h|sec)?)(\s?)(\d+(min|sec))?(\s?)(\d+(sec))", re.I)
TIME_PATTERN = re.compile(r"(at|by)\s\d+(:\d+)?(pm|am)", re.IGNORECASE)
TAG_PATTERN = re.compile(r"@(?P<tag>(\w+))?")
PRIORITY_PATTERN = re.compile(r"#(?P<priority>(^(high|medium|low)$)|(\w+))?")
ASSIGNED_PATTERN = re.compile(r"\w+@\w+.\w+")


def regex_patterns(text: str) -> dict:
    data: dict = {}
    text = text.lower()
    # print(text)
    
    date = DATE_PATTERN
    if date.search(text) != None:
        date = date.search(text).group()
        data["due"] = date_parsing(date)
    else:
        data["due"] = "indefinte"

    frequency = FREQUENCY_PATTERN
    fs = frequency.search(text)
    if fs != None:
        if fs.group("freq")== "day":
            data["frequency"] = "Daily"
        elif fs.group("freq")== "month":
            data["frequency"] = "Monthly"
        else:
            data["frequency"] = "Weekly"
    else:
        data["frequency"] = "N/A"

    duration = DURATION_PATTERN
    if duration.search(text) != None:
        data["duration"] = duration.search(text).group()
    else:
        data["duration"] = "undecided"  

    time = TIME_PATTERN
    if time.search(text) != None:
        data["time"] = time.search(text).group()
    else:
        data["time"] = "whenever"  

    tag = TAG_PATTERN
    if tag.search(text) != None:
        data["tag"] = tag.search(text).group('tag')
    else:
        data["tag"] = "no tag"  

    priority = PRIORITY_PATTERN
    if priority.search(text) != None:
        data["priority"] = priority.search(text).group('priority')
    else:
        data["priority"] = "undefined" 

    assigned = ASSIGNED_PATTERN
    if assigned.search(text) != None:
        data["assigned"] = assigned.search(text).group()
    else:
        data["assigned"] = "To Me"

    return data


if __name__ == '__main__':
    fire.Fire(serialize=False)
