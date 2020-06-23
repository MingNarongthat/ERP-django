
from django.urls import path

from django.conf.urls import url
from .views import *

urlpatterns = [
    path('',Document, name='Doc-page'),
    path('Document',Document, name='Doc-page'),
    path('Document2',Document2, name='Doc2-page'),
    path('ExportDoc',GENPDF, name='Report-page'),
    path('ExportDoc2',GENPDF2, name='Report2-page'),
    

]