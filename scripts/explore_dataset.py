"""
Script to explore the dataset
"""
import os
import click
import pandas as pd


class filters_movies:

    def __init__(self, df):
        self.df = df

    def get_movies_year(self, year):
        return self.df[self.df['Year'] == int(year)]


class computations_movies(filters_movies):

    def sum_movies_released(self):
        return self.df['Movies Released'].sum()


@click.command(short_help="script to explore the film genre datset")
@click.option(
    "--dataset", "-d", type=str, required=True, help="Path to the dataset file."
)
@click.option(
    "--year", "-y", help="Year to filter but to get the number of movies released."
)
@click.option(
    "--output", "-o", help="Output file if we have something.", default='datasets'
)
def main(dataset, year, output):
    """
    Explore dataset and call other functions
    """

    df = pd.read_csv(dataset)
    import pdb;pdb.set_trace()

    if year:
        try:
            df = filters_movies(df).get_movies_year(year)
        except TypeError as e:
            raise TypeError(f'The parameter year was not found: {e}')

    print(computations_movies(df).sum_movies_released())

    out_path = os.path.join(output, f'film_genre_{year}.csv')
    df.to_csv(out_path, sep=',', index=None)


if __name__ == '__main__':
    main()