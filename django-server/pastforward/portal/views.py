from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegForm
from .models import Team, Contest


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
            try:
                team = Team.objects.create(
                    contest=contest, team_name=team_name, college_name=college_name, email=email)
            except Exception as e:
                new_form = RegForm()
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
