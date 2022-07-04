from typing import List
from django.urls import path
from . import views

app_name = "intel_api"

intel_urls = [
    path('labs/list/', views.LabList.as_view(),name="list_labs"),
    

    path('auth/login/', views.IntelAuthLogin.as_view(),name="intel_auth_login"),
    path('auth/logout/', views.IntelAuthLogout.as_view(),name="intel_auth_logout"),
    
    path('userprofile/', views.IntelUserProfileView.as_view(),name="intel_userwprofile"),
    path('user/entity/', views.IntelUserLabView.as_view(),name="intel_user_lab"),


    path('fetch/lab/by/registration/number/', views.IntelGetLabByRegistrationNumberView.as_view(),name="intel_get_lab_by_registration_number"),
    path('fetch/lab/by/lab/name/', views.IntelGetLabByLabNameView.as_view(),name="intel_get_lab_by_lab_name"),
]
