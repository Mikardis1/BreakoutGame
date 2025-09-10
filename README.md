# Breakout Game

A classic Breakout-style game built with Python's Turtle graphics and Pygame for background music.

## Project Structure
```
BreakoutGame/
│
├── ball.py
├── paddle.py
├── bricks.py
├── scoreboard.py
├── player.py
├── main.py
│
├── requirements.txt        # Dependências (pygame, etc.)
├── README.md               # Descrição do projeto
├── TODO.md                 # Lista de tarefas/ideias
│
├── assets/                 # Pasta para ficheiros externos
│   ├── Theme_Song.ogg      # Música de fundo
│   └── (sprites/imagens se usares no futuro)
│
└── .gitignore              # Ignora __pycache__/ e ficheiros .pyc

```

## Features

- Paddle control using left and right arrow keys
- Multiple colored bricks with different point values
- Ball that bounces off walls, paddle, and bricks
- Scoreboard that updates based on brick hits
- Player lives and Game Over / Victory conditions
- Background music in `.ogg` format

## Installation

1. Make sure you have Python 3 installed.  
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/breakout-game.git
   pip install -r requirements.txt
   cd breakout-game
