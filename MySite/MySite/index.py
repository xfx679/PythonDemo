from django.http.request import HttpRequest
from django.shortcuts import render_to_response


def index(request=HttpRequest):
    # txt = request.GET['txt']
    # contest = {}
    # if txt == '1':
    #     contest['contest1'] = True
    # elif txt == '2':
    #     contest['contest2'] = True
    # return render_to_response("index.html", contest)

    contest = {}
    contest['items'] = ['小明', '小张', '小强', '小红']
    return render_to_response('index.html', contest)
