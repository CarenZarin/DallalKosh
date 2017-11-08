from django.shortcuts import render

# Create your views here.

from .forms import *
from django.contrib.auth.decorators import login_required



def root(request):
    return render(request, 'root.html')

@login_required()
def requestedgood(request):
    if request.method == 'POST':
        form = RequestedGoodForm(request.POST, request.FILES)

        if form.is_valid():

            obj = form.save(commit=False)
            obj.requestedgood_user = request.user
            form.save()


    else:
        form = RequestedGoodForm()

    return render(request, 'requestedgood.html', {'form': form})

@login_required()
def requestedgoodlist(request):
    requested_good_list = RequestedGood.objects.all()

    print(requested_good_list)

    return render(request, 'requestedgoodlist.html', {'requested_good_list': requested_good_list})

@login_required()
def request(request):

    print(request.GET.get('id'))

    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.good_owner = request.user
            obj.good_requestedgood = RequestedGood.objects.get(pk=int(request.GET.get('id')))
            print(obj.good_requestedgood)
            form.save()

    else:
        form = RequestForm()

    return render(request, 'request.html', {'form': form})

@login_required()
def show_user_goods(request):

    user =request.user

    user_goods_list =Good.objects.filter(good_requestedgood__requestedgood_user=user)


    return render(request, 'show_user_goods.html', {'user_goods_list': user_goods_list})

@login_required()
def show_user_requested_goods(request):


    user =request.user

    user_requested_goods_list =RequestedGood.objects.filter(requestedgood_user=user)

    return render(request, 'user_requested_goods_list.html', {'user_requested_goods_list': user_requested_goods_list})
