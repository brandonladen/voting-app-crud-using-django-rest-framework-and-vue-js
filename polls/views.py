from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Accounts.models import Candidate, Vote, Voter, Post
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from django.db.models import Count, ExpressionWrapper, Case, Value, F, FloatField, When
from django.db.models.functions import Round

# Create your views here.
def home(request):
    candidate_poll = Candidate.objects.all()
    context = {
        'Candidate': candidate_poll
    }
    return render(request, 'polls/index.html', context)

def result(request):
    # Step 1: Retrieve all candidates
    candidates = Candidate.objects.all()

    # Step 2: Calculate percentage for each candidate
    candidates_with_percentage = []
    total_votes = Candidate.objects.aggregate(total_votes=Count('votes'))['total_votes']

    for candidate in candidates:
        candidate_votes = candidate.votes.count()
        percentage_of_votes = round((candidate_votes / total_votes) * 100 ,2)if total_votes > 0 else 0

        candidates_with_percentage.append({
            'candidate': candidate,
            'votes': candidate_votes,
            'percentage_of_votes': percentage_of_votes,
        })

    # Step 3: Pass the information to the template
    context = {
        'candidates_with_percentage': candidates_with_percentage,
    }


    return render(request, 'polls/result.html', context=context)


def candidate_delete(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate.delete()
    return redirect('home')


@login_required
def vote(request, cand_id, post_id):
    candidate = Candidate.objects.filter(pk=cand_id).first()
    post = Post.objects.filter(id=post_id).first()
    voter = Voter.objects.filter(user=request.user).first()
    if candidate.votes.filter(post=post, voter=voter).first() == None:
        messages.success(request, f'You have already voted for {post.get_title_display()}')
    if candidate.votes.filter(voter=voter).first() == None:
        candidate.votes.create(voter=voter)
        messages.success(request, f'Successfully voted for {candidate.user.first_name} {candidate.user.last_name}')
    else:
        messages.info(request, f'You cannot vote for {candidate.user.first_name} {candidate.user.last_name} twice!')
    return redirect('home')

