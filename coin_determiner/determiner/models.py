from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Coin(models.Model):
    """
    Class that represents the coin
    """
    value = models.IntegerField('Value', default=1, validators=[
        MaxValueValidator(250),
        MinValueValidator(1)
    ])

    def coinDeterminer(self, value, coin_list=None):
        """
        With a given value, the function returns the
        least number of coins
        :param value: Input value to be processed
        :param coin_list: Optional list of default coins
        :return: A least number of coins
        """
        used_coins = []
        # If coin_list not given, get the default values
        if not coin_list:
            coins = [1, 5, 7, 9, 11]
        else:
            coins = coin_list
        # List'll begin with the highest value
        coins.sort()
        coins.reverse()
        coins_number = 0
        # Returns 1 if value is equal to one of default coins
        if value in coins:
            used_coins.append(value)
            coins_number += 1
        else:
            # While value not 0 run the code below
            while value > 0:
                for coin in coins:
                    # If result of division is zero, subtract value from coin
                    # and add +1 to coins_number
                    if value % coin == 0:
                        used_coins.append(coin)
                        value -= coin
                        coins_number += 1
                        break
                    # If result of division is not zero, get the highest coin
                    # and subtract value from it
                    elif value > coin:
                        used_coins.append(coin)
                        value -= coin
                        coins_number += 1
                        break

        return coins_number

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'
