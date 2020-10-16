from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from sign.models import Event, Guest


# Create your views here.
def index(request):
    return render(request, 'index.html')


# 发布会管理
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user')
    return render(request, 'event_manage.html', {'user': username, 'events': event_list})


# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    print(username + '132')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})


# 签到功能
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})


# 签到动作
@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone', '')
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': '手机号为空或不存在'})
    result = Guest.objects.filter(phone=phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': '该用户未参加此次发布会'})
    result = Guest.objects.get(phone=phone, event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "已签到"})
    else:
        Guest.objects.filter(phone=phone, event_id=event_id).update(sign='1')
    return render(request, 'sign_index.html', {'event': event, 'hint': '签到成功', 'guest': result})


# 退出登录
@login_required
def logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect('/index/')
        response.delete_cookie('user')
        return response
