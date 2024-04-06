from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import LoginForm, CandidateCreationForm, VoterCreationForm
from .models import Voter
from .models import Candidate, Post
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register_candidate(request, candidate_id=0):
    form = CandidateCreationForm()
    if request.method == 'POST':
        if candidate_id == 0:
            form = CandidateCreationForm(request.POST, request.FILES)
            if form.is_valid():
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    messages.info(request, 'Password didn\'t match!')
                    return redirect('register_candidate')
                user = form.save()
                user.set_password(password1)
                Candidate.objects.create(
                    user = user,
                    post = form.cleaned_data['post']
                )
                messages.success(request, 'Candidate created successfully!')
                return redirect('login')
        else:
            candidate = Candidate.objects.get(id=candidate_id)
            form = CandidateCreationForm(request.POST, request.FILES, instance=candidate)
            if form.is_valid:
                form.save()
                messages.success(request, 'Candidate updated successfully!') #added by Brandon
                return redirect('home') #added by Brandon

    context = {
        'form' : form,
        'page_title': 'Candidate Registration Form',
    }
    return render(request, 'accounts/candidate_creation_form.html', context)



def register_voter(request, voter_id=0):
    form = VoterCreationForm()
    if request.method == 'POST':
        if voter_id == 0:
            form = VoterCreationForm(request.POST, request.FILES)
            if form.is_valid():
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    messages.info(request, 'Passwords don\'t match!')
                    return redirect('register_voter')
                user = form.save()
                user.set_password(password1)
                Voter.objects.create(
                    user = user,
                )
                messages.success(request, "Voter created successfully!")
                return redirect('login')
            else:
                voter = Voter.objects.get(id=voter_id)
                form = VoterCreationForm(request.POST, request.FILES, instance=voter)
                if form.is_valid():
                    form.save()
    context = {
        'form' : form,
        'page_title': 'Voter Registration Form',
    }
    return render(request, 'accounts/candidate_creation_form.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form,'page_title':'Login Page'})

def logout_user(request):
    logout(request)
    return redirect('home')



from django.views.generic import TemplateView, View, DeleteView
from django.http import JsonResponse

class CrudView(TemplateView):
    template_name = 'accounts/ajx.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Candidate.objects.all()
        return context
    
class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Candidate.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)
    
class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Candidate.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)
    
class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Candidate.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
