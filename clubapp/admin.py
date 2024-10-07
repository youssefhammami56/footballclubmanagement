from django.contrib import admin
from .models import Competition, Notification, Player, Team, WaitingPlayer, Membership

class MembershipInline(admin.TabularInline):
    model = Membership
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Notification Details', {
            'fields': ('title', 'content')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location']
    search_fields = ['name']
    list_filter = ['date']
    date_hierarchy = 'date'    

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'nationality', 'birth_date']
    search_fields = ['name']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'coach', 'stadium']
    search_fields = ['name']
    inlines = [MembershipInline]

@admin.register(WaitingPlayer)
class WaitingPlayerAdmin(admin.ModelAdmin):
    list_display = ['player']
    search_fields = ['player__name']
    actions = ['accept_players']

    def accept_players(self, request, queryset):
        for waiting_player in queryset:
            player = waiting_player.player
            Membership.objects.create(player=player, team=player.team, position=player.position)
        queryset.delete()

    accept_players.short_description = 'Accept selected players'

admin.site.register(Membership)