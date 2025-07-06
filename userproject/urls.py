from django.contrib import admin
from django.urls import path, include
from accounts.views import home, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('', include('accounts.urls')),  # <-- penting untuk route lain seperti signup/, users/, dll.
]