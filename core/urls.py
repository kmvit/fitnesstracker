from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from core.views import HomeView, EveryDayReportView, EveryWeekReportView, Results, AdminReview, Success, AboutPage

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('everydayreport/', login_required(EveryDayReportView.as_view()), name='everydayreport'),
    path('everyweekreport/', login_required(EveryWeekReportView.as_view()), name='everyweekreport'),
    path('results/', login_required(Results.as_view()), name='results'),
    path('adminreview/', login_required(AdminReview.as_view()), name='admin_review'),
    path('success/', Success.as_view(), name='success'),
    path('about/', AboutPage.as_view(), name='about'),
]
