from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Country(models.Model):
    CountryID = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length=100, verbose_name="Country Name")
    flagImage = models.ImageField(upload_to='productimg', verbose_name="Flag Image")

    def __str__(self):
        return self.CountryName

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User Name")
    customerName = models.CharField(max_length=200, verbose_name="Customer Name")
    locality = models.CharField(max_length=200, verbose_name="Locality")
    city = models.CharField(max_length=50, verbose_name="City")
    zipcode = models.IntegerField(verbose_name="Zip Code")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, verbose_name="Country Name")

    def __str__(self):
        return self.customerName

class CarType(models.Model):
    TypeID = models.AutoField(primary_key=True)
    TypeName = models.CharField(max_length=500, verbose_name="Vehicle Type")

    def __str__(self):
        return self.TypeName

class Company(models.Model):
    CompanyID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=500, verbose_name="Company Name")
    CompanyStock = models.CharField(max_length=500, verbose_name="Company Stock", null=True, blank=True)
    CompanyLogo = models.ImageField(upload_to='productimg', verbose_name="Company Logo")

    @staticmethod
    def get_all_companies():
        return Company.objects.all()

    def __str__(self):
        return self.CompanyName

class Steering(models.Model):
    SteeringID = models.AutoField(primary_key=True)
    SteeringName = models.CharField(max_length=50, blank=True, null=True, verbose_name="Steering Name")

    def __str__(self):
        return self.SteeringName

class ManufacturingYM(models.Model):
    ManufacturingYMID = models.AutoField(primary_key=True)
    ManufacturingDate = models.DateField(auto_now_add=False, blank= True,null=True)

    def __str__(self):
        return str(self.ManufacturingDate)

class PriceRange(models.Model):
    PriceID = models.AutoField(primary_key=True)
    Price = models.CharField(max_length=100, verbose_name="Price Range", blank=True, null=True, default="add price range like ($500 - $1,000)")

    def __str__(self):
        return str(self.Price)


class Discount(models.Model):
    DiscountID = models.AutoField(primary_key=True)
    Discount = models.CharField(max_length=100, verbose_name="Discount", blank=True, null=True, default="Add discount like (30% Off or more)")

    def __str__(self):
        return str(self.Discount)

class OtherCategorie(models.Model):
    OtherCategorieID = models.AutoField(primary_key=True)
    OtherCategoryName = models.CharField(max_length=200, null=True, blank=True, verbose_name="Other Category Name", default="add othere category like (LHD, Hybrid, electric)")
    CatImage = models.ImageField(upload_to='productimg', verbose_name="Other Category Image")

    def __str__(self):
        return str(self.OtherCategoryName)

class Currencies(models.Model):
    CurrecnyID = models.AutoField(primary_key=True)
    CurrencyName = models.CharField(max_length=50, verbose_name="Currency Name", default="add currency like USD")

    def __str__(self):
        return str(self.CurrencyName)

class Languages(models.Model):
    LanguageID = models.AutoField(primary_key=True)    
    LanguageName = models.CharField(max_length=50, verbose_name="Language Name", default="add language like English")
    FImage = models.ImageField(upload_to='productimg', verbose_name="Flag Image")

    def __str__(self):
        return str(self.LanguageName)

class MainHeading(models.Model):
    MainHeadingID = models.AutoField(primary_key=True)
    purpose = models.CharField(max_length=50, verbose_name="Website Purpose")
    stock = models.CharField(max_length=100, verbose_name="Total Stock")
    todaystock = models.CharField(max_length=50, verbose_name="Today Stock")    
    country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.DO_NOTHING)
    currency = models.ForeignKey(Currencies, verbose_name="Currency", on_delete=models.DO_NOTHING)
    language = models.ForeignKey(Languages, verbose_name="Language", on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.purpose)

class ShippingSituation(models.Model):
    ShippingSituationID = models.AutoField(primary_key=True)
    Heading = models.CharField(max_length=200, verbose_name="Heading")
    Date = models.DateTimeField(auto_now_add=False, verbose_name="Date")
    Description  = models.TextField()

    def __str__(self):
        return str(self.Heading)

class SalesOffice(models.Model):
    SalesOfficeID = models.AutoField(primary_key=True)
    Heading = models.CharField(max_length=200, verbose_name="Heading")
    Description  = models.TextField()
    Image = models.ImageField(upload_to='productimg', verbose_name="Contact Image")

    def __str__(self):
        return str(self.Heading)

