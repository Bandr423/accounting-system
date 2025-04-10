from .views import financial_report

urlpatterns += [
    path('report/', financial_report, name='financial_report'),
]