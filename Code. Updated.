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

# 📅 Store Liverpool Match Results
Liverpool_results = {
    "Bournemouth": "4-2 Win",
    "Newcastle": "3-2 Win",
    "Arsenal": "1-0 Win",
    "Burnley": "1-0 Win",
    "Everton": "2-1 Win",
    "Crystal Palace": "1-2 Loss"
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
