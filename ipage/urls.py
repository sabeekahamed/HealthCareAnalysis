
from django.urls import path
from ipage.views import login,ppage,admin,search,questions,iresult,dr
urlpatterns = [
    path('admin/',admin.as_view()),
    path('',login.as_view()),
    path('ppage/',ppage.as_view()),
    path('search/',search.as_view(),name = 'search'),
    path('questions/',questions.as_view(),name = 'questions'),
    path('iresult/',iresult.as_view(),name = 'iresult'),
    path('dr/',dr.as_view(),name = 'dr'),
]
