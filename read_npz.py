import numpy as np
import matplotlib.pyplot as plt


data = np.load("training_data.npz")
returns = data["returns"]
ma = data["moving_avg"]
eps = data["epsilons"]


plt.figure()
plt.plot(returns, label="Episode goals")
plt.plot(ma, label="Moving avg (50)")
plt.xlabel("Episode")
plt.ylabel("Goals per episode")
plt.legend()
plt.title("Penalty Shootout – Learning Curve")
plt.tight_layout()
plt.savefig("learning_curve.png", dpi=150)
print("Saved learning_curve.png")
