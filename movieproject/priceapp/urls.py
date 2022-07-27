from django.urls import path,include
from  . import views
app_name='priceapp'
urlpatterns = [
    path('', views.index2, name='index2'),
    path('product/<int:product_id>/', views.detail2, name='detail2'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>/', views.update2, name='update2'),
    path('delete/<int:id>/', views.delete2, name='delete2')

]
