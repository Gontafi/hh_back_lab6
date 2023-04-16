from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>', views.CompanyDetail.as_view(), name='company-detail'),
    path('companies/<int:pk>/vacancies/', views.VacancyByCompanyList.as_view(), name='vacanvies-by-company-list'),
    path('vacancies/', views.VacancyList.as_view(), name='vacancies-list'),
    path('vacancies/<int:pk>', views.VacancyDetail.as_view(), name='vacanvies-detail'),
    path('vacancies/top_ten', views.TopTenVacancies.as_view(), name='top-ten-vacanvies-by-salary'),
    path('vacancies/<int:id>/submit', views.VacancySubmit.as_view(), name='vacancy-sumbit'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]