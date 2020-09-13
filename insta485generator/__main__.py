"""Build static HTML site from directory of HTML templates and plain files."""
import pathlib
import click


@click.command()
@click.argument('INPUT_DIR')
@click.option('--output', '-o', default="", help='Output directory.',)
@click.option('--verbose', '-v', is_flag=True, help='Print more output.',)

def main(input_dir, output, verbose):
    """Templated static website generator."""
    #Don't forget to use verbose and input path
    if output == "":
        output = input_dir
    input_path = pathlib.Path.cwd() / input_dir / "templates" / "index.html"


if __name__ == "__main__":
    main()
