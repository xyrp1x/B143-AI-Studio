import numpy as np


def to_state_index(state, kicks=5, max_diff=5):
k, diff = state
return (k * (2*max_diff + 1)) + (diff + max_diff)


def train_q_learning(episodes=5000, alpha=0.2, gamma=0.9, epsilon_start=1.0, epsilon_end=0.05, epsilon_decay=4000, seed=42):
env = PenaltyShootoutEnv(seed=seed)
max_diff = env.kicks
S = (env.kicks+1) * (2*max_diff + 1) # (kick step 0..5) × (score diff -5..+5)
Q = np.zeros((S, NUM_ACTIONS), dtype=np.float32)


returns = []
epsilons = []
total_steps = 0


for ep in range(episodes):
s = env.reset()
done = False
ep_return = 0.0
while not done:
s_idx = to_state_index(s, env.kicks, max_diff)
eps = max(epsilon_end, epsilon_start - (epsilon_start - epsilon_end) * (total_steps / epsilon_decay))
if random.random() < eps:
a = random.randrange(NUM_ACTIONS)
else:
a = int(np.argmax(Q[s_idx]))


s2, r, done, info = env.step(a)
s2_idx = to_state_index(s2, env.kicks, max_diff)


# Q-learning update
td_target = r + gamma * (0.0 if done else np.max(Q[s2_idx]))
Q[s_idx, a] += alpha * (td_target - Q[s_idx, a])


ep_return += r
s = s2
total_steps += 1


returns.append(ep_return)
epsilons.append(eps)


# Metrics
returns = np.array(returns, dtype=np.float32)
moving_avg = np.convolve(returns, np.ones(50)/50, mode='same')


# Save artifacts
np.savez(
"training_data.npz",
Q=Q,
returns=returns,
moving_avg=moving_avg,
epsilons=np.array(epsilons, dtype=np.float32),
actions=np.array(ACTIONS),
)
return Q


if __name__ == "__main__":
train_q_learning()
print("Training complete. Artifacts saved to training_data.npz")
