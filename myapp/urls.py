from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.product_list, name='product-list'), 
    path('create-product/', views.form_product, name='product-create'), 
    path('export-csv/', views.export_csv, name='export-csv'),
    path('export-pdf/', views.export_pdf, name='export-pdf'),    
]