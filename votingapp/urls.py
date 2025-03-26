from django.urls import path
from . views import *


urlpatterns = [
    path('',index),
    path('vote/',VoteView.as_view(),name='vote'),
    path('candidates/',CandidatesView.as_view(),name='candidates')
]