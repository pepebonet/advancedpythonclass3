"""
Script to make updates in github
"""
import click
import pandas as pd


click.command(short_help='Parser to import dataset')
click.option('-f', '--filename', required=True, help='File to import')
def main(filename):
    """
    Main Function
    """

    df = pd.read_csv(filename)

    print(df.shape)


if __name__ == "__main__":
    main()