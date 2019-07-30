from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    ClientForm,
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from accounts.models import Check1, Client, Factory, Good, Payment1, Transport
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib import messages

#Клиент
def view_client(request, pk=None):
    if pk:       
        name = get_object_or_404(Client, pk=pk)
    else:
        name = request.name
    args = {'id':name.id, 'name': name.name, 'phone':name.phone, 'address':name.address} 
    return render(request, 'accounts/client_detail.html', args)

def edit_client(request, pk=None):
    instance = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/account/Client") 
    context = {
        "name": instance.name,
        "phone": instance.phone,
        "address": instance.address,
        "form": form,
    }
    return render(request, "accounts/edit.html", context)

def delete_client(request, pk=None):
    instance = get_object_or_404(Client, pk=pk)
    instance.delete()
    return redirect("accounts:Client")

#Home
def home(request):
    return render(request, 'accounts/home.html')

def Checks(request):
    all_check = Check1.objects.all()
    sum = 0
    for check in all_check:
        sum += check.price
    context1 = {'all_check': all_check, 'sum': sum}
    return render(request, 'accounts/Check.html', context1)

def Clients(request):
    all_client = Client.objects.all()
    context = {'all_client': all_client}
    return render(request, 'accounts/Client.html', context)

def Factorys(request):
    all_factory = Factory.objects.all()
    context = {'all_factory': all_factory}
    return render(request, 'accounts/Factory.html', context)

def Goods(request):
    all_good = Good.objects.all()
    sum = 0
    for good in all_good:
        sum += good.count
    context = {'all_good': all_good, 'sum': sum}
    return render(request, 'accounts/Good.html', context)

def Payments(request):
    all_payment = Payment1.objects.all()
    sum1 = 0
    sum2 = 0
    for payment in all_payment:
        sum1 += payment.price
        sum2 += payment.price_nds
    context = {'all_payment': all_payment, 'sum1': sum1, 'sum2': sum2}
    return render(request, 'accounts/Payment.html', context)

def Transports(request):
    all_transport = Transport.objects.all()
    context = {'all_transport': all_transport}
    return render(request, 'accounts/Transport.html', context)


# сохранение данных в бд
def create(request):
    if request.method=='POST':
        tom = Client()
        tom.name = request.POST.get("name")
        tom.phone = request.POST.get("phone")
        tom.address = request.POST.get("address")
        tom.save()
    return HttpResponseRedirect("/account/Client")     

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def check_new(request, pk):
    id_client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        tom = Check1()
        tom.name = request.POST.get("name")
        tom.price = request.POST.get("price")
        tom.date = request.POST.get("date")
        tom.id_client = id_client
        tom.save()
    return HttpResponseRedirect("/account/Check")

def delete_check(request, pk=None):
    instance = get_object_or_404(Check1, pk=pk)
    instance.delete()
    return redirect("accounts:Check")

def payment_new(request, pk):
    id_client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        tom = Payment1()
        tom.name = request.POST.get("name")
        tom.date = request.POST.get("date")
        tom.check_name =  request.POST.get("check_name")
        tom.price = request.POST.get("price") 
        price_a =  float(tom.price)
        tom.nds = price_a *0.18  
        tom.price_nds = price_a + (tom.nds)   
        tom.id_client = id_client
        tom.save()
    return HttpResponseRedirect("/account/Payment")

def delete_payment(request, pk=None):
    instance = get_object_or_404(Payment1, pk=pk)
    instance.delete()
    return redirect("accounts:Payment")

#Завод
def create_factory(request):
    if request.method=='POST':
        tom = Factory()
        tom.name = request.POST.get("name")
        tom.phone = request.POST.get("phone")
        tom.address = request.POST.get("address")
        tom.save()
    return HttpResponseRedirect("/account/Factory") 

def view_factory(request, pk=None):
    if pk:       
        name = get_object_or_404(Factory, pk=pk)
    else:
        name = request.name
    args = {'id':name.id, 'name': name.name, 'phone':name.phone, 'address':name.address} 
    return render(request, 'accounts/factory_detail.html', args)

def edit_factory(request, pk=None):
    instance = get_object_or_404(Factory, pk=pk)
    form = ClientForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/account/Factory") 
    context = {
        "name": instance.name,
        "phone": instance.phone,
        "address": instance.address,
        "form": form,
    }
    return render(request, "accounts/edit.html", context)

def delete_factory(request, pk=None):
    instance = get_object_or_404(Factory, pk=pk)
    instance.delete()
    return redirect("accounts:Factory")

#good,transport
def good_new(request, pk):
    id_factory = get_object_or_404(Good, pk=pk)
    if request.method == "POST":
        tom = Good()
        tom.name = request.POST.get("name")
        tom.count = request.POST.get("count")
        tom.id_factory = id_factory
        tom.save()
    return HttpResponseRedirect("/account/Good")

def delete_good(request, pk=None):
    instance = get_object_or_404(Good, pk=pk)
    instance.delete()
    return redirect("accounts:Good")

def transport_new(request, pk):
    id_factory = get_object_or_404(Transport, pk=pk)
    if request.method == "POST":
        tom = Transport()
        tom.name = request.POST.get("name")
        tom.phone = request.POST.get("phone")
        tom.address =  request.POST.get("address")
        tom.id_factory = id_factory
        tom.save()
    return HttpResponseRedirect("/account/Transport")

def delete_transport(request, pk=None):
    instance = get_object_or_404(Transport, pk=pk)
    instance.delete()
    return redirect("accounts:Transport")