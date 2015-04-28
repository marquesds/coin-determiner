from django.db import models


class Coin(models.Model):
    """
    Write something here
    """
    value = models.IntegerField('Value', max_length=250)

    def coinDeterminer(self, num, coin_list=None):
        """
        Write something here
        :param num:
        :param coin_list:
        :return:
        """
        if not coin_list:
            coins = [1, 5, 7, 9, 11]
        else:
            coins = coin_list
        coins.sort()
        coins.reverse()
        cNum = 0
        if num in coins:
            cNum += 1
        else:
            while num > 0:
                for c in coins:
                    if num % c == 0:
                        num -= c
                        cNum += 1
                        break
                    elif num > c:
                        num -= c
                        cNum += 1
                        break

        return cNum

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'
