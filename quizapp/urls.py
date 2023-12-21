from django.urls import path, include

from .views import question, qiuz, ResultList

urlpatterns = [
    path('', qiuz, name='qiuz'),
    path('quiz/<int:pk>/', question, name='quistion'),
    path('results/', ResultList.as_view(), name='results'),

]
