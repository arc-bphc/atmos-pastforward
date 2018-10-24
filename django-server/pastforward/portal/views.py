from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegForm
from .models import Team, Contest
from .arduino_functions import phase1, phase2


def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)

        if(form.is_valid()):
            team_name = form.cleaned_data.get('team_name')
            college_name = form.cleaned_data.get('college_name')
            email = form.cleaned_data.get('email')
            contest = Contest.objects.create()
            # TODO: test form working
            try:
                team = Team.objects.create(
                    contest=contest, team_name=team_name, college_name=college_name, email=email)
            except Exception as e:
                new_form = RegForm()
                contest.delete()
                return render(request, 'registration.html', {'form': form, 'msg': 'error', 'team_name': team_name})

            return render(request, 'registration.html', {'form': form, 'msg': 'success', 'team_name': team_name})

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


def leaderboard(request):
    teams = Team.objects.order_by('-contest__score')
    return render(
        request,
        'leaderboard.html',
        context={'teams': teams}
    )


def gameplay(request, team_name, phase=0):

    team = Team.objects.all().filter(team_name=team_name)
    if (phase == 0):
        return render(
            request,
            'gameplay.html',
            context={'team_name': team[0].team_name}
        )

    if(phase == 1):
        phase1_time = phase1()
        return render(
            request,
            'phase1.html',
            context={
                'team_name': team[0].team_name,
                'time': phase1_time,
            }
        )
