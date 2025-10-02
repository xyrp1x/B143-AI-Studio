# B143-AI-Studio
# Super Insane Penalty Shootout with Reinforcement Learning


**Developed By:** Tymur Lukianov, GH1026500


This project implements a **Q-learning** agent that learns to take penalty kicks against a stochastic goalkeeper. 5 ways to score, only one will win.  This repository includes the game environment, RL training script, playback script, and a simple analysis notebook.

## Setup 


```bash
git clone "https://github.com/<your-username>/penalty-shootout-rl.git"


### 2 Navigate into the Project Directory

```bash
cd Reinforcement-learning-on-Game
```

### 3  Virtual Environment


```bash
python -m venv project_env
.\project_env\Scripts\Activate.ps1
```

## 4. Install Dependencies

Install packages:

```bash
pip install -r requirements.txt
```

##  File content

### `penalty_game.py`

- **Run With:**

```bash
python penalty_game.py
```

---

## `penalty_shootout_ql.py`

 Train the Q-learning RL agent over a series of episodes 
- **Output:** Saves the learned Q-table to `training_data.npz`.

- **Training Mode Toggle:**  
  You can toggle visual training by editing `VISUAL_TRAINING` inside this script:

  - `True`: Watch the agent train 
  - `False`: Headless mode 
- **Run With:**

```bash
python zombie_shooter_ql.py
```

---

### `play_with_agent.py`

- **Purpose:** Loads the trained Q-table and runs the game using the agent's learned policy.
- **Run After Training:**

```bash
python play_with_agent.py
```

---

## `RL_Project_Analysis.ipynb`

- **Purpose:** A Jupyter Notebook for analyzing the agent’s learned strategy using heatmaps, charts, and statistics.
- **Run With:**

```bash
jupyter notebook RL_Project_Analysis.ipynb
```

### `read_npz.py`

- **Purpose:** A python script to view the q_values
- **Run With:**

```bash
python read_npz.py
```

---

## how to play

1. **Train the Agent**

   Run the training script to let the agent learn from scratch:


   ```bash
python penalty_shootout_ql.py
   ```

2. **Watch the AI Play**

   After training, run this to observe the learned behavior:

   ```bash
   python play_with_agent.py
   ```

3. ** we also can play**

  python penalty_game.py

  
3. ** look through the project**

   Use the Jupyter Notebook to visualize  how the agent makes decisions:

   ```bash
   jupyter notebook RL_Project_Analysis.ipynb
   ```

---

## conclusion 

After this project i have done a well trained q learned agend that is able to decide how to score with the most efficent way choosing between 5 options, i also made it possible to try it yourself.
