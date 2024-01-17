"""
Contains all the filters for your dataset
"""


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

    def filter_price_high(self, price):
        """
        filter by price
        """
        return self.df[self.df["Price Starting With ($)"] > price]
