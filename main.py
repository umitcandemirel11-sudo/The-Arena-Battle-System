import random

# --- DATA STRUCTURES ---
# We store character stats in a dictionary structure.
# This structure is similar to Unity's ScriptableObject concept as a data package.
player = {
    "name": "Gandalf",
    "hp": 100,
    "attack": 15,
    "defense": 5
}

enemy = {
    "name": "Saruman",
    "hp": 80,
    "attack": 12,
    "defense": 3
}

# --- BATTLE MECHANICS ---
def battle_turn(attacker, defender):
    """
    Calculates damage by subtracting defense from attack.
    Adds variability to hits with random.randint (dice roll logic).
    """
    damage = (attacker["attack"] - defender["defense"]) + random.randint(0, 5)
    
    # Permanently update the character's HP (Pass by Reference)
    defender["hp"] -= damage
    
    # Prevent HP from dropping below zero (Clamping)
    if defender["hp"] < 0:
        defender["hp"] = 0
        
    print(f"{attacker['name']} made a move! {defender['name']} took {damage} damage.")
    return defender["hp"]

# --- GAME LOOP ---
print(f"🏟️ ARENA BEGINS: {player['name']} vs {enemy['name']} 🏟️\n")

# The loop continues until one character's HP reaches 0.
while player["hp"] > 0 and enemy["hp"] > 0:
    # 1. Player's turn
    battle_turn(player, enemy)
    
    # If the enemy is still alive, it's their turn
    if enemy["hp"] > 0:
        battle_turn(enemy, player)
    
    # Print the current status after each round
    print(f"--- STATUS: {player['name']}: {player['hp']} HP | {enemy['name']}: {enemy['hp']} HP ---\n")

# --- RESULT SCREEN ---
if player["hp"] > 0:
    print(f"🏆 VICTORY! {player['name']} won the battle!")
else:
    print(f"💀 DEFEAT! {enemy['name']} emerged victorious...")