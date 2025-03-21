from django.urls import path
from .views import (
    home, submit_success,
    teacher_success, about, contact,  feedback_view
)

urlpatterns = [
    path('', home, name='home'),
    path('submit_success/', submit_success, name='submit_success'),
    path('teacher_success/', teacher_success, name='teacher_success'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('feedback/', feedback_view, name='feedback'),

]
