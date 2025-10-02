import pygame
import sys
import numpy as np


# -------- Game constants --------
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
GOAL_COLOR = (200, 200, 200)
BALL_COLOR = (245, 245, 245)
ARROW_COLOR = (30, 144, 255)


ACTIONS = ["L", "LC", "C", "RC", "R"] # five shot directions
ACT_TO_IDX = {a: i for i, a in enumerate(ACTIONS)}


class PenaltyEnvVisual:
"""
Lightweight visual wrapper for the headless training environment in penalty_shootout_ql.py.
This lets a human play with the keyboard OR watch a trained agent act.
"""
def __init__(self):
pygame.init()
self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penalty Shootout")
self.clock = pygame.time.Clock()
self.font = pygame.font.SysFont(None, 28)
# Geometry
self.goal_rect = pygame.Rect(70, 80, WIDTH-140, 60)
self.spot = (WIDTH//2, HEIGHT-120)
self.arrow_targets = self._compute_targets()


# Score state for display-only
self.reset_display_state()


def _compute_targets(self):
gx, gy, gw, gh = self.goal_rect
y = gy + gh + 10
xs = np.linspace(gx+15, gx+gw-15, 5)
return [(int(x), int(y)) for x in xs]


def reset_display_state(self):
self.kick_idx = 0
self.score = 0
self.history = [] # list of (action_idx, keeper_idx, goal_bool)


def draw_pitch(self):
self.screen.fill(GREEN)
pygame.draw.rect(self.screen, GOAL_COLOR, self.goal_rect, border_radius=6)
# Goal posts
pygame.draw.rect(self.screen, WHITE, self.goal_rect, 3, border_radius=6)
# Penalty spot
pygame.draw.circle(self.screen, WHITE, self.spot, 5)


def draw_ui(self, highlight_idx=None):
# Arrows an targets
for i, (tx, ty) in enumerate(self.arrow_targets):
length = 70
end = (tx, ty - length)
color = ARROW_COLOR if i != highlight_idx else (255, 165, 0)
pygame.draw.line(self.screen, color, (tx, ty), end, 6)


# Scoreboard
text = self.font.render(f"Kick {self.kick_idx+1}/5 Score: {self.score}", True, WHITE)
self.screen.blit(text, (20, HEIGHT-40))


def animate_shot(self, action_idx, keeper_idx, goal):
# Simple animation: ball moves toward chosen target; keeper dives to target
ball_x, ball_y = self.spot
target_x, target_y = self.arrow_targets[action_idx]
vis.run_human(step_cb)
