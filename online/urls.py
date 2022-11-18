from django.urls import path

from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('courses', views.CoursesPage.as_view(), name='courses'),
    path('course-test/<int:id>', views.CoursesTest.as_view(), name='course-test'),
    path('course/<int:id>', views.CoursePage.as_view(), name='course'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('news', views.NewsPage.as_view(), name='news'),
    path('contact', views.ContactPage.as_view(), name='contact'),
    path('grand', views.GrandPage.as_view(), name='grand'),
    path('mission', views.MissionPage.as_view(), name='mission'),
    path('insidenews', views.InsidenewsPage.as_view(), name='insidenews'),
    path('register', views.Registration.as_view(), name='register'),
    path('login', views.LoginPage.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('profile', views.ProfileView.as_view(), name='profile'),

]



