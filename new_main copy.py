import pygame
import sys
import numpy as np


pygame.init()
SCREEN_X = 800
SCREEN_Y = 600
hx = SCREEN_X / 2
hY = SCREEN_Y / 2
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YALLOW = (255, 255, 0)
GRAY = (150, 150, 150)
GRAYS = pygame.Color(150, 150, 150, 50)
RED = (255, 0, 0)

# 工場のスプライト
class Factory1(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(GRAYS)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

  def click(self, pos):
    return self.rect.collidepoint(pos)

class Factory2(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 400
    self.y = 400
    self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
    self.image.fill(GRAYS)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

# ゲームスタート
def game_start():
  # スプライトのグループ作成
  sprite_group = pygame.sprite.LayeredUpdates()
  # sprite_group.change_layer(tr, 0)

  start_X = 0
  start_Y = 100
  start_count = [[100, 200, 300, 400, 500, 600, 700],
                 [100, 200, 300, 400, 500, 600, 700],
                 [100, 200, 300, 400, 500, 600, 700],
                 [100, 200, 300, 400, 500, 600, 700]]
  for i, ii in enumerate(start_count):
    start_Y = 100 * (i + 1)
    for j, start_X in enumerate(ii):
      # start_X += 100
      fac1 = Factory1(start_X, start_Y)
      sprite_group.add(fac1)

      # メインループ
  running = True
  money = 100
  while running:
    screen.fill((BLACK))
    sprite_group.draw(screen)
    # pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 100))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if fac1.click(event.pos):
          fac2 = Factory2()
          sprite_group.add(fac2)
    font = pygame.font.Font(None, 36)
    text = font.render("Hello, Python!", False, (255, 255, 255))  # 白色
    screen.blit(text, (50, 50))
    pygame.display.flip()
    sprite_group.update()

game_start()

# 2035