class Car(models.Model):
    CarID = models.AutoField(primary_key=True)
    CarName = models.CharField(max_length=500, blank=True, null=True, verbose_name="Car Name", default="Car Name like Honda City (IDSI)")
    company = models.ForeignKey(Company, verbose_name="Company Name", on_delete=models.DO_NOTHING, default="")
    type = models.ForeignKey(CarType, verbose_name="Vehicle Type", on_delete=models.DO_NOTHING)
    CarImage = models.ImageField(upload_to='productimg', verbose_name="Vehicle Image")
    RefNo = models.CharField(max_length=500,verbose_name="Ref No", null=True, blank=True)
    ChassisNo = models.CharField(max_length=500,verbose_name="Chassis No", null=True, blank=True)
    ModelCode = models.CharField(max_length=500,verbose_name="Model Code", null=True, blank=True)
    EngineSize = models.CharField(max_length=500,verbose_name="Engine Size", null=True, blank=True)
    Location = models.CharField(max_length=500,verbose_name="Location", null=True, blank=True)
    Version = models.CharField(max_length=500,verbose_name="Version/Class", null=True, blank=True)
    Drive = models.CharField(max_length=500,verbose_name="Drive", null=True, blank=True)
    Transmission = models.CharField(max_length=500,verbose_name="Transmission", null=True, blank=True)
    mfdate = models.ForeignKey(ManufacturingYM, blank= True,null=True, on_delete=models.DO_NOTHING, verbose_name="Manufacturing Date")
    Mileage = models.CharField(max_length=500,verbose_name="Mileage", null=True, blank=True)
    EngineCode = models.CharField(max_length=500,verbose_name="Engine Code", null=True, blank=True)
    steering = models.ForeignKey(Steering, verbose_name="Steering", on_delete=models.DO_NOTHING, default="")        
    ExtColor = models.CharField(max_length=500,verbose_name="Ext Color", null=True, blank=True)
    Fuel = models.CharField(max_length=500,verbose_name="Fuel", null=True, blank=True)
    Seats = models.CharField(max_length=500,verbose_name="Seats", null=True, blank=True)
    Door = models.CharField(max_length=500,verbose_name="Door", null=True, blank=True)
    M3 = models.CharField(max_length=500,verbose_name="M3", null=True, blank=True)
    Dimensions = models.CharField(max_length=500,verbose_name="Dimensions", null=True, blank=True)
    Weight = models.CharField(max_length=500,verbose_name="Vehicle Weight", blank=True, null=True)
    MaxCap = models.CharField(max_length=500,verbose_name="Max Capicity", null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name="CountryName", on_delete=models.DO_NOTHING, default="")
    pricerange = models.ForeignKey(PriceRange, verbose_name="Price Range", on_delete=models.DO_NOTHING, default="")
    discount = models.ForeignKey(Discount, verbose_name="By Discount", on_delete=models.DO_NOTHING, default="")
    othercategorie = models.ForeignKey(OtherCategorie, verbose_name="Other Categories", on_delete=models.DO_NOTHING, default="")
    Description = models.TextField(verbose_name="Description", null=True, blank=True)
    Price = models.CharField(max_length=500,verbose_name="Vehicle Price", null=True, blank=True)
    TotalPrice = models.CharField(max_length=500,verbose_name="Total Price", null=True, blank=True)

    @staticmethod
    def get_all_cars():
        return Car.objects.all()

    @staticmethod
    def get_all_cars_by_CompanyId(company_id):
        if company_id:
            return Car.objects.filter(company=company_id)
        else:
            return Car.get_all_cars()

    def __str__(self):
        return self.CarName

class CarImage(models.Model):
    CarImageID = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Car")
    CarImage = models.ImageField(upload_to='productimg', verbose_name="Vehicle Image")

    def __str__(self):
        return self.car.CarName

class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    ReviewHeading = models.CharField(max_length=50, verbose_name="Review Heading")
    UserName = models.CharField(max_length=100, verbose_name="User Name")
    Description = models.TextField()
    Date = models.DateField(auto_now_add=False, blank= True,null=True, verbose_name="Date")
    company = models.ForeignKey(Company, verbose_name="Vehicle Company", on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, verbose_name="Vehicle Name", on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, verbose_name="Country Name", on_delete=models.DO_NOTHING)
    Image = models.ImageField(upload_to='productimg', verbose_name="Review Image")

    def __str__(self):
        return self.ReviewHeading

class QuestionAndAnswer(models.Model):
    QAID = models.AutoField(primary_key=True)
    Question = models.CharField(max_length=200, verbose_name="Question")
    Answer = models.TextField(verbose_name="Answer")

    def __str__(self):
        return self.Question




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(verbose_name="User Name",max_length=20)
    email = models.CharField(verbose_name="Email", max_length=20)
    contact = models.CharField(verbose_name="Contact No", max_length=20)

    def __str__(self):
        return self.userName

class CutomerInvoiceDetail(models.Model):
    CIDID = models.AutoField(primary_key=True)
    User = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    Car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    InvoiceDetail = models.CharField(verbose_name="Invoice Detail", max_length=200)

    def __str__(self):
        return self.InvoiceDetail












