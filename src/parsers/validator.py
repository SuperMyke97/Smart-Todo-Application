import re
import fire
from regex_patterns import DATE_PATTERN, FREQUENCY_PATTERN, DURATION_PATTERN, TIME_PATTERN, TAG_PATTERN, PRIORITY_PATTERN, ASSIGNED_PATTERN 

    
def is_date(date: str)->bool:    
    """Returns True if the date matches the pattern, False otherwise."""
    return re.match(DATE_PATTERN, date) is not None

def is_frequency(frequency: str)->bool:    
    """Returns True if the frequency matches the pattern, False otherwise."""
    return re.match(FREQUENCY_PATTERN, frequency) is not None

def is_duration(duration: str)->bool:    
    """Returns True if the duration matches the pattern, False otherwise."""
    return re.match(DURATION_PATTERN, duration) is not None

def is_time(time: str)->bool:    
    """Returns True if the time matches the pattern, False otherwise."""
    return re.match(TIME_PATTERN, time) is not None

def is_tag(tag: str)->bool:    
    """Returns True if the tag matches the pattern, False otherwise."""
    return re.match(TAG_PATTERN, tag) is not None

def is_priority(priority: str)->bool:    
    """Returns True if the priority matches the pattern, False otherwise."""
    return re.match(PRIORITY_PATTERN, priority) is not None

def is_assigned(assigned: str)->bool:    
    """Returns True if the assigned matches the pattern, False otherwise."""
    return re.match(ASSIGNED_PATTERN, assigned) is not None


if __name__ == '__main__':
    fire.Fire(serialize=False)
