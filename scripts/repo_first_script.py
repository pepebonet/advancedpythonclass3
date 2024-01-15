"""
Script to make updates in github
"""
import click
import pandas as pd


class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self, df):
        self.df = df

    def filter_price(self, price):
        """
        filter by price
        """
        return self.df[self.df["Price Starting With ($)"] < price]


def load_dataset(filename):
    """
    Function to load dataset
    """
    extension = filename.rsplit('.', 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    else:
        raise TypeError(f"The extension is {extension} and not csv. Try again")


@click.command(short_help="Parser to import dataset")
@click.option("-i", "--input_file", help="Input a file")
def main(input_file):
    """
    Main Function
    """
    df = load_dataset(input_file)

    result = FilteringClass(df).filter_price(12)
    print(result.shape)


if __name__ == "__main__":
    main()
