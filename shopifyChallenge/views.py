from django.http import HttpResponse
from django.shortcuts import render



# the home page of the main website
def home_view(request):
    user = request.user
    hello = 'Hello,'

    #Shows different main page depends on different users
    context = {
        'user': user,
        'hello': hello,
    }

    return render(request,'main/home.html', context)
    # return HttpResponse("Hello world")