from django.shortcuts import render

# Create your views here.

from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


from DallalKosh.accounts.models import MyProfile

def root(request):
    return render(request, 'root.html')

@login_required()
def entertobazar(request):
    return render(request, 'Enter_to_Bazar.html')

@login_required()
def requestedgood(request):
    message= ''
    if request.method == 'POST':
        form = RequestedGoodForm(request.POST, request.FILES)

        if form.is_valid():

            obj = form.save(commit=False)
            obj.requestedgood_user = request.user
            form.save()
            messages.success(request, 'your request is submited ')
            return HttpResponseRedirect('/entertobazaar')



    else:
        form = RequestedGoodForm()

    return render(request, 'requestedgood.html', {'form': form , 'message':message})

@login_required()
def customers_requests(request):


    user = request.user
    requested_good_list=[]

    profile = MyProfile.objects.get(user=user)
    if profile.myprofile_is_seller :
        requested_good_list = RequestedGood.objects.all()
        return render(request, 'requestedgoodlist.html', {'requested_good_list': requested_good_list})

    else:
        return render(request, 'requestedgoodlist.html', {'message': 'you are not allowd '})


@login_required()
def provider_offer(request):

    print(request.GET.get('id'))
    user=request.user
    profile = MyProfile.objects.get(user=user)
    if profile.myprofile_is_seller :

        if request.method == 'POST':
            form = RequestForm(request.POST, request.FILES)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.good_owner = request.user
                obj.good_requestedgood = RequestedGood.objects.get(pk=int(request.GET.get('id')))
                print(obj.good_requestedgood)
                form.save()
                return HttpResponseRedirect('/entertobazaar')

        else:
            form = RequestForm()

        return render(request, 'request.html', {'form': form})

    else:
        return render(request, 'request.html', {'message': 'شما اجازه‌ی دسترسی به این صفحه را ندارید '})


@login_required()
def provider_goods(request):

    user =request.user

    user_goods_list =Good.objects.filter(good_requestedgood__requestedgood_user=user)


    return render(request, 'show_user_goods.html', {'user_goods_list': user_goods_list})

@login_required()
def customer_requestlist(request):


    user =request.user

    user_requested_goods_list =RequestedGood.objects.filter(requestedgood_user=user)

    #
    # if request.method=='POST':
    #     final_choose= request.POST.get('final_choose')
    #     if final_choose == 'on':if
    #

    return render(request, 'user_requested_goods_list.html', {'user_requested_goods_list': user_requested_goods_list})


@login_required()
def show_company_goods(request):

    user = request.user
    profile = MyProfile.objects.get(user=user)
    company_goods_list =[]
    if profile.myprofile_is_seller:
        company_goods_list =Good.objects.filter(good_owner=user)

        return render(request, 'show_company_goods.html', {'company_goods_list': company_goods_list})
    else :
        return render(request, 'show_company_goods.html', {'message': 'you are not allowed '})

@login_required()
def customer_final_choose(request):
    user = request.user
    

    return render(request , '')