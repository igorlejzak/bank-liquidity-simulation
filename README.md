# Bank Liquidity Simulation

A Python project I built to learn more about how banks manage liquidity risk.

The program simulates how a bank's liquidity buffer changes over 1000 days
using Monte Carlo methods. Each day is modelled as either normal (95% chance)
or stressed (5% chance), where stressed days represent sudden spikes in
withdrawals. Running 1000 independent scenarios shows the full range of
possible outcomes — from banks that accumulate liquidity to those that
eventually fall below the minimum buffer threshold.

## What it does
- Loads deposit data from a CSV file
- Runs 1000 Monte Carlo simulations of daily cash flows
- Models stressed days with higher withdrawal rates
- Highlights the best and worst performing paths on a chart
- Shows the minimum required buffer (20% of total deposits)

## How to run
```bash
pip install -r requirements.txt
python main.py
```

## Tech
Python, NumPy, Pandas, Matplotlib