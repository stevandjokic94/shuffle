from django.views import generic
from .models import GameStats


def get_avg_pts(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.points
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_min(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.minutes
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_def_reb(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.def_rebounds
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_off_reb(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.off_rebounds
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_tot_reb(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.off_rebounds + game.def_rebounds
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_ass(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.assists
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_stl(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.steals
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_blk(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.blocks
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_tos(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot = 0
    for game in games:
        tot += game.tos
    try:
        return round(float(tot) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_ft(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    tot_att = 0
    for game in games:
        tot_made += game.ftm
        tot_att += game.fta
    try:
        return round(float(tot_made) / float(tot_att) * 100, 2)
    except:
        return round(0, 2)


def get_avg_ftm(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    for game in games:
        tot_made += game.ftm
    try:
        return round(float(tot_made) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_fta(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    for game in games:
        tot_made += game.fta
    try:
        return round(float(tot_made) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_2fg(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    tot_att = 0
    for game in games:
        tot_made += game.fg2m
        tot_att += game.fg2a
    try:
        return round(float(tot_made) / float(tot_att), 2) * 100
    except:
        return round(0, 2)


def get_avg_2fgm(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    for game in games:
        tot_made += game.fg2m
    try:
        return round(float(tot_made) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_2fga(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    for game in games:
        tot_made += game.fg2a
    try:
        return round(float(tot_made) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_3fg(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    tot_att = 0
    for game in games:
        tot_made += game.fg3m
        tot_att += game.fg3a
    try:
        return round(float(tot_made) / float(tot_att), 2) * 100
    except:
        return round(0, 2)


def get_avg_3fgm(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    for game in games:
        tot_made += game.fg3m
    try:
        return round(float(tot_made) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_3fga(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    for game in games:
        tot_made += game.fg3a
    try:
        return round(float(tot_made) / float(len(games)), 2)
    except:
        return round(0, 2)


def get_avg_fg(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_made = 0
    tot_att = 0
    for game in games:
        tot_made += game.fg2m + game.fg3m
        tot_att += game.fg2a + game.fg3a
    try:
        return round(float(tot_made) / float(tot_att), 2) * 100
    except:
        return round(0, 2)


def get_avg_pir(pk):
    games = GameStats.objects.filter(player__pk=pk).filter(game__season='2019/20')
    tot_pir = 0
    for game in games:
        tot_pir += 2 * game.fg2m + 3 * game.fg3m + game.ftm + game.def_rebounds + game.off_rebounds + game.assists + \
               game.steals + game.blocks - game.tos - game.fg2a - game.fg3a - game.fta
    try:
        return round(float(tot_pir) / float(len(games)), 2)
    except:
        return round(0, 2)
