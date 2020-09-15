"""Build static HTML site from directory of HTML templates and plain files."""
import pathlib
import json
from distutils.dir_util import copy_tree as copyer
import sys
import click
import jinja2


@click.command()
@click.argument("INPUT_DIR")
@click.option(
    "--output", "-o", default="", help="Output directory.",
)
@click.option(
    "--verbose", "-v", is_flag=True, help="Print more output.",
)
def main(input_dir, output, verbose):
    """Templated static website generator."""
    # Don't forget to use verbose and input path
    json_path = pathlib.Path(input_dir) / "config.json"

    # Open JSON File
    with open(json_path, mode="r") as file:
        try:
            data = json.load(file)
        except ValueError:
            print("JSON ERROR")
            sys.exit(1)
    for item in data:
        # Determine output path
        url = item["url"].lstrip("/")  # remove leading slash
        input_dir = pathlib.Path(input_dir)  # convert str to Path object
        template_dir = input_dir / "templates"
        # default, can be changed with --output option
        output_dir = input_dir / "html"
        if output != "":
            output_dir = pathlib.Path(output)
        output_path = output_dir / url
        output_file = output_path / "index.html"

        try:
            output_path.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print("Directory already exists")
            sys.exit(1)
        try:
            output_file.touch()
        except FileExistsError:
            print("File already exists")
            sys.exit(1)
        if (input_dir / "static").exists():
            copyer(str(input_dir / "static"), str(output_dir))
            if verbose:
                print("Copied " + str(input_dir / "static") + " -> "
                      + str(output_path))
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(template_dir)),
            autoescape=jinja2.select_autoescape(["html", "xml"]),
        )
        template = env.get_template(item["template"])
        output_file.write_text(template.render(item["context"]))

        if verbose:
            print("Rendered " + item["template"] + " -> " + str(output_file))


if __name__ == "__main__":
    main()
