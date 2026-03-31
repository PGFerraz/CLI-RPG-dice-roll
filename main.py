#!/usr/bin/env python3

import random, sys, re, json, time

# Colors
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[0m'

def lines():
    print(MAGENTA + '-'*25 + RESET)

def parse_roll(roll_str):

    pattern = r'(\d+)d(\d+)(z?)([+-]\d+)?'
    match = re.fullmatch(pattern, roll_str)

    if not match:
        print("Wrong Format! Use this way: 2d6+3")
        sys.exit(1)

    num_dice = int(match.group(1))
    num_sides = int(match.group(2))
    zero_based = match.group(3) == 'z'
    bonus = int(match.group(4)) if match.group(4) else 0

    return num_dice, num_sides, bonus, zero_based

def roll_dice(num_dice, num_sides, bonus=0, zero_based=False):
    total = 0

    lines()
    for i in range(num_dice):
        if zero_based:
            roll = random.randint(0, num_sides - 1)
        else:
            roll = random.randint(1, num_sides)

        print(BLUE + f'Dice {i+1}:' + RESET, roll)
        total += roll

    lines()

    if bonus != 0:
        print(YELLOW + 'Bonus:' + RESET, bonus)
        total += bonus
        lines()

    print(GREEN + 'Total:' + RESET, total)
    lines()
    
    rlist = []
    rlist.append({
            'time': time.ctime(),
            'total': total
        })
    
    with open('log.json', 'ar') as f:
        json.dump(rlist, f, indent=4)

if sys.argv[1] == 'log':
    with open('log.json', 'a') as f:
        data = json.load(f)
        print(json.dumps(data, indent=4))
    sys.exit(1)

if len(sys.argv) < 2:
    print("Use: roll 2d6+3")
    sys.exit(1)

roll_input = sys.argv[1]

num_dice, num_sides, bonus, zero_based = parse_roll(roll_input)
roll_dice(num_dice, num_sides, bonus, zero_based)
