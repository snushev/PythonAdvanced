def team_lineup(*args):
    teams = {}
    for player, country in args:
        if country not in teams:
            teams[country] = []
        teams[country].append(player)

    sorted_teams = sorted(teams.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for country, players in sorted_teams:
        result.append(f"{country}:")
        for player in players:
            result.append(f"  -{player}")

    return '\n'.join(result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
