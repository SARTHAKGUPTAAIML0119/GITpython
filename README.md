# Binomial Distribution: Coin Flip Simulator 🪙

A Python-based simulation tool to visualize the probability of "successes" in a series of independent trials (coin flips) using the Binomial Distribution.

## How it Works
This program allows users to:
1. Define the number of **Tries** ($n$) per experiment.
2. Define the number of **Experiments** (size) to run.
3. Automatically calculate outcomes based on a fair probability ($p=0.5$).
4. Visualize the results using a **Seaborn Distribution Plot** with a KDE (Kernel Density Estimate) curve.

## Installation
This project uses `uv` for package management. To get started:

```bash
# Install dependencies
uv sync

# Run the program
uv run coinflipprobablity.py
