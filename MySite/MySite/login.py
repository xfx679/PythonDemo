from django.http.request import HttpRequest
from django.shortcuts import render_to_response


def login(request=HttpRequest):
    print('成功1')
    return render_to_response('login.html')
