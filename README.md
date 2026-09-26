## Work in progress...

A small care game about my childhood stuffed bunny, Latta.
I built this to practice **object-oriented programming** in Python.
`bunny.py` is the character. `game.py` is the window, buttons, and clock.

## What you can do
- Feed her (carrots, lettuce, hay, apple, orange — cake makes her sad)
- Brush her fur
- Make her laugh
- Give her a shower
- Hear a childhood memory
- Watch her hunger rise over 5 minutes: she will tell you when she is hungry

She waves when the game starts, and again when she is happy (happiness above 50).
If happiness drops to 30 or below, she looks sad.
## OOP ideas used
- **Class / object** — `Bunny` is the blueprint, `latta` is the real bunny
- **Attributes** — hunger, happiness, cleanliness, hair
- **Methods** — `feed()`, `brush()`, `make_laugh()`, `shower()`, `tell_memory()`
- **Composition** — Latta *has a* `MemoryBook`

## How to run
```bash
cd Latta
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
