from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User

from .models import *


# Create your views here.
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class home(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses
        }
        return render(request, "index.html", context)


class InsidenewsPage(View):
    def get(self, request):
        return render(request, "insidenews.html")


class MissionPage(View):
    def get(self, request):
        return render(request, "mission.html")


class ProfileView(View):
    def get(self, request):
        return render(request, "dash-profile.html")

    def post(self, request):
        data = request.POST
        Profile.objects.create(first_name=data['first_name'], last_name=data['last_name'], birth_date=data['birth_date'], number=data['number'])
        profile = Profile.objects.all()
        context = {
            'profile': profile
        }
        return redirect('profile', context)


class CoursesPage(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses
        }
        return render(request, "courses.html", context)


class CoursesTest(View):
    def get(self, request, id):
        return render(request, "course-test.html")


class CoursePage(View):
    def get(self, request, id):
        courses = Course.objects.filter(id=id)
        context = {
            'courses': courses
        }
        return render(request, "course.html", context)


class NewsPage(View):
    def get(self, request):
        return render(request, "news.html")


class AboutPage(View):
    def get(selfself, request):
        return render(request, "about.html")


class ContactPage(View):
    def get(self, request):
        return render(request, "contact.html")


class GrandPage(View):
    def get(self, request):
        return render(request, "grand.html")


class Registration(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request):
        data = request.POST
        user = User.objects.create_user(username=data['name'], email=data['email'], password=data['password'])
        user.save()
        return redirect('login')


class LoginPage(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('invalid credentials')
        return render(request, 'login.html')


class IndexCourse(View):
    def get(self, request):
        course = Course.objects.all()
        context = {
            'course': course
        }
        return render(request, 'index.html', context)
