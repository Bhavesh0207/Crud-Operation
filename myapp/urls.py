from django.urls import path
from .import views

urlpatterns = [
    path('showproduct', views.showproductpage, name="showproduct"),
    path('addproduct', views.addproductpage, name="addproduct"),
    path('insertproductdata', views.insertproductdata, name="insertproductdata"),
    path('manageproduct', views.showmanageproduct, name="manageproduct"),
    path('singleproduct/<int:pid>', views.singleproductpage, name="singleproductpage"),
    path('', views.showloginpage, name="login.html"),
    path('registration.html', views.showregistrationpage, name="registration.html"),
    path('insertlogindata', views.insertlogindata, name="insertlogindata"),
    path('insertregistrationdata', views.insertregistrationdata, name="insertregistrationdata"),
    path('checklogindata', views.checklogindata, name="checklogindata"),
    path('logout', views.logout, name="logout"),
    path('showcart', views.showcart, name="showcart"),
    path('addtocart', views.addtocart, name="addtocart"),
    path('increaseitem/<int:id>', views.increaseitem, name="increase"),
    path('decreaseitem/<int:id>', views.decreaseitem, name="decrease"),
    path('removeitem/<int:id>', views.removeitem, name="remove"),
    path('placeorder', views.fetchorderdetails, name="placeorder"),
    path('profile', views.showprofile, name="showprofile"),
    path('forgotpassword.html', views.forgotpage, name="forgotpassword"),
    path('sendmail', views.forgotpassword, name="sendmail"),
    path('editproduct/<int:id>', views.editproduct, name="editproduct"),
    path('updateproduct', views.updateproduct, name="updateproduct")
]
