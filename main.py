import random

def simulate_snake_draft(teams, players_pool, rounds_per_team):
    """
    Simulates a snake draft process for fantasy football.
    Each team picks players in a specific order, which reverses each round.
    """
    team_rosters = {team_name: [] for team_name in teams}
    available_players = list(players_pool) # Create a mutable copy of the player pool
    draft_log = []

    print("--- Starting Snake Draft Simulation ---")
    print(f"Teams participating: {', '.join(teams)}")
    print(f"Total players available: {len(available_players)}")
    print(f"Rounds per team: {rounds_per_team}\n")

    for round_num in range(1, rounds_per_team + 1):
        print(f"--- Round {round_num} ---")

        # Determine the picking order for the current round
        if round_num % 2 != 0: # Odd rounds: forward order (Team A, B, C...)
            current_pick_order = list(teams)
        else: # Even rounds: reverse order (...C, B, A)
            current_pick_order = list(reversed(teams))

        for team_name in current_pick_order:
            if not available_players:
                print("No more players available to draft! Ending draft early.")
                break

            # Simulate player selection: pick a random available player
            # In a real system, this would involve user input or strategic AI.
            picked_player = random.choice(available_players)
            available_players.remove(picked_player) # Player is no longer available
            team_rosters[team_name].append(picked_player) # Assign player to team roster

            draft_log.append(f"Round {round_num}, {team_name} picks {picked_player}")
            print(f"  {team_name} picks {picked_player}")
        print()

    print("--- Draft Complete ---")
    print("\nFinal Rosters:")
    for team, roster in team_rosters.items():
        print(f"{team}: {', '.join(roster)}")

    print("\nDraft Log (Chronological):")
    for entry in draft_log:
        print(entry)

    return team_rosters

if __name__ == "__main__":
    # Example data for demonstration
    fantasy_teams = ["Team Falcons", "Team Dragons", "Team Wolves", "Team Bears"]
    all_players = [
        "Player A", "Player B", "Player C", "Player D", "Player E",
        "Player F", "Player G", "Player H", "Player I", "Player J",
        "Player K", "Player L", "Player M", "Player N", "Player O",
        "Player P", "Player Q", "Player R", "Player S", "Player T"
    ]
    num_rounds_per_team = 3 # Each team will pick 3 players

    simulate_snake_draft(fantasy_teams, all_players, num_rounds_per_team)
