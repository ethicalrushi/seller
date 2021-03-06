"""amazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from basic_app import views
from django.conf.urls import url
from Loginapp.views import user_login, register, user_logout

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^product/',views.product, name='product'),
    url(r'^sell/',views.seller, name='seller'),
    url(r'^$', include('basic_app.urls')),
    url(r'^Loginapp/', include('Loginapp.urls')),
    url(r'^electronics/',views.elex, name='electronics'),
    url(r'^books/',views.books, name='books'),
    url(r'^fashion/',views.fashion, name='fashion'),
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/',views.bag, name='cart'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
