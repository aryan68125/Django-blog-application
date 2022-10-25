from django.urls import path
# from django.conf.urls import url is depriciated hence use this instead
from django.urls import re_path as url

'''import TaskList class from views.py into this urls.py file of the application'''
from . import views

'''we can actually use the views directly
    path('logout/', LogoutView.as_view(next_page = 'login' ), name='logout'), will use the LogoutView directly
    next_page = 'login' means once we press login button in pur front end it should send the user back to the login page
'''
from django.contrib.auth.views import LogoutView

'''
TaskList is a class in our views.py but our urls.py of our app cannot use class in here so we will have to modify
the code for the url from this 'example url =     path('add_todo/',views.add_todo, name="add_todo"),'
to this 'exaple url = path('', TaskList.as_view(), name='tasks'),'

view by default looks for pk value
path('task/<int:pk>/', TaskDetail.as_view(), name='tasks'),
'''

#here use a decorateor that will allow su to use pi calls to validate username
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    #url routes related to user registration ,login and password reset functions of the website
    path('register', views.RegistrationView.as_view() , name='register'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
    path('success', views.SuccessView.as_view() , name='success'),
    path('request-reset-email', views.RequestResetEmailView.as_view(), name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>', views.SetNewPasswordView.as_view(), name='set-new-password'),
    path('login', views.LoginView.as_view() , name='login'),
    path('logout', views.LogoutView.as_view() , name='logout'),

    #url routes related to username and email validation in real time
    path('validate-username/', csrf_exempt(views.UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email/', csrf_exempt(views.EmailValidationView.as_view()), name='validate-email'),
]
