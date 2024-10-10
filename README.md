# Yahtzee Game

This is a Python implementation of the classic Yahtzee game, built using the `pygame` module. The game allows the player to roll dice and choose which ones to keep for subsequent rolls, with the goal of achieving the highest possible score.

## Installation

To run this program, you need to have Python installed on your machine, along with the `pygame` library. If you don't have `pygame` installed, you can easily install it using `pip`.

### Install Pygame

```bash
pip install pygame
```

## How to Play

1. Run the Python program.
   
2. Once the application opens, click the **ROLL** button to roll the dice.

3. Click on individual dice to set them as **hold** (these dice will not be re-rolled in subsequent turns).

4. You can re-roll the dice up to **two times** before your final result is automatically displayed at the bottom of the screen.

5. The goal is to roll combinations like **Three of a Kind**, **Full House**, or **Yahtzee** to achieve the best score.

## Game Features

- **Multiple Rolls**: You can roll the dice up to three times per turn.
- **Hold Dice**: Choose which dice to hold by clicking on them.
- **Automatic Scoring**: The game automatically calculates your score based on the dice rolled.

## Requirements

- Python 3.x
- Pygame module (`pip install pygame`)
