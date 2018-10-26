from random import randint

from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegForm
from .models import Team, CurrentRound
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
            
            # TODO: test form working
            try:
                gate_set = randint(0, 9)
                team = Team.objects.create(
                    team_name=team_name, college_name=college_name, email=email, gate_set=gate_set)
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
    teams = Team.objects.order_by('-final_score')
    return render(
        request,
        'leaderboard.html',
        context={'teams': teams}
    )


def round1(request, team_name):
    running = CurrentRound.objects.all()
    team = Team.objects.all().filter(team_name=team_name)[0]

    if(team.round1_done is True):
        return renderDefault(request, "Round 1 already done. \nDelete from admin panel to start again.")

    if(len(running) == 0):
        file = open("portal/output1.txt", "w")
        file.write("")
        file.close()
        phase1(team_name)
        text = team_name + ": Round2 Started"
        return render(
            request,
            'round.html',
            context={'text': text},
        )
    else:
        file = open("portal/output1.txt", "r")
        text = file.read()
        if (len(CurrentRound.objects.all()) == 0):
            text = "Release the Monitor"
        return render(
            request,
            'round.html',
            context={'text': text},
        )


def deleteMonitor(request):
    running = CurrentRound.objects.all()
    if(len(running) > 0):
        running[0].delete()
        return renderDefault(request, "Monitor Released")
    else:
        return renderDefault(request, "Monitor already Released")


def round2(request, team_name):

    team = Team.objects.all().filter(team_name=team_name)[0]

    if(team.round2_done is True):
        return renderDefault(request, "Round 2 already done. Delete from admin panel to start again.")


    running = CurrentRound.objects.all()
    if(len(running) == 0):
        file = open("portal/output2.txt", "w")
        file.write("")
        file.close()
        phase2(team_name)
        text = team_name + ": Round2 Started"
        return render(
            request,
            'round.html',
            context={'text': text},
        )
    else:
        file = open("portal/output2.txt", "r")
        text = file.read()
        if (len(CurrentRound.objects.all()) == 0):
            text = "Release the Monitor"
        return render(
            request,
            'round.html',
            context={'text': text},
        )


def renderDefault(request, text):
    return render(
        request,
        'response.html',
        context={'text': text}
    )
