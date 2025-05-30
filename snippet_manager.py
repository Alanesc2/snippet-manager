import click
import json
import pyperclip

@click.group()
def cli():
    pass


@click.command()
def add():
    title = input('Enter snippet title: ')
    language = input('Enter snippet language: ')
    code = input('Enter code snippet: ')

    with open('snippets/snippets.json', 'r') as f:
        snippets = json.load(f)

    snippets.append({
        'title': title,
        'language': language,
        'code': code
    })

    with open('snippets/snippets.json', 'w') as f:
        json.dump(snippets, f, indent=4)
    
    print(f"Snippet saved successfully!")

@click.command()
def display():
    with open('snippets/snippets.json', 'r') as f:
        snippets = json.load(f)
    
    for snippet in snippets:
        print(f"Title: {snippet['title']}")
        print(f"Language: {snippet['language']}")
        print(f"Code: {snippet['code']}")
        print('=======')

@click.command()
@click.argument('keyword')
def search(keyword):
    with open('snippets/snippets.json', 'r') as f:
        snippets = json.load(f)
    
    results = [snippet for snippet in snippets if 
    keyword.lower() in snippet['title'].lower()
    or keyword.lower() in snippet['language'].lower()]

    if results:
        for result in results:
            print(f"Title: {result['title']}")
            print(f"Language: {result['language']}")
            print(f"Code: {result['code']}")
            print('======')
    
    else:
        print("No snippets found")
     
@click.command()
def delete():
    with open('snippets/snippets.json', 'r') as f:
        snippets = json.load(f)
    
    for idx, snippet in enumerate(snippets):
        print(f"{idx + 1}, {snippet['title']} - {snippet['language']}")

    choice = int(input('Enter the number of snippet to delete: ')) - 1

    if 0 <= choice < len(snippets):
        del snippets[choice]
    
        with open('snippets/snippets.json', 'w') as f:
            json.dump(snippets, f, indent=4)
        print('Snippet deleted successfully!')
  
    else:
        print('No matching found!')

@click.command()
def copy():
    with open('snippets/snippets.json', 'r') as f:
        snippets = json.load(f)
    
    for idx, snippet in enumerate(snippets):
        print(f"{idx + 1}, {snippet['title']} - {snippet['language']}")

    choice = int(input('Enter the number of snippet to copy: ')) - 1

    if 0 <= choice < len(snippets):
        snippet = snippets[choice]
        pyperclip.copy(snippet)
        print('Snippet copied to clipboard!')
        
    else:
        print('No matching found!')

cli.add_command(add)
cli.add_command(display)
cli.add_command(search)
cli.add_command(delete)
cli.add_command(copy)


if __name__ == '__main__':
    cli()