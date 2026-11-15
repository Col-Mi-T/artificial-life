import sys
sys.dont_write_bytecode = True


def options():
    import questionary
    choice = questionary.select(
        "What would you like to do?",
        choices=[
            "Brian's Brain",
            "Conway's Game Of Life",
            "Seeds",
            "Exit"
        ]
    ).ask()
    if choice.lower() == "exit":
        sys.exit(0)
    elif choice.lower() == "brian's brain":
        from brians_brain import b_b
        b_b.brain()
        
    elif choice.lower() == "conway's game of life":
        from conway_gol import con_game
        con_game.conway()
        
    elif choice.lower() == "seeds":
        from silverman_seeds import seeds_ca
        seeds_ca.seeds()
        
    elif choice.lower()=="exit":
        sys.exit(0)

while True:
    options()
    
    