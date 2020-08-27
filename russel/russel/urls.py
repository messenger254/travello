
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('travello/',include('travello.urls', namespace = "travello")),
    path('admin/', admin.site.urls),
    path('',include('accounts.urls', namespace = "accounts")),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
