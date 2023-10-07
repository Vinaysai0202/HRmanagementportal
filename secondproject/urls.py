"""
URL configuration for secondproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from hr_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hr_app/',include('hr_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',views.home,name='Home'),
    path('employee/',views.employee,name='Employee'),
    path('contact/',views.contact_form,name='Contact'),
    path('empdata/',views.employee_list,name='Emp'),
    path('logout/',views.logout,name='Logout'),
    path('hr/',views.hr,name='Hr'),
    # path('news/',views.news,name='News'),
    path('calender/',views.submit_holiday, name='Submit_holiday'),
    path('holiday_list/', views.holiday_list, name='List'),
    path('news/',views.submit_news, name='Submit_news'),
    path('news_list/', views.news_list, name='News_list'),
    path('update_employee/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),






]
