from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('request-job/', views.company_request, name='company_request'),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/jobs/', views.manage_jobs, name='manage_jobs'),
    path('dashboard/jobs/add/', views.add_job, name='add_job'),
    path('dashboard/jobs/edit_job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('dashboard/jobs/delete_application/<int:job_id>/', views.delete_application, name='delete_application'),
    path('dashboard/jobs/toggle/<int:job_id>/', views.toggle_job_status, name='toggle_job_status'),
    path('dashboard/applications/', views.view_applications, name='view_applications'),
    path('dashboard/company-requests/', views.view_company_requests, name='view_company_requests'),
    path('company/<int:request_id>/', views.show_company_request, name='show_company_request'),
    path('company/<int:request_id>/accept/', views.accept_company_request, name='accept_company_request'),
    path('company/<int:request_id>/reject/', views.reject_company_request, name='reject_company_request'),
    path('company/<int:request_id>/mark-signed/', views.mark_contract_signed, name='mark_contract_signed'),    
    path('dashboard/accepted-companies/', views.accepted_companies, name='accepted_companies'),


]
