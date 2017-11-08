from django.shortcuts import render

# Create your views here.

from .forms import *

def root(request):
    return render(request, 'root.html')


def requestedgood(request):



    if request.method == 'POST':
        form = RequestedGoodForm(request.POST ,request.FILES)

        if form.is_valid():

            form.save()
            print('yep')


    else:
        form = RequestedGoodForm()

    return render(request, 'requestedgood.html', {'form':form})


def requestedgoodlist(request):

    requested_good_list = RequestedGood.objects.all()

    print(requested_good_list)


    return render(request, 'requestedgoodlist.html', {'requested_good_list':requested_good_list})

def request(request):



    if request.method == 'POST':
        form = RequestForm(request.POST ,request.FILES)

        if form.is_valid():
            obj =form.save(commit=False)
            obj.good_owner =request.user

            form.save()
            print('yep')


    else:
        form = RequestForm()

    return render(request, 'request.html', {'form':form})
