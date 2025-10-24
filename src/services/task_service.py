import re
import fire
from dateutil.parser import parse
from datetime import datetime

data=[{'due':       '2025-10-20',
      'Frequency': 'N/A',
    'Duration':  'undecided',
    'time':      'whenever',
    'tag':       'work',
    'Priority':  'high',
    'task_metadata': ['2', 'at 2pm', '@work', 'call doctor tomorrow'], 
    'Assigned':  'alice_1@example.com'},
    {'Duration': ' undecided',
     'time':      'whenever',
     'tag':       'work',
     'Priority':  'high',
     'Assigned':  'alice_1@example.com'}]




def search(pattern: str, data: list[dict]= data):
    count = 0
    key = ''
    if data:
        for task in data:
            for k, wordval in task.items():
                                
                if type(wordval) != list and pattern.find(wordval)>=0:
                    key = k
                if type(wordval) == list and pattern in wordval:
                    due = False                      
                    for subword in wordval:
                        # print(subword)
                        if re.fullmatch(pattern=pattern, string=subword):
                            count+=1
                if pattern.find(k)>=0:
                    key = k
                    due = True
                    wordval = parse(wordval)
                    # print(type(wordval))
                    str_date=wordval.strftime("%B %Y,")
                    # print(str_date)
                    count+=1
                    
        if due:
            print(f"Found {count} tasks with {key} {str_date}...")
        else:
            print(f"Found {count} tasks with {key} {pattern}...")


if __name__ == '__main__':
    fire.Fire()
    
