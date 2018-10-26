from django.db import models

# Create your models here.



class Team(models.Model):

    final_score = models.IntegerField(default=0)
    gate_set = models.IntegerField(default=-1)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    score3 = models.IntegerField(default=0)
    round1_done = models.BooleanField(default=False)
    round2_done = models.BooleanField(default=False)
    team_name = models.CharField(max_length=100, unique=True)
    college_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.team_name


class CurrentRound(models.Model):
    round = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
