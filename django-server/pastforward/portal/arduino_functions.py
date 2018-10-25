import time
import subprocess
import threading

from .models import CurrentRound


def phase1(team_name):
    running = CurrentRound.objects.all()
    if (len(running) == 0):
        CurrentRound.objects.create(team=team_name, round="1")
        threading.Thread(target=threadPhase1).start()


def threadPhase1():
    subprocess.run(["python2", "portal/phase1.py"])


def phase2(team_name):
    running = CurrentRound.objects.all()
    if (len(running) == 0):
        CurrentRound.objects.create(team=team_name, round="2")
        threading.Thread(target=threadPhase2).start()


def threadPhase2():
    subprocess.run(["python2", "portal/phase2.py"])
