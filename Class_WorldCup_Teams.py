class team(object):
    def __init__(self, year, team, players):
        self.year = year
        self.team = team
        self.players = players

    def __str__(self):
        return "Year: {}, Team: {}, FullName: {}".format(str(self.year), str(self.team), str(self.players))

    




