from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from data.itemList import context as itemContext
from data.cartItems import context as cartContxt
from items.models import ItemList


def index(request):
    if request.method == 'POST':
        for itemIdx in cartContxt.keys():
            item = ItemList.objects.get(id=itemIdx)
            item.count -= cartContxt[itemIdx]['count']
            item.save()

        cartContxt.clear()
    return render(request, 'pay/success.html', {})
