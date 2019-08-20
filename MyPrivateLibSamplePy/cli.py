# -*- coding: utf-8 -*-

"""Console script for MyPrivateLibSamplePy."""
import sys
import click
import MyPrivateLibSamplePy


@click.command()
def main(args=None):
    """Console script for MyPrivateLibSamplePy."""
    text = MyPrivateLibSamplePy.message()
    click.echo(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
