"""
Script to explore the dataset
"""
import os
import click
import pandas as pd

MAX_ALLOWED_ROWS = 100000


class FiltersMovies():  # pylint: disable=R0903
    """
    Class to provide functions for filtering movies
    """

    def __init__(self, df):
        self.df = df

    def get_movies_year(self, year):
        """
        Get movies for a given year
        """
        return self.df[self.df['Year'] == int(year)]


class ComputationsMovies(FiltersMovies):
    """
    Functions to perform computations in movies
    """

    def sum_movies_released(self):
        """
        Sum the number of released movies
        """
        return self.df['Movies Released'].sum()


def check_columns(df):
    """
    Check number of rows does not exceeds our limit
    """

    if df.shape[0] > MAX_ALLOWED_ROWS:
        raise ValueError("Number of rows is too large")


def load_dataset(dataset):
    """
    Load input dataset with pandas
    """

    extension = dataset.rsplit('.')[-1]
    if extension != 'csv':
        raise TypeError("The file needs to be a csv")

    df = pd.read_csv(dataset)

    check_columns(df)

    return df


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
def main(dataset=None, year=None, output=None):
    """
    Explore dataset and call other functions
    """

    df = load_dataset(dataset)

    if year:
        try:
            df = FiltersMovies(df).get_movies_year(year)
        except TypeError as e:
            raise TypeError(f'The parameter year was not found: {e}') from e

    print(ComputationsMovies(df).sum_movies_released())

    out_path = os.path.join(output, f'film_genre_{year}.csv')
    df.to_csv(out_path, sep=',', index=None)


if __name__ == '__main__':
    main()
