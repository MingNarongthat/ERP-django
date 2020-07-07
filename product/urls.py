
from django.urls import path

from django.conf.urls import url
from .views import *

urlpatterns = [
	path('',Document, name='Doc-page'),
	# Quotation
	path('Document',Document, name='Doc-page'),
	path('Document2',Document2, name='Doc2-page'),
	path('newProduct',newProduct, name='newProduct-page'),
	# Invoice
	path('Invoice1',Invoice1, name='Inv1-page'),
	path('Invoice2',Invoice2, name='Inv2-page'),
	path('InvoiceNew',InvoiceNew, name='Inv3-page'),
	# Invoice
	path('Tax1',Tax1, name='Tax1-page'),
	path('Tax2',Tax2, name='Tax2-page'),
	path('TaxNew',TaxNew, name='Tax3-page'),
	# Add customer
	path('AddCustomer',AddCustomer,name='AddCustomer-page'),
	path('ShowCustomer',ShowCustomer,name='ShowCustomer-page'),
	# Export Quotation
	path('ExportDoc',GENPDF, name='Report-page'),
	path('ExportDoc2',GENPDF2, name='Report2-page'),
	path('ExportDoc3',GENPDF3, name='Report3-page'),
	# Export Invoice
	path('ExportInv',GENINV, name='Invreport-page'),
	path('ExportInv2',GENINV2, name='Inv2report-page'),
	path('ExportInv3',GENINV3, name='Inv3report-page'),
	# Export ธฟป
	path('ExportTax',GENTAX, name='Taxreport-page'),
	path('ExportTax2',GENTAX2, name='Tax2report-page'),
	path('ExportTax3',GENTAX3, name='Tax3report-page'),
   

]