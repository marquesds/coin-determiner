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
        Write something here
        :param num:
        :param coin_list:
        :return:
        """
        used_coins = []
        # Write something here
        if not coin_list:
            coins = [1, 5, 7, 9, 11]
        else:
            coins = coin_list
        # List'll begin with the highest value
        coins.sort()
        coins.reverse()
        coins_number = 0
        # Write something here
        if value in coins:
            used_coins.append(value)
            coins_number += 1
        else:
            # Write something here
            while value > 0:
                for coin in coins:
                    # Write something here
                    if value % coin == 0:
                        used_coins.append(coin)
                        value -= coin
                        coins_number += 1
                        break
                    elif value > coin:
                        # Write something here
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
