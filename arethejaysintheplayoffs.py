import click
import statsapi


@click.command()
def cli():
    click.echo("Starting MLB")
    data = statsapi.standings_data()
    teams = []
    for key in data:
        for team in data[key]["teams"]:
            teams.append(Team(team["team_id"], key, team["name"], team["div_rank"], team["w"], team["l"]))

    teams = sorted(teams, key=lambda i: i.percent, reverse=True)

    al_west = []
    al_east = []
    al_central = []
    nl_west = []
    nl_east = []
    nl_central = []

    for team in teams:
        if team.division == 200:
            al_west.append(team)
        elif team.division == 201:
            al_east.append(team)
        elif team.division == 202:
            al_central.append(team)
        elif team.division == 203:
            nl_west.append(team)
        elif team.division == 204:
            nl_east.append(team)
        elif team.division == 205:
            nl_central.append(team)

    del al_west[:2]
    del al_east[:2]
    del al_central[:2]
    del nl_west[:2]
    del nl_east[:2]
    del nl_central[:2]

    nl = []
    al = []

    nl.extend(nl_east)
    nl.extend(nl_west)
    nl.extend(nl_central)
    al.extend(al_east)
    al.extend(al_west)
    al.extend(al_central)

    al = sorted(al, key=lambda i: i.percent, reverse=True)
    nl = sorted(nl, key=lambda i: i.percent, reverse=True)

    def first_or_second_in_division():
        for each in al:
            if each.team_id == 141:
                return False
        return True

    if al[0].team_id == 141 or al[1].team_id == 141 or first_or_second_in_division():
        click.echo("Yes")
    else:
        click.echo("No")


class Team:
    def __init__(self, team_id, division, name, rank, wins, losses):
        self.team_id = team_id
        self.division = division
        self.name = name
        self.rank = rank
        self.wins = wins
        self.losses = losses
        self.percent = wins/(wins+losses)
