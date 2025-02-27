from django.contrib import admin
from .models import product, login, registration, carttable, ordertable
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Register your models here

def export_to_pdf(modeladmin, request, queryset):
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.black),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.white),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])


   headers = ['productname', 'productprice', 'productdesc']

   data = []
   for obj in queryset:
       data.append([obj.productname, obj.productprice, obj.productdesc])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response


export_to_pdf.short_description = "Export to PDF"


class showproduct(admin.ModelAdmin):
    list_display = ["productname", "productprice", "productdesc", "product_photo"]
    list_filter = ['productname']
    list_filter = ['productprice']
    list_filter = ['productdesc']
    actions = [export_to_pdf]
admin.site.register(product, showproduct)


class showlogin(admin.ModelAdmin):
    list_display = ["email", "password"]
    list_filter = ['email']
    list_filter = ['password']
    actions = [export_to_pdf]
admin.site.register(login, showlogin)

class showregistration(admin.ModelAdmin):
    list_display = ["name", "email", "password", "gender", "phone_number", "address", "role", "product_photo"]
    list_filter = ['name']
    list_filter = ['email']
    list_filter = ['password']
    list_filter = ['gender']
    list_filter = ['phone_number']
    list_filter = ['address']
    list_filter = ['role']
    actions = [export_to_pdf]
admin.site.register(registration, showregistration)


class showcarttable(admin.ModelAdmin):
    list_display = ["userid", "productid", "quantity", "totalamount", "cartstatus", "orderid"]
    list_filter = ['userid']
    list_filter = ['productid']
    list_filter = ['quantity']
    list_filter = ['totalamount']
    list_filter = ['cartstatus']
    list_filter = ['orderid']
    actions = [export_to_pdf]
admin.site.register(carttable, showcarttable)


class showordertable(admin.ModelAdmin):
    list_display = ["userid", "finaltotal", "paymode"]
    list_filter = ['userid']
    list_filter = ['finaltotal']
    list_filter = ['paymode']
    actions = [export_to_pdf]
admin.site.register(ordertable, showordertable)

