from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from django.views.generic import View,DetailView
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'home.html')

class VoteView(View):
    def get(self,*args,**kwargs):
        form = VotersForm()
        stages = Voter.STAGE_OPTIONS
        context = {
            'form':form,
            'stages':stages,
        }
        return render(self.request,'vote.html',context)
    
    def post(self,*args,**kwargs):
        form = VotersForm(self.request.POST or None)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            reg_no = form.cleaned_data['reg_no']
            departments = form.cleaned_data['departments']
            stage = form.cleaned_data['stage']

            voters = Voter(name=fullname,reg_no=reg_no,department=departments,stage=stage)
            voters.save()
            messages.success(self.request, 'Voter submitted successifully')
            return redirect('candidates',department=departments)

        messages.warning(self.request, 'Invalid form.')
        return redirect('voter')

class CandidatesView(DetailView):
    def get(self, *args, **kwargs):
        department = self.kwargs.get('department', None)  
        male_delegates = Deligate.objects.filter(position='MR')
        female_delegates = Deligate.objects.filter(position='FR')
        academic_delegates = Deligate.objects.filter(position='AR')
        form = VotesForm()
        context = {
            'male_delegates': male_delegates,
            'female_delegates': female_delegates,
            'academic_delegates': academic_delegates,
            'form': form,
            'department': department,
        }
        return render(self.request, 'candidates.html', context)

    def post(self, *args, **kwargs):
        form = VotesForm(self.request.POST or None)
        if form.is_valid():
            male_vote = form.cleaned_data.get('male_vote')
            female_vote = form.cleaned_data.get('female_vote')
            academic_vote = form.cleaned_data.get('academic_vote')

            if male_vote:
                try:
                    male_delegate = Deligate.objects.get(id=male_vote)
                    male_delegate.vote += 1
                    male_delegate.save()
                except Deligate.DoesNotExist:
                    messages.warning(self.request, 'Deligate does not exist')
                    return redirect('candidates',department=self.kwargs.get('department'))


            if female_vote:
                try:
                    female_delegate = Deligate.objects.get(id=female_vote)
                    female_delegate.vote += 1
                    female_delegate.save()
                except Deligate.DoesNotExist:
                    messages.warning(self.request, 'Deligate does not exist')
                    return redirect('candidates',department=self.kwargs.get('department'))

            if academic_vote:
                try:
                    academic_delegate = Deligate.objects.get(id=academic_vote)
                    academic_delegate.vote += 1
                    academic_delegate.save()
                except Deligate.DoesNotExist:
                    messages.warning(self.request, 'Deligate does not exist')
                    return redirect('candidates',department=self.kwargs.get('department'))
                

            messages.success(self.request, 'Thank you for voting')
            return redirect('success')

        messages.warning(self.request, 'Invalid form')
        return redirect('candidates',department=self.kwargs.get('department'))

class SuccessView(View):
    def get(self,*args,**kwargs):
        return render(self.request, 'success.html')

class StudentRegistrationView(View):
    def get(self,*args,**kwargs):
        form = StudentRegistrationForm()
        context = {
            'form':form
        }
        return render(self.request, 'register.html',context)

    def post(self,*args,**kwargs):
        form = StudentRegistrationForm(self.request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email'] 
            reg_no = form.cleaned_data['reg_no']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password == password2:
                if Student.objects.filter(reg_no=reg_no).exists():
                    messages.warning(self.request, 'This registration number already exists')
                    return redirect('register')
                else:
                    student = Student.objects.create(first_name=first_name,last_name=last_name,
                        email=email,reg_no=reg_no,password=password2)
                    student.save()
                    messages.success(self.request, 'Register successifull. Log in here!!')
                    return redirect('register')
            else:
                messages.warning(self.request, 'Password missmatch')
                return redirect('register')
        messages.warning(self.request, 'Invalid form')
        return redirect('register')
    
class StudentLoginView(View):
    def get(self,*args,**kwargs):
        return render(self.request, 'login.html')

    def post(self,*args,**kwargs):
        form = StudentLoginForm(self.request.POST or None)
        if form.is_valid():
            reg_no = form.cleaned_data['reg_no']
            password = form.cleaned_data['password']

            student = authenticate(self.request,username=reg_no, password=password)

            if student is not None:
                login(self.request, student)
                return redirect('home')
            else:
                messages.error(self.request, 'Invalid email or password.')
                return redirect('login')
        messages.warning(self.request, 'Invalid form')
        return redirect('login')
    