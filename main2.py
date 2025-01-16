import pygame
import sys
import numpy as np


pygame.init()
SCREEN_X = 800
SCREEN_Y = 600
hx = SCREEN_X / 2
hY = SCREEN_Y / 2
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YALLOW = (255, 255, 0)
GRAY = (150, 150, 150)
GRAYS = pygame.Color(150, 150, 150, 50)


class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 400
    self.y = 300
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(RED)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)
    self.speed = 10

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
      self.rect.x += self.speed
    if keys[pygame.K_a]:
      self.rect.x -= self.speed

      # 工場のスプライト
class Factory1(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 200
    self.y = 240
    self.image = pygame.Surface((200, 200))
    self.image.fill(RED)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def click(self, pos):
    return self.rect.collidepoint(pos)

class Factory2(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.fac2_flag = False
    self.x = 100
    self.y = 400
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(BLUE)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def buy(self, pos):
    self.fac2_flag = True
    return self.rect.collidepoint(pos)

class Factory3(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.fac2_flag = False
    self.x = 100
    self.y = 500
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(BLUE)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def buy(self, pos):
    self.fac2_flag = True
    return self.rect.collidepoint(pos)

# ゲームスタート
def game_start():
  # スプライトのグループ作成
  sprite_group = pygame.sprite.LayeredUpdates()
  factorys = pygame.sprite.LayeredUpdates()
  fac1 = Factory1()
  fac2 = Factory2()
  fac3 = Factory3()
  sprite_group.add(fac1, fac2, fac3)
  # sprite_group.change_layer(tr, 0)
  # 関数などその他もろもろ
  coin_num = 0
  rise = 1
  clock_time = 0
  fac2_flag1 = False
  fac2_flag2 = False
  fac3_flag1 = False
  fac3_flag2 = False
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
        if fac3.buy(event.pos):
          if fac3_flag2 == False and fac3_flag1 == True:
            if coin_num >= 1000:
              fac3_flag2 = True
          elif fac3_flag1 == False:
            if coin_num >= 150:
              fac3_flag1 = True

        if fac2.buy(event.pos):
          if fac2_flag2 == False and fac2_flag1 == True:
            if coin_num >= 500:
              fac2_flag2 = True
              coin_num -= 500
          else:
            if fac2_flag1 == False:
              if coin_num >= 100:
                fac2_flag1 = True
                coin_num -= 100
            else:
              pass

        if fac1.click(event.pos):
          coin_num += rise
          if fac2_flag1 == True:
            coin_num += 1
          if fac2_flag2 == True:
            coin_num += 3
    font = pygame.font.Font(None, 36)
    text1 = font.render(F'COIN:{coin_num} $', True, (255, 255, 255))
    screen.blit(text1, (10, 10))
    font = pygame.font.Font(None, 45)
    text2 = font.render(F'LET\'S CLICK!', True, (255, 255, 255))
    screen.blit(text2, (103, 80))

    if fac2_flag2 == False and fac2_flag1 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click + 3$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 500 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag1 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click + 1$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 100 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    else:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'None', True, (255, 255, 255))
      screen.blit(text3, (65, 430))

    if fac3_flag1 == True and fac3_flag2 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 100$/s', True, (255, 255, 255))
      screen.blit(text3, (65, 530))
      text4 = font.render(F'need 1000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 545))
    elif fac3_flag1 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 10$/s', True, (255, 255, 255))
      screen.blit(text3, (65, 530))
      text4 = font.render(F'need 150 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 545))
    else:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'Level MAX', True, (255, 255, 255))
      screen.blit(text3, (65, 530))

    clock_time += clock.get_time()
    if clock_time >= 1000:
      clock_time = 0
      if fac3_flag2 == True:
        coin_num += 100
      elif fac3_flag1 == True:
        coin_num += 10
    pygame.display.flip()
    clock.tick(60)
    sprite_group.update()

game_start()

# 2035
# aaa
