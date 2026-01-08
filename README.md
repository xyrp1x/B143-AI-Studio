Reinforcement Learning for a Penalty Shootout Game
Project Overview

This project demonstrates the application of Reinforcement Learning (RL) techniques to a custom-designed Penalty Shootout game using Python.
The objective is to train an agent that learns how to score goals against a goalkeeper by selecting optimal shot directions over multiple episodes.

Two classical RL algorithms are implemented and compared:

Q-learning (off-policy)

SARSA (on-policy)

The project includes environment design, algorithm implementation, experimentation, evaluation, and analysis.

Game Description

Each episode consists of 5 penalty kicks

At each step, the agent chooses one of 5 shot directions

The goalkeeper dives according to a probabilistic strategy

Reward = +1 for a goal, 0 for a save

Goal: maximise total goals per episode

Reinforcement Learning Formulation

State:
(current kick index, last goalkeeper dive direction)

Actions:
Five discrete shot directions

Reward:
+1 for a goal, 0 otherwise

Policy:
ε-greedy with exponential decay

Algorithms Implemented
Q-learning

An off-policy algorithm that updates Q-values using the maximum expected future reward.

SARSA

An on-policy algorithm that updates Q-values based on the action actually taken.

Both algorithms use tabular Q-learning and are trained over multiple episodes.

Experimental Setup

Training episodes: 8,000

Evaluation episodes: 2,000

Multiple random seeds for robustness

Metrics:

Average goals per episode

Success rate (≥3 goals)

Perfect episode rate (5 goals)

A random agent is used as a baseline.


Results

Both RL agents outperform the random baseline

SARSA achieves the most stable and highest overall performance

Learning curves demonstrate clear convergence over time

Generated outputs:

learning_curves_step2.png

results_step2.csv




## how to run ##
1. Install dependencies
pip install -r requirements.txt

2. Train the agent
python penalty_shootout_ql.py

3. Play using the trained agent
python play_with_agent.py

Project Structure
B143-AI-Studio/
│── penalty_game.py
│── penalty_shootout_ql.py
│── play_with_agent.py
│── rl_algorithms.py
│── penalty_env_headless.py
│── results_step2.csv
│── learning_curves_step2.png
│── README.md
│── requirements.txt
