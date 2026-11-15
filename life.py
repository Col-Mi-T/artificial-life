import sys
sys.dont_write_bytecode = True
from conway_gol import con_game
from silverman_seeds import seeds_ca
from brians_brain import b_b

args = sys.argv[1:]

if len(args) < 1:
    print("\nChoose a Simulation\n\nAvailable Flags:\n\t- '-b' or '--brain' for Brian's Brain\n\t- '-c' or '--conway' for Conway's Game Of Life\n\t- '-s' or '--seeds' for Seeds")
    sys.exit(1)


if args[0] == "-c" or args[0] == "--conway":
    con_game.conway()
elif args[0] == "-s" or args[0] == "--seeds":
    seeds_ca.seeds()
elif args[0] == "-b" or args[0] == "--brain":
    b_b.brain()
else:
    print("\nUnknown Simulation!\n\nAvailable Flags:\n\t- '-b' or '--brain' for Brian's Brain\n\t- '-c' or '--conway' for Conway's Game Of Life\n\t- '-s' or '--seeds' for Seeds")
    sys.exit(1)