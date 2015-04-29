from django.shortcuts import render
from .forms import CoinForm
from .models import Coin


def index(request):
    coin = Coin()
    form = CoinForm()
    result = 0

    if request.method == 'POST':
        form = CoinForm(request.POST)
        if form.is_valid():
            result = coin.coinDeterminer(int(form['value'].value()))

    context = {
        'form': form,
        'result': result
    }

    return render(request, 'index.html', context)
