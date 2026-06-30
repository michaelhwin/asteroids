# 🚀 Asteroids

A recreation of the classic 1979 Atari arcade game, built with Python and Pygame.

## Gameplay

Pilot your ship through an asteroid field and shoot everything that moves. Colliding with any asteroid ends the game. Shots that hit an asteroid cause it to split — keep firing until the fragments are gone.

## Controls

| Action | Key |
|---|---|
| Rotate Left | `A` |
| Rotate Right | `D` |
| Thrust | `W` |
| Fire | `Space` |

## Getting Started

### Prerequisites

- Python 3.8+
- [Pygame](https://www.pygame.org/)

### Installation

```bash
git clone https://github.com/yourname/asteroids.git
cd asteroids
pip install pygame
```

### Running

```bash
python main.py
```

## Project Structure

```
asteroids/
├── main.py            # Entry point, game loop, and collision handling
├── player.py          # Player ship movement and shooting
├── asteroid.py        # Asteroid behaviour and splitting logic
├── asteroidfield.py   # Spawns and manages the asteroid field
├── shot.py            # Projectile logic
├── constants.py       # Screen size and other tunable values
└── logger.py          # State and event logging (log_state, log_event)
```

## Game Loop

Each frame the loop:

1. Processes Pygame events (quit, input)
2. Updates all sprites (`updatable` group) by delta time
3. Checks player–asteroid collisions → game over on hit
4. Checks shot–asteroid collisions → splits asteroid, removes shot
5. Draws all sprites (`drawable` group)
6. Logs the current game state via `log_state()`
7. Flips the display and ticks at 60 FPS

## License

MIT — see [LICENSE](LICENSE) for details.
