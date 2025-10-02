import pygame
for ln in lines[1:]:
txt = small.render(ln, True, WHITE)
self.screen.blit(txt, (80, y)); y += 28
y += 10
for ln in controls:
txt = small.render(ln, True, (255, 215, 0))
self.screen.blit(txt, (80, y)); y += 28
foot = small.render(footer, True, (173, 216, 230))
self.screen.blit(foot, (WIDTH//2 - foot.get_width()//2, HEIGHT-90))


pygame.display.flip()
self.clock.tick(60)
return True


def run_human(self, step_callback):
"""
step_callback(action_idx) -> (keeper_idx, goal_bool)
The callback comes from the logic env (see training script). This function only draws.
"""
self.reset_display_state()
if not self.show_rules(mode="human"):
return
running = True
while running:
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False
if event.type == pygame.KEYDOWN:
if event.key in (pygame.K_a, pygame.K_LEFT): action = 0
elif event.key in (pygame.K_s, pygame.K_1): action = 1
elif event.key in (pygame.K_d, pygame.K_DOWN): action = 2
elif event.key in (pygame.K_f, pygame.K_2): action = 3
elif event.key in (pygame.K_g, pygame.K_RIGHT): action = 4
else: action = None
if action is not None and self.kick_idx < 5:
keeper_idx, goal = step_callback(action)
self.animate_shot(action, keeper_idx, goal)
self.kick_idx += 1
self.score += int(goal)
if self.kick_idx >= 5:
running = False


self.draw_pitch()
self.draw_ui()
pygame.display.flip()
self.clock.tick(60)
pygame.quit()


def run_agent(self, policy_fn):
"""policy_fn(state_tuple)-> action_idx (0..4)"""
self.reset_display_state()
if not self.show_rules(mode="agent"):
return
from penalty_shootout_ql import PenaltyShootoutEnv # import headless env
env = PenaltyShootoutEnv()
s = env.reset()
done = False
while not done:
a = policy_fn(s)
s2, r, done, info = env.step(a)
self.animate_shot(a, info["keeper_idx"], info["goal"]) # draw outcome
self.kick_idx += 1
self.score += int(info["goal"])
s = s2
pygame.quit()


if __name__ == "__main__":
# Quick  demo with a random keeper and user-controlled shooter
from penalty_shootout_ql import PenaltyShootoutEnv
env_logic = PenaltyShootoutEnv()


def step_cb(action_idx):
_, _, _, info = env_logic._step_no_state_update(action_idx)
env_logic.apply_step_update(info) # advance environment state
return info["keeper_idx"], info["goal"]


vis = PenaltyEnvVisual()
vis.run_human(step_cb)
