"""Build static HTML site from directory of HTML templates and plain files."""
import click

@click.command()
@click.argument('INPUT_DIR')
@click.option('--output', '-o', default="", help='Output directory.',)
@click.option('--verbose', '-v', is_flag=True, help='Print more output.',)

def main(input_dir, output, verbose):
    """Templated static website generator."""
    if output == "":
        output = input_dir
    print(input_dir)
    print(output)
    print(verbose)



if __name__ == "__main__":
    main()
    