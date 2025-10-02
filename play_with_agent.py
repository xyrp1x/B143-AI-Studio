import numpy as np
from penalty_shootout_ql import PenaltyShootoutEnv, to_state_index, ACTIONS
from penalty_game import PenaltyEnvVisual


# Load Q table
DATA = np.load("training_data.npz")
Q = DATA["Q"]


env = PenaltyShootoutEnv()
max_diff = env.kicks


def policy(state):
idx = to_state_index(state, env.kicks, max_diff)
return int(np.argmax(Q[idx]))


if __name__ == "__main__":
vis = PenaltyEnvVisual()
vis.run_agent(policy)
