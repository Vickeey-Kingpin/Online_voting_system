from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from django.views.generic import View,DetailView
from django.contrib import messages
from .models import *

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
            return redirect('candidates')

        messages.warning(self.request, 'Invalid form.')
        return redirect('voter')

# class CandidatesView(DetailView):
#     def get(self,*args,**kwargs):
#         male_delegates = Deligate.objects.filter(position='MR')
#         female_delegates = Deligate.objects.filter(position='FR')
#         form = VotesForm()
#         academic_delegates = Deligate.objects.filter(position='AR')
#         context = {
#             'male_delegates': male_delegates,
#             'female_delegates': female_delegates,
#             'academic_delegates': academic_delegates,
#             'form':form,
#         }
#         return render(self.request, 'candidates.html',context)

#     def post(self,*args,**kwargs):
#         form = VotesForm(self.request.POST or None)
#         if form.is_valid():
#             vote = form.cleaned_data['vote']

#         deligates = Deligate.objects.all()  
#         for deligate in deligates:
#             deligate.vote += 1
#             deligate.save()
#             messages.success(self.request, 'Voted successifully')
#             return redirect('candidates')

#         messages.warning(self.request, 'Invalid form.')
#         return redirect('candidates')

class CandidatesView(DetailView):
    def get(self, *args, **kwargs):
        male_delegates = Deligate.objects.filter(position='MR')
        female_delegates = Deligate.objects.filter(position='FR')
        academic_delegates = Deligate.objects.filter(position='AR')
        form = VotesForm()
        context = {
            'male_delegates': male_delegates,
            'female_delegates': female_delegates,
            'academic_delegates': academic_delegates,
            'form': form,
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
                    pass  

            if female_vote:
                try:
                    female_delegate = Deligate.objects.get(id=female_vote)
                    female_delegate.vote += 1
                    female_delegate.save()
                except Deligate.DoesNotExist:
                    pass  

            if academic_vote:
                try:
                    academic_delegate = Deligate.objects.get(id=academic_vote)
                    academic_delegate.vote += 1
                    academic_delegate.save()
                except Deligate.DoesNotExist:
                    pass  # Handle error, e.g., invalid delegate ID

            messages.success(self.request, 'Votes cast successfully')
            return redirect('candidates')

        messages.warning(self.request, 'Invalid form')
        return redirect('candidates')
