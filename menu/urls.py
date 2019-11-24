"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from . import views
# from menu.views import Ourservice, ServiceDetail

app_name = 'menu'
urlpatterns = [
path('',                    views.Homebview ,                  name= 'home'),
path('services/',           views.Ourservice.as_view(),        name = 'service'),
path('deteil/<int:question_id>/', views.ServiceDetail	,      name = 'Details'),
path('service_categories',  views.ServiceCategory.as_view(),   name= 'ServiceCategories'),
path('about/',              views.AboutView.as_view(),         name= 'Profile'),
path('team/',               views.TeamView.as_view(),          name='ourteam'),
path('contact/',            views.ContactView,                 name = 'contact'),
path('vision/',             views.visionView.as_view(),        name= 'vision'),
path('associates/',         views.AssociatesView.as_view(),    name  = 'associates'),
path('clients/',            views.ClientsView.as_view(),       name = 'ourclients'),
path('application/<int:apply_id>/', views.Apply_service,          name =  'applications'),
path('clientdetails/<int:client_id>/', views.Client_details,        name= 'Client_detail'),

 ]