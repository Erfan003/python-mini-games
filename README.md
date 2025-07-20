# Python Mini Games 🎮

*Reimagining classic mini‑games in Python with fresh challenges, creative twists, and unexpected fun.*

---

## 🎯 What Is This?

**Python Mini Games** is a growing collection of small, terminal‑friendly Python games. The goal: take familiar classics, remix them with new rules or challenge modes, and keep the code clean and easy to learn from.

At the moment the collection includes **one game** — *Number Guess* — and the repo structure is ready for more. Jump in, play, and help it grow!

---

## 🎲 Available Games

### 1. Number Guess

A classic number‑guessing game: the computer picks a secret number, you try to find it within a limited number of attempts. You get feedback after each guess: **higher** or **lower**.

**Features**

- Difficulty presets: *Easy, Medium, Hard, Extreme*.
- **Custom mode** — choose your own range & attempt limit.
- Dynamic hint range updates after each guess.

**Run it**

```bash
cd games/number_guess
python number_guess.py
```

> On Windows you can also use: `py number_guess.py`

---

## 🚀 Quick Start

Clone the repo and run the game:

```bash
git clone https://github.com/<your-username>/python-mini-games.git
cd python-mini-games/games/number_guess
python number_guess.py
```

---

## 🛠 Requirements

- Python **3.8+** (standard library only — no external dependencies yet).

---

## 📂 Project Structure

```
python-mini-games/
│
├── games/
│   └── number_guess/
│       ├── number_guess.py
│       └── README.md
│
├── README.md
└── LICENSE
```

As new games are added, each gets its own folder under `games/`.

---

## ➕ Adding a New Game

Want to add *Tic Tac Toe*, *Snake*, *Hangman*, or something wild? Awesome! Use this pattern:

```
python-mini-games/
└── games/
    └── new_game_name/
        ├── new_game_name.py
        └── README.md   # short description, how to run, future ideas
```

**Guidelines**

- Use **lower\_snake\_case** for folders & main Python files.
- Keep games runnable with a simple `python game.py`.
- Include a short README in the game folder.
- Avoid heavy dependencies; if needed, update root `requirements.txt`.

---
<!--
## 🧭 Roadmap

- Have ideas? Open an Issue or start a Discussion.

---

## 🤝 Contributing

Contributions are welcome — from bug fixes to new games!

**Basic flow:**

1. Fork the repo.
2. Create a branch: `git checkout -b feature/tic-tac-toe`.
3. Add your game under `games/<game_name>/`.
4. Commit & push.
5. Open a Pull Request.

If you're new to GitHub, check the *Getting Started* note below (coming soon).

---
 -->


## 🐛 Issues & Feedback

Found a bug in game? Got a better difficulty idea? Please open an Issue — short descriptions are fine.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

### 💬 زبان‌ فارسی
در آینده روی پشتیبانی بازی‌ها از زبان دوست‌داشتنی فارسی هم کار میکنم 🤍

---


**Have fun & keep coding!** 🎉

