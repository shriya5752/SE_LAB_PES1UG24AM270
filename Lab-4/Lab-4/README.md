# Lab 4 — VibeCoding

## Code & Commits

The updated `game.py`, with separate commits for each task, is in my Galaga fork:

https://github.com/shriya5752/31_galaga

Commit history:
- Fix bezier exponent bug - Task 1
- Add enemy_tint wave recoloring - Task 2
- Add wave-start banner - Task 3
- Add shield charges every 3 waves - Task 4

## Deliverables in this folder

- `Galaga Before.MP4` — 10s gameplay before changes (shows the buggy Bezier entry/dive paths)
- `Galaga After.mp4` — 10s gameplay after changes (shows fixed paths, recolored enemies, wave banner, and shield)
- `Galaga game Gemini Chat.pdf` — full LLM chat history used for this lab
- `game.py` — copy of the updated code

## Tasks Completed

| Task | What was done |
|------|----------------|
| 1 | Fixed the cubic Bezier exponents in the `bezier()` function so entry/dive paths bulge correctly |
| 2 | Implemented `enemy_tint(kind)` to recolor enemies by wave number |
| 3 | Implemented `on_wave_start(wave)` to display a "WAVE N" banner |
| 4 | Implemented `shield_charges(wave)` to grant 1 shield charge every 3rd wave |
