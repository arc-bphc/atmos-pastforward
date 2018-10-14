from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    college_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.team_name
