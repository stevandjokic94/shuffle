from django.contrib import admin
from .models import Team, Game, GameStats, Player, Gallery
# Register your models here.


class GSInline(admin.StackedInline):
    model = GameStats
    extra = 1


class GameAdmin(admin.ModelAdmin):
    inlines = [GSInline]


admin.site.register(Game, GameAdmin)
admin.site.register(Team)
admin.site.register(Gallery)
admin.site.register(Player)