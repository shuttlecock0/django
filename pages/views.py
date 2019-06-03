from django.shortcuts import render
import random
from pprint import pprint
import math

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return render(request, 'index.html')

def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

# 자기소개/ 이름과 나이를 url 로 받아서 출력
def introduce(request, name, age):
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'introduce.html', context)

# 숫자 2개를 variable routing으로 받아 곱셈 결과를 출력
def times(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'res': num1*num2
    }
    return render(request, 'times.html', context)

# 원의 반지름 값을 variable routing 으로 받아 원의 넓이를 출력
def area(request, r):
    context = {
        'r': r,
        'res': r * r * math.pi
    }
    return render(request, 'area.html', context)
