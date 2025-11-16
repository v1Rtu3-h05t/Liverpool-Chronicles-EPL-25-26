# -*- coding: utf-8 -*-

# 🗂️ Store Liverpool Goals by Player
Liverpool_goals = {
    "Hugo Ekitike": ["37' VS Bournemouth", "45+1' VS Newcastle"],
    "Cody Gakpo": ["49' VS Bournemouth"],
    "Federico Chiesa": ["88' VS Bournemouth"],
    "Mohamed Salah": ["90+4' VS Bournemouth"], 
    "Ryan Gravenberch": ["35' VS Newcastle"],
    "Rio Ngumoha": ["90+10' VS Newcastle"],
    "Dominik Szoboszlai": ["83' VS Arsenal"],
    "Milos Kerkez": ["45'+5' VS Brentford"]
}

# Update Below this line
Liverpool_goals["Mohamed Salah"].append("90+5' (P) VS Burnley")
Liverpool_goals["Ryan Gravenberch"].append("10' VS Everton")
Liverpool_goals["Hugo Ekitike"].append("29' VS Everton")
Liverpool_goals["Federico Chiesa"].append("86' VS Crystal Palace")
Liverpool_goals["Cody Gakpo"].append("63' VS Chelsea")
Liverpool_goals["Cody Gakpo"].append("78' VS Manchester United")
Liverpool_goals["Mohamed Salah"].append("89' VS Brentford")
Liverpool_goals["Mohamed Salah"].append("45+1' VS Aston Villa")
Liverpool_goals["Ryan Gravenberch"].append("58' VS Aston Villa")

# 📅 Store Liverpool Match Results
Liverpool_results = {
    "Bournemouth": "4-2 Win",
    "Newcastle": "3-2 Win",
    "Arsenal": "1-0 Win",
    "Burnley": "1-0 Win",
    "Everton": "2-1 Win",
    "Crystal Palace": "1-2 Loss",
    "Chelsea": "2-1 Loss",
    "Manchester United": "1-2 Loss",
    "Brentford": "3-2 Loss",
    "Aston Villa": "2-0 Win",
    "Manchester City": "3-0 Loss"
}

# 📊 Print current goal list for each player
for player, goals in Liverpool_goals.items():
    print(f"\n{player} has scored {len(goals)} goal(s):")
    for i, goal in enumerate(goals, start=1):
        print(f" {i}. {goal}")

# 🏟️ Liverpool Match Results Summary
print("\n📅 Liverpool Match Results:")
for opponent, result in Liverpool_results.items():
    print(f" - VS {opponent}: {result}")

# ⚽ Average Goals per Player
total_matches = len(Liverpool_results)
print("\n⚽ Average Goals per Player: ")
for player, goals in Liverpool_goals.items():
    avg_goals = len(goals) / total_matches
    print(f"- {player}: {avg_goals:.2f} goals per match")

# 📈 Win vs Loss Ratio
wins = sum(1 for result in Liverpool_results.values() if "Win" in result)
losses = sum(1 for result in Liverpool_results.values() if "Loss" in result)
draws = sum(1 for result in Liverpool_results.values() if "Draw" in result)

print("\n📈 Liverpool Season Summary:")
print(f" - Wins: {wins}")
print(f" - Losses: {losses}")
print(f" - Draws: {draws}")
if losses > 0:
    print(f" - Win/Loss Ratio: {wins/losses:.2f}")
else:
    print(" - Win/Loss Ratio: Perfect season (no losses!)")

# 🥅 Goals scored vs conceded
goals_scored = 0
goals_conceded = 0
for result in Liverpool_results.values():
    score = result.split()[0]   # e.g. "4-2"
    lfc, opp = score.split("-")
    goals_scored += int(lfc)
    goals_conceded += int(opp)

avg_scored = goals_scored / total_matches
avg_conceded = goals_conceded / total_matches

print(f"\n🥅 Liverpool Goals Summary:")
print(f" - Total goals scored: {goals_scored}")
print(f" - Total goals conceded: {goals_conceded}")
print(f" - Average goals scored per match: {avg_scored:.2f}")
print(f" - Average goals conceded per match: {avg_conceded:.2f}")

# 🏆 Team-wide average goals per match
total_goals = sum(len(goals) for goals in Liverpool_goals.values())
team_avg_goals = total_goals / len(Liverpool_results)

print(f"\n🏆 Liverpool scored {total_goals} total goals")
print(f" - Average goals per match: {team_avg_goals:.2f}")

# 📊 Goal contribution percentage
print("\n📊 Goal Contribution Percentage:")
for player, goals in Liverpool_goals.items():
    contribution = (len(goals) / total_goals) * 100
    print(f" - {player}: {contribution:.1f}% of team goals")

# 🆕 Update Match Results Below this line
# 🌟 Example: Add new result Liverpool_results["Aston Villa"] = "2-2 Draw" 


# 🛠️ Update Instructions

# 🌟 Example: Add a new goal after a future match
# Liverpool_goals["Cody Gakpo"].append("55' VS Aston Villa")

# 🌟 Example: Insert a revised goal (e.g., VAR correction)
# Liverpool_goals["Hugo Ekitike"].insert(1, "25' vs Bournemouth (VAR corrected)")

# 🌟 Example: Remove a disallowed goal
# disallowed = Liverpool_goals["Federico Chiesa"].pop()
# print(f"\n❌ Disallowed goal removed: {disallowed}")