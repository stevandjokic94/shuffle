from django.db import models

# Create your models here.
from django.utils.functional import cached_property
from django.utils.text import slugify


class Team(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('team.views.details', args=[str(self.id)])


class Game(models.Model):
    home = models.ForeignKey(Team, related_name='home_team', on_delete=models.CASCADE)
    away = models.ForeignKey(Team, related_name='away_team', on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    season = models.CharField(default='2019/20', max_length=10)

    @cached_property
    def opponent(self):
        if self.home.name == 'Shuffle':
            return self.away.name
        else:
            return self.home.name

    @cached_property
    def outcome(self):
        if self.home.name == 'Shuffle':
            if self.home_score > self.away_score:
                return 'W'
            else:
                return 'L'
        if self.away.name == 'Shuffle':
            if self.home_score > self.away_score:
                return 'L'
            else:
                return 'W'

    def __str__(self):
        return self.home.name + " " + str(self.home_score) + " : " + str(self.away_score) + " " + self.away.name + " " +\
               str(self.pk)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('game.views.details', args=[str(self.id)])


class Player(models.Model):
    name = models.CharField(max_length=40)
    number = models.IntegerField()
    height = models.IntegerField()
    position = models.CharField(max_length=20)
    image = models.ImageField()
    current = models.BooleanField(default=True)

    avg_min = models.FloatField(editable=False, default=0)
    avg_pts = models.FloatField(editable=False, default=0)
    avg_off_reb = models.FloatField(editable=False, default=0)
    avg_def_reb = models.FloatField(editable=False, default=0)
    avg_tot_reb = models.FloatField(editable=False, default=0)
    avg_ass = models.FloatField(editable=False, default=0)
    avg_stl = models.FloatField(editable=False, default=0)
    avg_blk = models.FloatField(editable=False, default=0)
    avg_tos = models.FloatField(editable=False, default=0)
    avg_ft = models.FloatField(editable=False, default=0)
    avg_2fg = models.FloatField(editable=False, default=0)
    avg_2fgm = models.FloatField(editable=False, default=0)
    avg_2fga = models.FloatField(editable=False, default=0)
    avg_3fgm = models.FloatField(editable=False, default=0)
    avg_3fga = models.FloatField(editable=False, default=0)
    avg_ftm = models.FloatField(editable=False, default=0)
    avg_fta = models.FloatField(editable=False, default=0)
    avg_3fg = models.FloatField(editable=False, default=0)
    avg_fg = models.FloatField(editable=False, default=0)
    avg_pir = models.FloatField(editable=False, default=0)

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Player, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('player.views.details', kwargs={'slug': self.slug, 'id': self.id})


class GameStats(models.Model):
    player = models.ForeignKey(Player, related_name='gamestats', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    season = models.CharField(default='2019/20', max_length=20)

    def_rebounds = models.IntegerField()
    off_rebounds = models.IntegerField()
    assists = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    tos = models.IntegerField()

    fg2m = models.IntegerField()
    fg2a = models.IntegerField()
    fg3m = models.IntegerField()
    fg3a = models.IntegerField()
    ftm = models.IntegerField()
    fta = models.IntegerField()

    @cached_property
    def points(self):
        return self.fg2m * 2 + self.fg3m * 3 + self.ftm

    @cached_property
    def pir(self):
        return 3 * self.fg2m + 4 * self.fg3m + 2 * self.ftm + self.def_rebounds + self.off_rebounds + self.assists \
            + self.steals + self.blocks - self.tos - self.fg2a - self.fg3a - self.fta

    @cached_property
    def avg_2fg(self):
        if self.fg2m == 0:
            return 0
        else:
            return round(round(float(self.fg2m) / float(self.fg2a), 3) * 100, 1)

    @cached_property
    def avg_3fg(self):
        if self.fg3m == 0:
            return 0
        else:
            return round(round(float(self.fg3m) / float(self.fg3a), 3) * 100, 2)

    @cached_property
    def avg_fg(self):
        if self.fg2m == 0 and self.fg3m == 0:
            return 0
        else:
            return round(round(float(self.fg2m + self.fg3m) / float(self.fg2a + self.fg3a), 3) * 100, 1)

    @cached_property
    def ft(self):
        if self.ftm == 0:
            return 0
        else:
            tot = round((float(self.ftm) / float(self.fta)), 3)
            return round(tot * 100, 1)

    @cached_property
    def tot_reb(self):
        return self.off_rebounds + self.def_rebounds

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('player.views.details', args=[str(self.id)])

    def __str__(self):
        return self.player.name + " at " + self.game.__str__()


class Gallery(models.Model):
    players = models.ManyToManyField(Player)
    img = models.ImageField(upload_to='images/')
