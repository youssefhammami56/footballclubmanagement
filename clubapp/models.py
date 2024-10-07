from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Competition(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()
    #team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, through='Membership')

    def __str__(self):
        return self.name


class WaitingPlayer(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.player)


class Membership(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.player.name} - {self.team.name} ({self.position})"