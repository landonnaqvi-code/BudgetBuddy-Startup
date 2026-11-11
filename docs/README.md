# BudgetBuddy

A small spending/allowance tracker you run in the terminal. Start with
taking a survey that stores data regarding your financial situation.
Then, you can add transactions and remove them as you manage money.
At any moment you can access the old data regarding your financial
situation and find data regarding your transactions such the
average spent per transaction or which ones are the most expensive.
At any moment, enter "0" and you are done with the program.

## Run it

```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

## How it's laid out

| File | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The transactions, the balance, and small helpers |
| `features/reports.py` | Summary reports (half-built - finish it via a ticket) |
| `data/budgetbuddy.json` | The transaction history and starting balance |
| `tests/test_core.py` | Example tests to copy from |

## Team

- Landon (Building BudgetBuddy)<!-- Add yourself here on your Git lesson: - Your Name (role) -->

- (your squad will add themselves here)

## Where to start

Pick a ticket from the `tickets/` folder (or the Issues tab once your section
repo exists). Read `CONTRIBUTING.md` for the Definition of Done every pull
request has to meet.
