from django.views import generic
from .models import Player, Game, GameStats, Gallery
from operator import itemgetter
from . import utils

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'team/index.html'
    model = Player
    context_object_name = 'all_players'

    latest_game = None
    try:
        latest_game = Game.objects.order_by('-id')[0]
    except:
        latest_game = 'No games in DB'
    try:
        game_stats = GameStats.objects.filter(game=latest_game)
    except:
        game_stats = []
    # Ne moze da se sortira po property-u, pa mora for petlja
    max = 0
    for index in range(len(game_stats)):
        if game_stats[index].pir > max:
            max = game_stats[index].pir
            mvp = game_stats[index]

    pts_leaders = None
    # try:
    pts_leaders = []
    try:
        for player in Player.objects.all():
            player.avg_pts = utils.get_avg_pts(player.pk)
            player.save()
            pts_leaders.append((player, player.avg_pts))
        pts_leaders.sort(key=itemgetter(1), reverse=True)
    except:
        pts_leaders = 'Not enough data for points'

    ass_leaders = None
    try:
        ass_leaders = []
        for player in Player.objects.all():
            player.avg_ass = utils.get_avg_ass(player.pk)
            player.save()
            ass_leaders.append((player, player.avg_ass))
        ass_leaders.sort(key=itemgetter(1), reverse=True)
    except:
        ass_leaders = 'Not enough data for assists'
    reb_leaders = None
    try:
        reb_leaders = []
        for player in Player.objects.all():
            player.avg_tot_reb = utils.get_avg_tot_reb(player.pk)
            player.save()
            reb_leaders.append((player, player.avg_tot_reb))
        reb_leaders.sort(key=itemgetter(1), reverse=True)
    except:
        ass_leaders = 'Not enough data for rebounds'

    stl_leaders = None
    try:
        stl_leaders = []
        for player in Player.objects.all():
            player.avg_stl = utils.get_avg_stl(player.pk)
            player.save()
            stl_leaders.append((player, player.avg_stl))
        stl_leaders.sort(key=itemgetter(1), reverse=True)
    except:
        ass_leaders = 'Not enough data for steals'

    blk_leaders = None
    try:
        blk_leaders = []
        for player in Player.objects.all():
            player.avg_blk = utils.get_avg_blk(player.pk)
            player.save()
            blk_leaders.append((player, player.avg_blk))
        blk_leaders.sort(key=itemgetter(1), reverse=True)
    except:
        blk_leaders = 'Not enough data for blocks'

    fg3_leaders = None
    try:
        fg3_leaders = []
        for player in Player.objects.all():
            player.avg_3fg = utils.get_avg_3fgm(player.pk)
            player.save()
            fg3_leaders.append((player, player.avg_3fg))
        fg3_leaders.sort(key=itemgetter(1), reverse=True)
    except:
        fg3_leaders = 'Not enough data for threes'

    try:
        for player in Player.objects.all():
            player.avg_fg = utils.get_avg_fg(player.pk)
            player.avg_min = int(utils.get_avg_min(player.pk))

            player.avg_2fgm = utils.get_avg_2fgm(player.pk)
            player.avg_2fga = utils.get_avg_2fga(player.pk)
            player.avg_2fg = utils.get_avg_2fg(player.pk)

            player.avg_3fg = utils.get_avg_3fg(player.pk)
            player.avg_3fgm = utils.get_avg_3fgm(player.pk)
            player.avg_3fga = utils.get_avg_3fga(player.pk)

            player.avg_ftm = utils.get_avg_ftm(player.pk)
            player.avg_fta = utils.get_avg_fta(player.pk)
            player.avg_ft = utils.get_avg_ft(player.pk)

            player.avg_def_reb = utils.get_avg_def_reb(player.pk)
            player.avg_off_reb = utils.get_avg_off_reb(player.pk)

            player.avg_tos = utils.get_avg_tos(player.pk)
            player.avg_pir = utils.get_avg_pir(player.pk)

            player.save()
    except:
        pass

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_game'] = self.latest_game
        context['mvp'] = self.mvp
        context['pts_leaders'] = self.pts_leaders
        context['ass_leaders'] = self.ass_leaders
        context['reb_leaders'] = self.reb_leaders
        context['fg3_leaders'] = self.fg3_leaders
        context['stl_leaders'] = self.stl_leaders
        context['blk_leaders'] = self.blk_leaders

        return context


class GamesView(generic.ListView):
    model = Game
    template_name = 'team/games.html'
    context_object_name = 'games'


class GameStatsView(generic.DetailView):
    model = Game
    template_name = 'team/game-stats.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super(GameStatsView, self).get_context_data(**kwargs)
        stats = GameStats.objects.filter(game=self.object)
        context['gamestats'] = stats

        points = 0
        fg2m = 0
        fg2a = 0
        fg3m = 0
        fg3a = 0
        ftm = 0
        fta = 0
        tot_reb = 0
        pir = 0
        off_r = 0
        def_r = 0
        ass = 0
        stl = 0
        blk = 0
        tos = 0

        for stat in stats:
            points += stat.points
            fg2m += stat.fg2m
            fg2a += stat.fg2a
            fg3m += stat.fg3m
            fg3a += stat.fg3a
            ftm += stat.ftm
            fta += stat.fta
            tot_reb += stat.off_rebounds + stat.def_rebounds
            pir += stat.pir
            off_r += stat.off_rebounds
            def_r += stat.def_rebounds
            ass += stat.assists
            stl += stat.steals
            blk += stat.blocks
            tos += stat.tos

        context['points'] = points
        context['fg2m'] = fg2m
        context['fg2a'] = fg2a
        context['avg_2fg'] = round(float(fg2m) / float(fg2a) * 100, 1)
        context['avg_fg'] = round(float(fg2m + fg3m) / float(fg2a + fg3a) * 100, 1)
        context['fg3m'] = fg3m
        context['fg3a'] = fg3a
        context['avg_3fg'] = round(float(fg3m) / float(fg3a) * 100, 1)
        context['ftm'] = ftm
        context['fta'] = fta
        context['ft'] = round(float(ftm) / float(fta) * 100, 1)
        context['def_reb'] = def_r
        context['off_reb'] = off_r
        context['rebounds'] = tot_reb
        context['assists'] = ass
        context['steals'] = stl
        context['blocks'] = blk
        context['tos'] = tos
        context['pir'] = pir

        return context


class TeamStatsView(generic.ListView):
    model = Player
    template_name = 'team/stats.html'
    context_object_name = 'players'


class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'team/detail.html'


class PlayersView(generic.ListView):
    model = Player
    template_name = 'team/players.html'
    context_object_name = 'all_players'


class GalleryView(generic.ListView):
    template_name = 'team/gallery.html'
    context_object_name = 'all_images'

    def get_queryset(self):
        return Gallery.objects.all()
