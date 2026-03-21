# CLI RPG dice roll
A command-line program to roll Table-Top RPG's Dices

A simple command-line tool written in Python to roll RPG dice (D&D-style). This tool allows you to roll dice directly from the Linux terminal using classic notation like:

roll 2d6+3
roll 1d20
roll 2d10z+5

---

## Features

- Roll multiple dice at once (e.g., 3d6)
- Add bonuses (e.g., 2d10+5)
- Support for zero-based dice (e.g., d10 from 0–9 using z)

## Installation

### Clone the repository
```bash
git clone https://github.com/PGFerraz/CLI-RPG-dice-roll.git
cd CLI-RPG-dice-roll
```

### Make the script executable
```bash
chmod +x roll
```

### Move it to a global path
```bash
sudo mv roll /usr/local/bin/
```
## Usage
Basic syntax
```bash
roll XdY+Z
```
### Where:

- X → number of dice
- Y → number of sides
- Z → bonus (optional)

# Examples
### Roll 3 six-sided dice
```bash
roll 3d6
```
### Roll 1 twenty-sided die
```bash
roll 1d20
```
### Roll with bonus
```bash
roll 2d10+5
```
### Zero-based dice (0–9)
```bash
roll 2d10z+5
```

##Requirements
- Python 3.x
- Linux (tested on Fedora)
