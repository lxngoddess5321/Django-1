from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemList
# Create your views here.

context = {
    'list': [
        {
        'id':0,
        'price': '599.00',
        'postal':'True',
        'title': 'GXG羽绒服男装 冬季时尚休闲加厚保暖连帽羽绒服外套',
        'shopNick': 'GXG官方旗舰店',
        'payNum':'56人已付款',
        'count':599,
        'image':'https://img.alicdn.com/imgextra/i2/2886195504/TB2KOFVplHH8KJjy0FbXXcqlpXa_!!2886195504.jpg'
    },
    {
        'id':1,
        'price': '899.00',
        'postal':'True',
        'title': 'Jordan 官方JORDAN JUMPMAN男子篮球鞋BQ3448',
        'shopNick': 'NIKE官方旗舰店',
        'payNum':'356人已付款',
        'count':899,
        'image':'https://img.alicdn.com/imgextra/i3/890482188/O1CN01UVZnjW1S29A4J64Dl_!!890482188.jpg'
    },
    {
        'id':2,
        'price': '489.00',
        'postal':'True',
        'title': 'GXG男装 连帽加厚灰鸭绒潮流中长款黑科技羽绒服男士',
        'shopNick': 'GXG官方旗舰店',
        'payNum':'1237人已付款',
        'count':489,
        'image':'https://img.alicdn.com/imgextra/i1/78643081/O1CN01IBa7WG1Yd8qkhf6Oq_!!78643081.jpg'
    },
    {
        'id':3,
        'price': '89.00',
        'postal':'True',
        'title': 'Python语言及其应用python语言程序设计Python程序设计教程',
        'shopNick': '人民邮电官方旗舰店',
        'payNum':'2370人已付款',
        'count':89,
        'image':'https://img.alicdn.com/imgextra/i2/2041592426/TB2xn0Yx.dnpuFjSZPhXXbChpXa_!!2041592426.jpg'
    },
    {
        'id':4,
        'price': '47.5',
        'postal':'True',
        'title': '正版 Python Django开发实战(视频讲解版)高效Python Web框架指南 django项目 ',
        'shopNick': '人民邮电官方旗舰店',
        'payNum':'370人已付款',
        'count':47.5,
        'image':'https://img.alicdn.com/imgextra/i2/2451699564/O1CN01P20Rwu2KWMWx0RtcT_!!2451699564.jpg'
    }
    ]
}

# def index(request):
#     # return HttpResponse(context)
#     return render(request,'items/list.html', context)

def index(request):
    return render(request, 'items/list.html', {'list': ItemList.objects.all()})
