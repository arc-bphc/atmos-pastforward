from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegForm
<<<<<<< HEAD
from .models import Team, Contest
=======
from .models import Team
>>>>>>> f70f5c50f710cef184e7c730c6a7d216d58af9e9


def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)

        if(form.is_valid()):
            team_name = form.cleaned_data.get('team_name')
            college_name = form.cleaned_data.get('college_name')
            email = form.cleaned_data.get('email')
<<<<<<< HEAD
            contest = Contest.objects.create()
            try:
                team = Team.objects.create(
                    contest=contest, team_name=team_name, college_name=college_name, email=email)
            except Exception as e:
                new_form = RegForm()
                return render(request, 'registration.html', {'form': form, 'msg': 'error', 'team_name': team_name})

            
            return render(request, 'registration.html', {'form': form, 'msg': 'success', 'team_name': team_name})
=======
            try:
                team = Team.objects.create(
                    team_name=team_name, college_name=college_name, email=email)
            except Exception as e:
                return HttpResponse("Team name already exists")

            return HttpResponse("Team registration Successful: {}".format(team_name))
>>>>>>> f70f5c50f710cef184e7c730c6a7d216d58af9e9

    else:
        form = RegForm()

    return render(request, 'registration.html', {'form': form})


def teams(request):
    teams = Team.objects.all()
    return render(
        request,
        'teams.html',
        context={'teams': teams}
    )
<<<<<<< HEAD


def leaderboard(request):
    teams = Team.objects.order_by('-contest__score')
    return render(
        request,
        'leaderboard.html',
        context={'teams': teams}
    )
=======
>>>>>>> f70f5c50f710cef184e7c730c6a7d216d58af9e9
