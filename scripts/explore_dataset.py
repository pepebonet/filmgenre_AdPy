"""
Script to explore the dataset
"""

import click
import pandas as pd


@click.command(short_help="script to explore the film genre datset")
@click.option(
    "--dataset", "-d", type=str, required=True, help="Path to the dataset file."
)
@click.option(
    "--output", "-o", help="Output file if we have something."
)
def main(dataset, output):
    """
    Explore dataset and call other functions
    """
    import pdb;pdb.set_trace()


if __name__ == '__main__':
    main()