from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from data.cartItems import context as cartContext
# from data.itemList import context as itemContext
from items.models import ItemList


def list(request):
    return render(request, 'cart/list.html', {'list': cartContext.values})


def add(request, item_idx):
    if request.method == 'POST':
        if item_idx in cartContext:
            cartItem = cartContext[item_idx]
            cartItem['count'] += 1
        else:
            item = ItemList.objects.get(id=item_idx)
            cartItem = {
                'id': item.id,
                'price': item.price,
                'title': item.title,
                'shopNick': item.shopNick,
                'payNum': item.payNum,
                'count': item.count,
                'image': item.image
            }
            cartItem['count'] = 1
            cartContext[item_idx] = cartItem

        return HttpResponseRedirect(reverse('items:index'))
        # return render(request, 'items/list.html', {'list': itemContext})
    else:
        return HttpResponse('failed')


def delete(request):
    return HttpResponse('haha')
    # del context['list'][]
    # return render(request, 'cart/list.html', context)
