from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("product/", views.store, name="product"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path("contact/", views.contact, name="contact"),
    path("feedback/", views.feedback, name="feedback"),
    path("map/", views.map, name="map"),
    path("payment/", views.payment, name="payment"),    
]
