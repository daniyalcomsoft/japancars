from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Country)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['CountryName','flagImage']

@admin.register(CarType)
class CarTypeModelAdmin(admin.ModelAdmin):
    list_display = ['TypeName']

@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ['CompanyName','CompanyStock','CompanyLogo']

@admin.register(Steering)
class SteeringModelAdmin(admin.ModelAdmin):
    list_display = ['SteeringName']


@admin.register(PriceRange)
class PriceRangeModelAdmin(admin.ModelAdmin):
    list_display = ["Price"]

@admin.register(Discount)
class DiscountModelAdmi(admin.ModelAdmin):
    list_display = ["Discount"]

@admin.register(OtherCategorie)
class OtherCategorieModelAdmin(admin.ModelAdmin):
    list_display = ["OtherCategoryName", "CatImage"]

@admin.register(ManufacturingYM)
class ManufacturigYMModelAdmin(admin.ModelAdmin):
    list_display =["ManufacturingDate"]

@admin.register(Currencies)
class CurrenciesModelAdmin(admin.ModelAdmin):
    list_display =["CurrencyName"]

@admin.register(Languages)
class LanguagesModelAdmin(admin.ModelAdmin):
    list_display=["LanguageName"]

@admin.register(MainHeading)
class MainHeadingModelAdmin(admin.ModelAdmin):
    list_display =["purpose", "stock", "todaystock", "country", "currency", "language"]

@admin.register(ShippingSituation)
class ShippingSituationModelAdmin(admin.ModelAdmin):
    list_display = ["Heading","Description","Date"]

@admin.register(SalesOffice)
class SalesOfficeModelAdmin(admin.ModelAdmin):
    list_display = ["Heading", "Description", "Image"]

@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        'company','CarName','type','ChassisNo','ModelCode','EngineSize','Location','CarImage'
    ]

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):    
    list_display = ["ReviewHeading", "UserName", "Description","Date", "company", "car", "country", "Image"]

# @admin.register(QuestionAndAnswer)
# class QuestionAndAnswerModelAdmin(admin.ModelAdmin):
#     list_display = ["Question", "Answer"] 

@admin.register(CarImage)
class CarImageModelAdmin(admin.ModelAdmin):
    list_display = ["car", "CarImage"]

@admin.register(Users)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ["userName", "email", "contact"]

@admin.register(CutomerInvoiceDetail)
class CutomerInvoiceDetailModelAdmin(admin.ModelAdmin):
    list_display = ["User", "Car", "InvoiceDetail"]