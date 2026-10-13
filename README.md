# CLI Tic-Tac-Toe with Rule-Based AI

A classic $3 \times 3$ Tic-Tac-Toe game written in Python that runs directly in your terminal. This project features ASCII grid rendering using `|` and `_` symbols, input validation, two-player support, and a rule-based heuristic AI opponent capable of detecting winning opportunities and blocking threats.

---

## 🎮 Features

- **Terminal Visual Board:** Rendered cleanly using `|` and horizontal dividers `---|---|---`.
- **Two Game Modes:**
  - **Player vs. Player (PvP):** Pass-and-play with a friend on the same terminal.
  - **Player vs. AI (PvE):** Play against an automated computer opponent.
- **Rule-Based Heuristic AI:**
  1. **Win Detection:** Identifies immediate winning moves and executes them.
  2. **Active Blocking:** Detects immediate human threats and blocks them.
  3. **Positional Advantage:** Prioritizes controlling the center square (`5`).
  4. **Random Selection:** Safely falls back to remaining legal moves using Python's `random` module.
- **Robust Input Handling:** Guards against invalid characters, out-of-range choices, and already occupied grid cells.

---

## 📋 Requirements

- Python 3.8+ (Compatible with Python 3.12, 3.13, and later versions).
- Standard library modules only (`random` is built-in; no external pip dependencies needed).

---

## 🚀 Installation & Running

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-python.git
   cd tic-tac-toe-python
   ```

2. **Run the Script:**
   ```bash
   python tic_tac_toe.py
   ```
   *(On Windows with Python Launcher, you can also use `py tic_tac_toe.py`)*

---

## 🕹️ How to Play

1. When prompted, select your game mode:
   - Enter `1` for Human vs. Human.
   - Enter `2` for Human vs. Smart AI.
2. The board positions correspond to numbers **1 through 9**:

   ```text
    1 | 2 | 3 
   ---|---|---
    4 | 5 | 6 
   ---|---|---
    7 | 8 | 9 
   ```

3. On your turn, type the number corresponding to your chosen cell and hit **Enter**.
4. The game automatically updates the board, detects matches across rows, columns, or diagonals, and alerts you when a player wins or if the match ends in a draw.

---

## 🧠 How the AI Works

The AI relies on a 4-tier decision priority hierarchy evaluated on every turn:

```text
+------------------------------------------------------------+
| 1. Win Check   : Can AI win this move?                     |
|                  --> Yes: Take the win.                    |
| 2. Block Check : Will player win on their next turn?       |
|                  --> Yes: Block player's spot.             |
| 3. Center Spot : Is cell 5 available?                      |
|                  --> Yes: Take index 4 (center).           |
| 4. Fallback    : Pick a random remaining cell.             |
+------------------------------------------------------------+
```

### Board Index Mapping

The board is represented internally as a 9-element list:

```python
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Indices: [0,   1,   2,   3,   4,   5,   6,   7,   8]
```

---

## 📁 Project Structure

```text
.
├── README.md          # Project documentation and guide
└── tic_tac_toe.py     # Main Python game script
```

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).