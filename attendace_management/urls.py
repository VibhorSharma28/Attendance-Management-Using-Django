"""attendace_management URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from records.views import (
	import_view,
    all_names_view,
    detail_view,
    holiday_view,
    update_view,
	)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/',import_view),
    path('',import_view),
    path('list/',all_names_view,name="list"),
    path('list/detail.html/<int:my_id>',detail_view),
    path('setHolidays/',holiday_view),
    path('list/save.html/<int:this_id>',update_view),
]