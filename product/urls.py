
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
	# Invoice
	path('Tax1',Tax1, name='Tax1-page'),
	# Add customer
	path('AddCustomer',AddCustomer,name='AddCustomer-page'),
	path('ShowCustomer',ShowCustomer,name='ShowCustomer-page'),
	# Export Quotation
	path('ExportDoc',GENPDF, name='Report-page'),
	path('ExportDoc2',GENPDF2, name='Report2-page'),
	path('ExportDoc3',GENPDF3, name='Report3-page'),
	# Export Invoice
	path('ExportInv',GENINV, name='Invreport-page'),
	# Export ธฟป
	path('ExportTax',GENTAX, name='Taxreport-page'),
   

]