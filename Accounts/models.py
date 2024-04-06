from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
# Create your models here.
class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="candidates")
    background_info = models.TextField()
    manifesto = models.TextField()
    photo = models.ImageField(upload_to = "Candidate/photo", null=True, blank=True)
    votes = models.ManyToManyField("Vote", null=True, blank=True)

    def get_percentage_of_total_votes(self):
        # Step 1: Get the total number of votes for the specific candidate
        candidate_votes = self.votes.count()

        # Step 2: Get the total number of votes across all candidates
        total_votes = Candidate.objects.aggregate(total=Count('votes'))['total']

        # Step 3: Calculate the percentage
        if total_votes > 0:
            percentage = (candidate_votes / total_votes) * 100
            return percentage
        else:
            return 0  # Return 0 if there are no votes to prevent division by zero

    
    
    def __str__(self):
        return self.user.username
    
    
    def display_photo(self):
        return self.photo.url if self.photo else '/static/assets/images/default.png'
    

    
class Post(models.Model):
    POST_CHOICES = (
        ("P", "President"),
        ("G", "Governor"),
        ("S", "Senator"),
        ("MP", "Member Of Parliament"),
    )

    title = models.CharField(max_length=100,choices=POST_CHOICES,verbose_name=('Post Vieing For:'),help_text='Select post')

    def __str__(self):
        return self.get_title_display()
    
    def total_votes(self):
        return self.votes.count()
    

class Voter(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to = "Candidate/photo")

    def __str__(self):
        return self.user.username
    
class Vote(models.Model):  
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name='votes', blank=True, null=True)   
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes', blank=True, null=True)   
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.user.username} voted"