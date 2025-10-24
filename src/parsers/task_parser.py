import re
import typer
from regex_patterns import regex_patterns

app = typer.Typer()

@app.command()
def add(text: str):
    
    text = text.lower()
    data: dict = regex_patterns(text)
    data["full_task"] = text
    text_list = text.split(" ")
    task_metadata = []

    patterns = [re.compile(r"due:(([0-9]{4}-[0-1][0-9]-[0-3][0-9])|(tomorrow)|(next\s?week\s\w+))", re.I), 
                re.compile(r"every\s?([a-zA-Z]+)", re.I), 
                re.compile(r"(\d+(min|hr|h|sec)?)(\s?)(\d+(min|sec))?(\s?)(\d+(sec))?", re.I),
                re.compile(r"(#[a-zA-Z]+)"),
                re.compile(r"((at|by)\s\d+(:\d+)?(pm|am))"),
                re.compile(r"(@[a-zA-Z]+)", re.I),
                re.compile(r"([a-zA-Z]+:\w+@\w+.com)", re.I)]


    for p in patterns:
        if p.search(text)!= None:
            subword = p.search(text).group().strip()
            task_metadata.append(subword)
            
            if ' ' in subword:
                for a in subword.split(' '): 
                    text_list.remove(a)
                    
            if subword in text_list:
                text_list.remove(subword)

        
    task = ' '.join(text_list)
    task_metadata.append(task)
    data['task'] = task
    data["task_metadata"] = task_metadata
    print(task_metadata)
    # print(data)
    typer.echo(f"Task added: {data["task"]} \
            \nTags: {data["tag"]} | Priority: {data["priority"]} | Due: {data["due"]}")
    return data 


@app.command()
def xyz(x,y):
    return x+y


if __name__ == '__main__':
    app()