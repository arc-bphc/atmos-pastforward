from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegForm
from .models import Team


def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)

        if(form.is_valid()):
            team_name = form.cleaned_data.get('team_name')
            college_name = form.cleaned_data.get('college_name')
            email = form.cleaned_data.get('email')
            try:
                team = Team.objects.create(
                    team_name=team_name, college_name=college_name, email=email)
            except Exception as e:
                return HttpResponse("Team name already exists")

            return HttpResponse("Team registration Successful: {}".format(team_name))

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
