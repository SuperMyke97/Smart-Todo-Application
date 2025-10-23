import re
import typer
from regex_patterns import regex_patterns

app = typer.Typer()

@app.command()
def add(text: str):
    
    text = text.lower()
    data: dict = regex_patterns(text)
    text_list = text.split(" ")

    patterns = [re.compile(r"due:(([0-9]{4}-[0-1][0-9]-[0-3][0-9])|(tomorrow)|(next\s?week\s\w+))", re.I), 
                re.compile(r"every\s?([a-zA-Z]+)", re.I), 
                re.compile(r"(\d+(min|hr|h|sec)?)(\s?)(\d+(min|sec))?(\s?)(\d+(sec))?", re.I),
                re.compile(r"(#[a-zA-Z]+)"),
                re.compile(r"((at|by)\s\d+(:\d+)?(pm|am))"),
                re.compile(r"(@[a-zA-Z]+)", re.I),
                re.compile(r"([a-zA-Z]+:\w+@\w+.com)", re.I)]


    for p in patterns:
        if p.search(text)!= None:
            z = p.search(text).group().strip()
            # print(z)
            if ' ' in z:
                for a in z.split(' '): 
                    text_list.remove(a)

            if z in text_list:
                text_list.remove(z)

        
    data["Task"] = ' '.join(text_list)
    # print(data)
    typer.echo(f"Task added: {data["Task"]} \
            \nTags: {data["Tag"]} | Priority: {data["Priority"]} | Due: {data["Due"]}")
    return data 


@app.command()
def xyz(x,y):
    return x+y


if __name__ == '__main__':
    app()