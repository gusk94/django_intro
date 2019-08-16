# pages/views
from django.shortcuts import render
from datetime import datetime
import random



def index(request):  # 첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html' 을 보여준다.
    return render(request, 'index.html')  # render의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'introduce.html')


# Template Variable Example
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name
    }

    # Django template 으로 context 전달
    return render(request, 'dinner.html', context)


def image(request):
    url = 'https://picsum.photos/500'
    context = {
        'url': url
    }
    return render(request, 'image.html', context)


def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2,
    }
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mange']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def isitbirthday(request):
    return render(request, 'isitbirthday.html')


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    lotto = random.sample(range(1, 46), 6)
    context = {
        'real_lotto': real_lotto,
        'lotto': sorted(lotto)
    }
    return render(request, 'lotto.html', context)


def search(request):
    return render(request, 'search.html')


def result(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    context = {
        'query': query,
        'category': category,
    }
    return render(request, 'result.html', context)


def lotto_pick(request):
    return render(request, 'lotto_pick.html')


def lotto_result(request):
    lotto_num = request.GET.get('lotto').split()
    lotto_num = sorted(list(map(int, lotto_num)))
    re_lotto = [21, 25, 30, 32, 40, 42]
    context = {
        're_lotto': re_lotto,
        'lotto_num': lotto_num, 
    }
    return render(request, 'lotto_result.html', context)


def static_example(request):
    return render(request, 'static_example.html')
