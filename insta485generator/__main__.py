"""Build static HTML site from directory of HTML templates and plain files."""
import pathlib
import click
import json
import jinja2


@click.command()
@click.argument('INPUT_DIR')
@click.option('--output', '-o', default="", help='Output directory.',)
@click.option('--verbose', '-v', is_flag=True, help='Print more output.',)

def main(input_dir, output, verbose):
    """Templated static website generator."""
    #Don't forget to use verbose and input path
    if output == "":
        output = input_dir
    json_path = pathlib.Path(input_dir) / "config.json"

    #Open JSON File
    with open(json_path, mode='r') as file:
        try:
            data = json.load(file)
        except ValueError:
            print("JSON ERROR")
            exit(1)
    
    print(verbose)
    for item in data:
        #Determine output path
        url = item["url"].lstrip("/")  # remove leading slash
        input_dir = pathlib.Path(output)  # convert str to Path object
        template_dir = input_dir / "templates"
        output_dir = input_dir/"html"  # default, can be changed with --output option
        output_path = output_dir/url
        output_file = output_path / "index.html"

        try:
            output_path.mkdir(parents = True)
            output_file.touch()

        except FileExistsError:
            print("Directory already exists")
            exit(1)
        
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(template_dir)), autoescape=jinja2.select_autoescape(['html', 'xml']),)
        template = env.get_template('index.html')
        output_file.write_text(template.render(item['context']))



        



        print(output_path)











if __name__ == "__main__":
    main()
