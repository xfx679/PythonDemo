from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


def login_action(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST.get('password'))
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            # cookie
            resphonse = HttpResponseRedirect("/search_name/")
            # resphonse.set_cookie('user', username, 3600)
            # session
            return resphonse
        else:
            return render_to_response('login.html', {'error': 'username and password error'})


# cookie
def login_cookie(request):
    username = request.COOKIES.get('user')
    return render_to_response('login_success.html', {'user': username})


# session
@login_required
def login_session(request):
    username = request.session.get('user')
    return render_to_response('event_manage.html', {'user': username})
