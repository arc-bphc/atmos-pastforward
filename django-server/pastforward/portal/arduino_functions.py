import time
import subprocess
import threading

from .models import CurrentRound, Team


def phase1(team_name):
    running = CurrentRound.objects.all()
    if (len(running) == 0):
        CurrentRound.objects.create(team=team_name, round="1")
        threading.Thread(target=threadPhase1, args=(team_name,)).start()


def threadPhase1(team_name):
    print(team_name)
    team = Team.objects.all().filter(team_name=team_name)[0]
    file = open("portal/gate.txt", 'w')
    file.write(str(team.gate_set))
    file.close()
    print("team name: " + team_name)
    subprocess.run(["python2", "portal/phase1.py"])
    file = open("portal/score.txt", "r")
    a = file.read()
    team.score1 = int(a)
    team.final_score = team.score1 + team.score2
    team.round1_done = True
    team.save()
    file.close()


def phase2(team_name):
    running = CurrentRound.objects.all()
    if (len(running) == 0):
        CurrentRound.objects.create(team=team_name, round="2")
        threading.Thread(target=threadPhase2, args=(team_name,)).start()


def threadPhase2(team_name):
    team = Team.objects.all().filter(team_name=team_name)[0]
    file = open("portal/gate.txt", 'w')
    file.write(str(team.gate_set))
    file.close()
    subprocess.run(["python2", "portal/phase2.py"])
    file = open("portal/score.txt", "r")
    a = file.read()
    team.score2 = int(a)
    team.final_score = team.score2 + team.score1
    team.round2_done = True
    team.save()
    file.close()

