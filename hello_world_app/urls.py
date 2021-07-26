"""django_basics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = "hello_app"
urlpatterns = [
    # Here we should always apply forward slash(i.e "/") at the end of URL(i.e first parameter).
    # However it is not mandatory but can create issue especially in case query parameters is there in URL.
    # But we should never use forward slash(i.e "/") if URL doesn't contain any value i.e in blank urls(Ex :- first URL)
    # This rule is true irrespective of whether the blank URL contains query string or not.
    path('', views.hello, name='hello_world'),
    path('template/', views.hello_template, name='hello_template'),
    path('dynamic/', views.dynamic_template, name='dynamic_template'),
    path('query_param/', views.query_param_data, name='query_string_param'),
    path('data_with_url/<int:id>/<str:name>/', views.data_with_url, name='url_data'),
    path('redirect/', views.redirect_another_page, name='redirect'),
    path('button_redirect', views.redirect_button_click, name='button_redirect'),
    path('simple_form', views.simple_form, name='form_demo')
]
