from django.urls import path
from . views import *


urlpatterns = [
    path('',index),
    path('vote/',VoteView.as_view(),name='vote'),
    path('candidates/<str:department>/', CandidatesView.as_view(), name='candidates'),
    path('success/',SuccessView.as_view(),name='success'),
    path('register/',StudentRegistrationView.as_view(),name='register'),
    path('login/',StudentLoginView.as_view(),name='login'),
]