from django.db import models

# Create your models here.


<<<<<<< HEAD
class Contest(models.Model):
    score = models.DecimalField(default=0, decimal_places=2, max_digits=5)


class Team(models.Model):
    contest = models.OneToOneField(
        Contest,
        on_delete=models.CASCADE,
        primary_key=True,
    )
=======
class Team(models.Model):
>>>>>>> f70f5c50f710cef184e7c730c6a7d216d58af9e9
    team_name = models.CharField(max_length=100, unique=True)
    college_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.team_name
