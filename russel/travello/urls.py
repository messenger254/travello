
from django.urls import path

from . import views

app_name = 'travello'

urlpatterns = [
    path("",views.home, name = "home"),
    path("contact/",views.contact, name = "contact"),
    path("about/",views.about, name = "about"),
    path("news/",views.news, name = "news"),
    
    # path("",views.index, name = "index"),
    # path('user/', views.userPage, name="user-page"),
    # path('account/', views.accountSettings, name="account"),
    #
    # path('products/', views.products, name='products'),
    # path('customer/<str:pk>/', views.customer, name="customer"),


    # path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    # path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name= "password_reset_confirm"),
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    #


]
