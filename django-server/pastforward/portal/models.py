from django.db import models

# Create your models here.


class Contest(models.Model):
    score = models.DecimalField(default=0, decimal_places=2, max_digits=5)


class Team(models.Model):
    contest = models.OneToOneField(
        Contest,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    team_name = models.CharField(max_length=100, unique=True)
    college_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.team_name
