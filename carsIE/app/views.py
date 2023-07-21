from typing import Type
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from math import ceil
from django.contrib import messages
from django.db.models import Q
from itertools import chain
import _json
from django.views import View
from datetime import date, datetime, timezone
from .forms import *
import pytz
z = datetime.now()
x=datetime.now(tz=pytz.timezone('Asia/Tokyo'))




def home(request):
    carss = Car.objects.all()
    companies = Company.objects.all()    
    type = CarType.objects.all()
    steer = Steering.objects.all()
    manfd = ManufacturingYM.objects.all()  
    ships = ShippingSituation.objects.all()     
    saleso = SalesOffice.objects.all()
    mhead = MainHeading.objects.all()
    pricerange = PriceRange.objects.all()
    discount = Discount.objects.all()
    type = CarType.objects.all()
    cont = Country.objects.all()
    rev = Review.objects.all()
    qas = QuestionAndAnswer.objects.all()
    context = {
        'carss':carss, 
        'companies':companies,         
        'type':type, 
        'steer':steer,  
        'manfd':manfd,
        'datetimejapan':x,
        'ships':ships,
        'saleso':saleso ,
        'mhead':mhead     ,
        'pricerange':pricerange ,
        'discount':discount    ,
        'type':type,
        'cont':cont,
        'rev':rev,
        'qas':qas
        }
    return render(request, 'app/home.html', context)

def search(request):
    allCars = Car.objects.all().order_by("CarName")
    
    if "query" in request.GET:
        query = request.GET['query']
        car = Car.objects.filter(Q(CarName__icontains=query)|Q(company__CompanyName__icontains=query)|Q(mfdate__ManufacturingDate__icontains=query)|Q(RefNo__icontains=query) )                 
    else:
        car = Car.objects.all().order_by("CarName")

    if "com" in request.GET:
        cid = request.GET["com"]
        car = Car.objects.filter(company__CompanyID=cid)

    if "pre" in request.GET:
        prID = request.GET["pre"]
        car = Car.objects.filter(pricerange__PriceID=prID)

    if "des" in request.GET:
        dsID = request.GET["des"]
        car = Car.objects.filter(discount__DiscountID=dsID) 

    if "tape" in request.GET:
        tpID = request.GET["tape"]
        car = Car.objects.filter(type__TypeID=tpID)  

    if "coo" in request.GET:
        conID = request.GET["coo"]
        car = Car.objects.filter(country__CountryID=conID)    

    CompanyID = request.GET.get('CompanyID')
    cars = Car.objects.filter(company=CompanyID).order_by("CarName")              

    context = {'allCars':allCars,'car':car, 'cars':cars}    
    return render(request, 'app/search.html', context) 

def load_cars(request):
    company = request.GET.get('company')
    cars = Car.objects.filter(company=company).order_by('CarName')
    context = {'cars':cars}
    return render(request, 'app/cars_dropdown_list_options.html', context)   


    

def searchdd(request):

   carForm = Car.objects.all()   
   companyname = request.POST.get('company_ddl')
   carname = request.POST.get('car_name') 
   ctyp = request.POST.get('cartype') 
   steeringn = request.POST.get('steeringname')
   fromdate = request.POST.get('from_date')
   todate = request.POST.get('to_date') 

   if companyname:
       carForm = Car.objects.filter(company=companyname)       

   if carname:
       carForm = Car.objects.filter(CarID=carname) 

   if fromdate:                
       carForm= Car.objects.filter(mfdate__ManufacturingDate__gte=fromdate)    
   
   if todate:       
       carForm= Car.objects.filter(mfdate__ManufacturingDate__lte=todate) 

   if fromdate and todate:
       carForm = Car.objects.filter(mfdate__ManufacturingDate__range=(fromdate, todate))   

   if ctyp:
       carForm = Car.objects.filter(type=ctyp)    

   if steeringn:
       carForm = Car.objects.filter(steering=steeringn)  
    

   context = {'carForm':carForm} 
   return render(request, 'app/searchdd.html', context)

def allreview(request):
    review = Review.objects.all()
    context = {'review':review}
    return render(request, 'app/allreview.html', context)



def terms(request):
    return render(request, 'app/terms.html')

def contact(request):
    return render(request, 'app/contact.html')




# def searchdd(request):

#    carForm = Car.objects.all()   

#    companyname = request.POST.get('company_ddl')
#    carname = request.POST.get('car_name') 
#    ctyp = request.POST.get('cartype') 
#    steeringn = request.POST.get('steeringname')
#    fromdate = request.POST.get('from_date')
#    todate = request.POST.get('to_date') 

# #    if request.method == "POST":
       
# #        fdate = datetime.year(fromdate)
# #        tdate = datetime.year(todate)
# #        carForm = Car.objects.filter(mfdate__range=(fdate, tdate))

# #        context = {'carForm':carForm}
# #        return render(request, 'app/searchdd.html', context)

#    if companyname:
#        if request.method == "POST":
#            carForm = Car.objects.filter(company=companyname)
            
#            context = {'carForm':carForm} 
#            return render(request, 'app/searchdd.html', context)

#    if carname:
#        if request.method == "POST":        
#            carForm = Car.objects.filter(CarID=carname)
                
#            context = {'carForm':carForm} 
#            return render(request, 'app/searchdd.html', context)
#    if ctyp:
#        if request.method == "POST":
#            carForm = Car.objects.filter(type=ctyp)

#            context = {'carForm':carForm} 
#            return render(request, 'app/searchdd.html', context)

#    if steeringn:
#        if request.method == "POST":
#            carForm = Car.objects.filter(steering=steeringn)

#            context = {'carForm':carForm} 
#            return render(request, 'app/searchdd.html', context)
      


class ProductDetailView(View):

    def get(self, request, pk):
        pro = Car.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'pro':pro})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
