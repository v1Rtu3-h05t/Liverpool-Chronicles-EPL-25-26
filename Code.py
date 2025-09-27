# 🗂️ Store Liverpool Goals by Player
Liverpool_goals = {
    "Hugo Ekitike": ["37' VS Bournemouth", "45+1' VS Newcastle"],
    "Cody Gakpo": ["49' VS Bournemouth"],
    "Federico Chiesa": ["88' VS Bournemouth"],
    "Mohamed Salah": ["90+4' VS Bournemouth"],  # ✅ Fixed: was missing comma and used tuple
    "Ryan Gravenberch": ["35' VS Newcastle"],
    "Rio Ngumoha": ["90+10' VS Newcastle"],
    "Dominik Szoboszlai": ["83' VS Arsenal"]
}

# Update Below this line
Liverpool_goals["Mohamed Salah"].append("90+5' (P) VS Burnley")
Liverpool_goals["Ryan Gravenberch"].append("10' VS Everton")
Liverpool_goals["Hugo Ekitike"].append("29' VS Everton")
Liverpool_goals["Federico Chiesa"].append("86' VS Crystal Palace")

# 📊 Print current goal list for each player
for player, goals in Liverpool_goals.items():
    print(f"\n{player} has scored {len(goals)} goal(s):")
    for i, goal in enumerate(goals, start=1):
        print(f" {i}. {goal}")

# 🛠️ Update Instructions

# 🌟 Example: Add a new goal after a future match
# Liverpool_goals["Cody Gakpo"].append("55' VS Aston Villa")

# 🌟 Example: Insert a revised goal (e.g., VAR correction)
# Liverpool_goals["Hugo Ekitike"].insert(1, "25' vs Bournemouth (VAR corrected)")

# 🌟 Example: Remove a disallowed goal
# disallowed = Liverpool_goals["Federico Chiesa"].pop()
# print(f"\n❌ Disallowed goal removed: {disallowed}")
