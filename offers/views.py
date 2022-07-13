from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from offers.models import newconnection
from .forms import CreateUserForm
from .forms import NewConnectionForm
from offers.models import plans
from offers.forms import PlanForm
from offers.forms import PostpaidForm
from offers.forms import DongleForm
from offers.forms import InvoiceForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from .serializers import userdetailsSerializer
from .serializers import CustomerDetailsSerializer

def index(request):
    return render(request, "index.html")

def home(request):
    record1 = plans.objects.all()
    record2 = postpaid.objects.all()
    record3 = dongle.objects.all()
    return render(request, 'home.html',{'record1': record1, 'record2':record2 , 'record3':record3})

def Adminhome(request):
    return render(request , 'Adminhome.html')

def Adminplans(request):
    records=plans.objects.all()
    postrecords = postpaid.objects.all()
    donglerecords = dongle.objects.all()
    return render(request, 'Adminplans.html',{'records': records ,'postrecords':postrecords,'donglerecords':donglerecords})

def update(request,id):
    context = {}
    obj=get_object_or_404(plans,id=id)
    form=PlanForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/Adminplans')

    context['form']=form
    return render(request,'update.html',context)

def upostpaid(request,id):
    context = {}
    obj=get_object_or_404(postpaid,id=id)
    form=PostpaidForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/Adminplans')

    context['form']=form
    return render(request,'upostpaid.html',context)

def udongle(request,id):
    context = {}
    obj=get_object_or_404(dongle,id=id)
    form=DongleForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/Adminplans')

    context['form']=form
    return render(request,'udongle.html',context)

def delete(request,id):
    res=plans.objects.get(id=id)
    res.delete()
    return redirect('/Adminplans')

def dpostpaid(request,id):
    res=postpaid.objects.get(id=id)
    res.delete()
    return redirect('/Adminplans')

def ddongle(request,id):
    res=dongle.objects.get(id=id)
    res.delete()
    return redirect('/Adminplans')
def  new(request):
    context = {}
    form=PlanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/Adminplans')

    context['form']=form
    return render(request,'new.html',context)
def npostpaid(request):
    context = {}
    form=PostpaidForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/Adminplans')

    context['form']=form
    return render(request,'npostpaid.html',context)

def ndongle(request):
    context = {}
    form=DongleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/Adminplans')

    context['form']=form
    return render(request,'ndongle.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method =="POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request,'Account was created for' + user)
                return redirect('login')
        context = {'form':form}
        return render(request,'accounts/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user=authenticate(request,username=username, password=password)

            if user is not None:
                return redirect('http://localhost:4200/')
            elif username == 'Admin1' and password == 'root12345':
                return redirect('/Adminhome')
            else:
                messages.info(request, 'username OR password is Incorrect')

        context={}
        return  render(request, 'accounts/login.html',context)

def logout(request):
    return redirect('/')



class Userdetailslist(APIView):
    def get(self, request):
        queryset= userdetails.objects.all()
        obj = userdetailsSerializer(queryset, many=True)
        return Response(obj.data)

class Customerlist(APIView):
    def get(self, request):
        queryset = Customer.objects.all()
        obj = CustomerDetailsSerializer(queryset, many=True)
        return Response(obj.data)

def recharge(request,id):
    rec = plans.objects.get(id=id)
    total = rec.pprize + 150 + 15
    return render(request,'recharge.html',{'rec':rec , 'total':total})

def Postrecharge(request,id):
    rec1 = postpaid.objects.get(id=id)
    total = rec1.pstprize + 150 + 15
    return render(request,'pstrecharge.html',{'rec1':rec1 ,'total':total})

def Donglerecharge(request,id):
    rec2 = dongle.objects.get(id=id)
    total = rec2.dprize + 150 + 15
    return render(request,'Donglerecharge.html',{'rec2':rec2 , 'total':total})

def Success(request):
    return render(request,'success.html')

def confirmation(request,id):
    res = plans.objects.get(id=id)
    total = res.pprize + 150 + 15
    return render(request, 'confirmation.html', {'res':res , 'total':total})

def Newconnection(request):
    context = {}
    form=NewConnectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')

    context['form']=form
    return render(request,'newconnection.html',context)

def AdminNew(request):
    con= newconnection.objects.all()
    return render(request,'Adminnew.html',{'con':con})

def confirmation2(request,id):
    res2 = postpaid.objects.get(id=id)
    total=res2.pstprize+150+15
    return render(request, 'confirmation2.html', {'res2':res2 , 'total':total})

def confirmation3(request,id):
    res3 = dongle.objects.get(id=id)
    total = res3.dprize + 150 + 15
    return render(request, 'confirmation3.html', {'res3':res3 , 'total':total})

def Invoice(request):
    context = {}
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/invoicebill')

    context['form'] = form
    return render(request, 'invoice.html', context)

def invoicebill(request):

    return render(request,'invoicebill.html')