import pygame
import sys
import numpy as np
import random as r


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
DOU = (134, 74, 43)
GIN = (192, 192, 192)
KIN = (255, 215, 0)


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
    self.x = 100
    self.y = 400
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(BLUE)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def buy(self, pos):
    return self.rect.collidepoint(pos)

class Factory3(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 100
    self.y = 500
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(BLUE)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def buy(self, pos):
    return self.rect.collidepoint(pos)

class Factory4(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 220
    self.y = 400
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(BLUE)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def buy(self, pos):
    return self.rect.collidepoint(pos)

class Factory5(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 220
    self.y = 500
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(BLUE)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def buy(self, pos):
    return self.rect.collidepoint(pos)

class Gatya(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 420
    self.y = 50
    self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image.fill(BLUE)
    self.rect = self.image.get_rect()
    self.rect.center = (self.x, self.y)

  def gatya(self, pos):
    return self.rect.collidepoint(pos)

# ゲームスタート
def game_start():
  # スプライトのグループ作成
  sprite_group = pygame.sprite.LayeredUpdates()
  factorys = pygame.sprite.LayeredUpdates()
  fac1 = Factory1()
  fac2 = Factory2()
  fac3 = Factory3()
  fac4 = Factory4()
  fac5 = Factory5()
  gt = Gatya()
  sprite_group.add(fac1, fac2, fac3, fac4, fac5, gt)
  # sprite_group.change_layer(tr, 0)
  # 関数などその他もろもろ
  coin_num = 0
  rise = 1
  clock_time = 0
  click_num = 0
  afk_time = 0
  fac2_flag1 = False
  fac2_flag2 = False
  fac2_flag3 = False
  fac2_flag4 = False
  fac2_flag5 = False
  fac2_flag6 = False
  fac2_flag7 = False
  fac2_flag8 = False
  fac2_flag9 = False
  fac2_flag10 = False
  fac3_flag1 = False
  fac3_flag2 = False
  fac3_flag3 = False
  fac3_flag4 = False
  fac4_flag1 = False
  fac4_flag2 = False
  fac4_flag3 = False
  fac4_flag4 = False
  fac5_flag1 = False
  fac5_flag2 = False
  fac5_flag3 = False
  fac5_flag4 = False

  gt_flag1 = False
  gt_flag2 = False
  gt_flag3 = False
  gt_flag4 = False
  gt_flag5 = False
  gt_flag6 = False

  res1 = False
  res2 = False
  res3 = False
  res4 = False
  item1 = False
  item2 = False
  item3 = False
  item4 = False
  item5 = False
  item6 = False
  item7 = False
  item8 = False
  item9 = False
  item10 = False
  item11 = False
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
        # 5オートrise
        if gt.gatya(event.pos):
          if coin_num >= 10000:
            coin_num -= 10000
            rank = [1, 2, 3, 4, 5, 6]
            p = [5, 5, 15, 15, 60, 60]
            c = r.choices(rank, weights=p, k=1)
            if c[0] == 1:
              gt_flag1 = True
            elif c[0] == 2:
              gt_flag2 = True
            elif c[0] == 3:
              gt_flag3 = True
            elif c[0] == 4:
              gt_flag4 = True
            elif c[0] == 5:
              gt_flag5 = True
            elif c[0] == 6:
              gt_flag6 = True

        # 5オートrise
        if fac5.buy(event.pos):
          if fac5_flag4 == False and fac5_flag3 == True:
            if coin_num >= 25000:
              fac5_flag4 = True
              coin_num -= 25000
          elif fac5_flag3 == False and fac5_flag2 == True:
            if coin_num >= 20000:
              fac5_flag3 = True
              coin_num -= 20000
          elif fac5_flag2 == False and fac5_flag1 == True:
            if coin_num >= 14000:
              fac5_flag2 = True
              coin_num -= 14000
          elif fac5_flag1 == False:
            if coin_num >= 5500:
              fac5_flag1 = True
              coin_num -= 5500

        # 4オートrise
        if fac4.buy(event.pos):
          if fac4_flag4 == False and fac4_flag3 == True:
            if coin_num >= 16000:
              fac4_flag4 = True
              coin_num -= 16000
          elif fac4_flag3 == False and fac4_flag2 == True:
            if coin_num >= 10000:
              fac4_flag3 = True
              coin_num -= 10000
          elif fac4_flag2 == False and fac4_flag1 == True:
            if coin_num >= 5000:
              fac4_flag2 = True
              coin_num -= 5000
          elif fac4_flag1 == False:
            if coin_num >= 1000:
              fac4_flag1 = True
              coin_num -= 1000

        # 3オートrise
        if fac3.buy(event.pos):
          if fac3_flag4 == False and fac3_flag3 == True:
            if coin_num >= 6000:
              fac3_flag4 = True
              coin_num -= 6000
          elif fac3_flag3 == False and fac3_flag2 == True:
            if coin_num >= 1500:
              fac3_flag3 = True
              coin_num -= 1500
          elif fac3_flag2 == False and fac3_flag1 == True:
            if coin_num >= 800:
              fac3_flag2 = True
              coin_num -= 800
          elif fac3_flag1 == False:
            if coin_num >= 150:
              fac3_flag1 = True
              coin_num -= 150
        # 2クリックrise
        if fac2.buy(event.pos):
          if fac2_flag10 == False and fac2_flag9 == True:
            if coin_num >= 200000:
              fac2_flag10 = True
              res4 = True
              coin_num -= 200000
          elif fac2_flag9 == False and fac2_flag8 == True:
            if coin_num >= 150000:
              fac2_flag9 = True
              coin_num -= 150000
          elif fac2_flag8 == False and fac2_flag7 == True:
            if coin_num >= 100000:
              fac2_flag8 = True
              coin_num -= 100000
          elif fac2_flag7 == False and fac2_flag6 == True:
            if coin_num >= 55000:
              fac2_flag7 = True
              coin_num -= 55000
          elif fac2_flag6 == False and fac2_flag5 == True:
            if coin_num >= 40000:
              fac2_flag6 = True
              coin_num -= 40000
          elif fac2_flag5 == False and fac2_flag4 == True:
            if coin_num >= 20000:
              fac2_flag5 = True
              coin_num -= 20000
          elif fac2_flag4 == False and fac2_flag3 == True:
            if coin_num >= 10000:
              fac2_flag4 = True
              coin_num -= 10000
          elif fac2_flag3 == False and fac2_flag2 == True:
            if coin_num >= 3000:
              fac2_flag3 = True
              coin_num -= 3000
          elif fac2_flag2 == False and fac2_flag1 == True:
            if coin_num >= 500:
              fac2_flag2 = True
              coin_num -= 500
          elif fac2_flag1 == False:
            if coin_num >= 100:
              fac2_flag1 = True
              coin_num -= 100
          else:
            pass
        # メインクリック
        if fac1.click(event.pos):
          click_num += 1
          afk_time = 0
          if fac2_flag10 == True:
            coin_num += 3000
          elif fac2_flag9 == True:
            coin_num += 2500
          elif fac2_flag8 == True:
            coin_num += 2000
          elif fac2_flag7 == True:
            coin_num += 1500
          elif fac2_flag6 == True:
            coin_num += 1000
          elif fac2_flag5 == True:
            coin_num += 800
          elif fac2_flag4 == True:
            coin_num += 500
          elif fac2_flag3 == True:
            coin_num += 100
          elif fac2_flag2 == True:
            coin_num += 50
          elif fac2_flag1 == True:
            coin_num += 10
          else:
            coin_num += rise
          if item3 == True:
            coin_num += 1000
          if item4 == True:
            coin_num += 100
          if item2 == True:
            coin_num += 10
          if item7 == True:
            coin_num += 1000
          if item8 == True:
            coin_num += 3000

    font = pygame.font.Font(None, 36)
    text1 = font.render(F'COIN:{coin_num} $', True, (255, 255, 255))
    screen.blit(text1, (10, 10))
    font = pygame.font.Font(None, 45)
    text2 = font.render(F'LET\'S CLICK!', True, (255, 255, 255))
    screen.blit(text2, (103, 80))
    font = pygame.font.Font(None, 30)
    text2 = font.render(F'Item Gatya! left Click! ', True, (255, 255, 255))
    screen.blit(text2, (450, 30))
    font = pygame.font.Font(None, 25)
    text2 = font.render(F'need 10000$ ', True, (255, 255, 255))
    screen.blit(text2, (450, 55))

    # ２クリック
    if fac2_flag10 == False and fac2_flag9 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 3000$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 200000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag9 == False and fac2_flag8 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 2500$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 150000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag8 == False and fac2_flag7 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 2000$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 100000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag7 == False and fac2_flag6 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 1500$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 55000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag6 == False and fac2_flag5 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 1000$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 40000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag5 == False and fac2_flag4 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 800$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 20000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag4 == False and fac2_flag3 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 500$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 10000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag3 == False and fac2_flag2 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 100$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 3000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag2 == False and fac2_flag1 == True:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 50$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 500 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    elif fac2_flag1 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'click = 10$', True, (255, 255, 255))
      screen.blit(text3, (65, 430))
      text4 = font.render(F'need 100 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 445))
    else:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'Level MAX', True, (255, 255, 255))
      screen.blit(text3, (65, 430))

      # ３オート
    if fac3_flag3 == True and fac3_flag4 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 250$/s', True, (255, 255, 255))
      screen.blit(text3, (65, 530))
      text4 = font.render(F'need 6000 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 545))
    elif fac3_flag2 == True and fac3_flag3 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 100$/s', True, (255, 255, 255))
      screen.blit(text3, (65, 530))
      text4 = font.render(F'need 1500 $ ', True, (255, 255, 255))
      screen.blit(text4, (65, 545))
    elif fac3_flag1 == True and fac3_flag2 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 50$/s', True, (255, 255, 255))
      screen.blit(text3, (65, 530))
      text4 = font.render(F'need 800 $ ', True, (255, 255, 255))
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

      # ４オート
    if fac4_flag3 == True and fac4_flag4 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 500$/s', True, (255, 255, 255))
      screen.blit(text3, (185, 430))
      text4 = font.render(F'need 16000 $ ', True, (255, 255, 255))
      screen.blit(text4, (185, 445))
    elif fac4_flag2 == True and fac4_flag3 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 350$/s', True, (255, 255, 255))
      screen.blit(text3, (185, 430))
      text4 = font.render(F'need 10000 $ ', True, (255, 255, 255))
      screen.blit(text4, (185, 445))
    elif fac4_flag1 == True and fac4_flag2 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 200$/s', True, (255, 255, 255))
      screen.blit(text3, (185, 430))
      text4 = font.render(F'need 5000 $ ', True, (255, 255, 255))
      screen.blit(text4, (185, 445))
    elif fac4_flag1 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 100$/s', True, (255, 255, 255))
      screen.blit(text3, (185, 430))
      text4 = font.render(F'need 1000 $ ', True, (255, 255, 255))
      screen.blit(text4, (185, 445))
    else:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'Level MAX', True, (255, 255, 255))
      screen.blit(text3, (185, 430))

      # ５オート
    if fac5_flag3 == True and fac5_flag4 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 1000$/s', True, (255, 255, 255))
      screen.blit(text3, (185, 530))
      text4 = font.render(F'need 26000 $ ', True, (255, 255, 255))
      screen.blit(text4, (185, 545))
    elif fac5_flag2 == True and fac5_flag3 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 700$/s', True, (255, 255, 255))
      screen.blit(text3, (185, 530))
      text4 = font.render(F'need 20000 $ ', True, (255, 255, 255))
      screen.blit(text4, (185, 545))
    elif fac5_flag1 == True and fac5_flag2 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 450$/s', True, (255, 255, 255))
      screen.blit(text3, (185, 530))
      text4 = font.render(F'need 14000 $ ', True, (255, 255, 255))
      screen.blit(text4, (185, 545))
    elif fac5_flag1 == False:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'get 300$/s', True, (255, 255, 255))
      screen.blit(text3, (185, 530))
      text4 = font.render(F'need 5500 $ ', True, (255, 255, 255))
      screen.blit(text4, (185, 545))
    else:
      font = pygame.font.Font(None, 20)
      text3 = font.render(F'Level MAX', True, (255, 255, 255))
      screen.blit(text3, (185, 530))

    # アイテム・実績などの管理
    if coin_num >= 10000 and res1 == False:
      item1 = True
      res1 = True
    if item1 == True:
      screen.fill((DOU), (400, 100, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : First 10000$', True, (255, 255, 255))
      screen.blit(text3, (435, 100))
      text3 = font.render(F'EFFECT : get 100$/s', True, (255, 255, 255))
      screen.blit(text3, (435, 115))
    else:
      screen.fill((WHITE), (400, 100, 30, 30))
      #
    if click_num >= 100 and res2 == False:
      item2 = True
      res2 = True
    if item2 == True:
      screen.fill((DOU), (400, 145, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : 100 Clicker', True, (255, 255, 255))
      screen.blit(text3, (435, 145))
      text3 = font.render(F'EFFECT : Click + 10$', True, (255, 255, 255))
      screen.blit(text3, (435, 160))
    else:
      screen.fill((WHITE), (400, 145, 30, 30))
      # 3
    if click_num >= 1000 and res3 == False:
      item3 = True
      res3 = True
    if item3 == True:
      screen.fill((GIN), (400, 325, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : 1000 Clicker', True, (255, 255, 255))
      screen.blit(text3, (435, 325))
      text3 = font.render(F'EFFECT : Click + 1000$', True, (255, 255, 255))
      screen.blit(text3, (435, 340))
    else:
      screen.fill((WHITE), (400, 325, 30, 30))
      # item10のやつ　afkのやつ
    afk_time += clock.get_time()
    if afk_time >= 15000 and item10 == False:
      item10 = True
    if item10 == True:
      screen.fill((DOU), (400, 190, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : Perhaps neglected?', True, (255, 255, 255))
      screen.blit(text3, (435, 190))
      text3 = font.render(F'EFFECT : I want you to click more!',
                          True, (255, 255, 255))
      screen.blit(text3, (435, 205))
    else:
      screen.fill((WHITE), (400, 190, 30, 30))
      # 6 ガチャ
    if gt_flag6 == True and item4 == False:
      item4 = True
    if item4 == True:
      screen.fill((DOU), (400, 235, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : click machine', True, (255, 255, 255))
      screen.blit(text3, (435, 235))
      text3 = font.render(F'EFFECT : Click + 100$', True, (255, 255, 255))
      screen.blit(text3, (435, 250))
    else:
      screen.fill((WHITE), (400, 235, 30, 30))
      # 5 ガチャ
    if gt_flag5 == True and item5 == False:
      item5 = True
    if item5 == True:
      screen.fill((DOU), (400, 280, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : auto machine', True, (255, 255, 255))
      screen.blit(text3, (435, 280))
      text3 = font.render(F'EFFECT : get 100$/s', True, (255, 255, 255))
      screen.blit(text3, (435, 295))
    else:
      screen.fill((WHITE), (400, 280, 30, 30))
      # 4 ガチャ
    if gt_flag4 == True and item6 == False:
      item6 = True
    if item6 == True:
      screen.fill((GIN), (400, 370, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : Rera auto machine', True, (255, 255, 255))
      screen.blit(text3, (435, 370))
      text3 = font.render(F'EFFECT : get 1000$/s', True, (255, 255, 255))
      screen.blit(text3, (435, 385))
    else:
      screen.fill((WHITE), (400, 370, 30, 30))
      # 3 ガチャ item7
    if gt_flag3 == True and item7 == False:
      item7 = True
    if item7 == True:
      screen.fill((GIN), (400, 415, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : Rera click machine', True, (255, 255, 255))
      screen.blit(text3, (435, 415))
      text3 = font.render(F'EFFECT : click +1000$', True, (255, 255, 255))
      screen.blit(text3, (435, 430))
    else:
      screen.fill((WHITE), (400, 415, 30, 30))
      # 2 ガチャ item8
    if gt_flag2 == True and item8 == False:
      item8 = True
    if item8 == True:
      screen.fill((KIN), (400, 460, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : God click machine', True, (255, 255, 255))
      screen.blit(text3, (435, 460))
      text3 = font.render(F'EFFECT : click + 3000$', True, (255, 255, 255))
      screen.blit(text3, (435, 475))
    else:
      screen.fill((WHITE), (400, 460, 30, 30))
      # 1 ガチャ item9
    if gt_flag1 == True and item9 == False:
      item9 = True
    if item9 == True:
      screen.fill((KIN), (400, 505, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : God click machine', True, (255, 255, 255))
      screen.blit(text3, (435, 505))
      text3 = font.render(F'EFFECT : click + 3000$', True, (255, 255, 255))
      screen.blit(text3, (435, 520))
    else:
      screen.fill((WHITE), (400, 505, 30, 30))
      # item11
    if res4 == True and item11 == False:
      item11 = True
    if item11 == True:
      screen.fill((KIN), (400, 550, 30, 30))
      font = pygame.font.Font(None, 24)
      text3 = font.render(F'NAME : MAX CLICK PAWER!', True, (255, 255, 255))
      screen.blit(text3, (435, 550))
      text3 = font.render(F'EFFECT : Nothing to give.', True, (255, 255, 255))
      screen.blit(text3, (435, 565))
    else:
      screen.fill((WHITE), (400, 550, 30, 30))

      # 一秒間に貰えるお金の計算をする場所
    clock_time += clock.get_time()
    if clock_time >= 1000:
      clock_time = 0
      # 3オート
      if fac3_flag4 == True:
        coin_num += 250
      elif fac3_flag3 == True:
        coin_num += 100
      elif fac3_flag2 == True:
        coin_num += 50
      elif fac3_flag1 == True:
        coin_num += 10
      # 4オート
      if fac4_flag4 == True:
        coin_num += 500
      elif fac4_flag3 == True:
        coin_num += 350
      elif fac4_flag2 == True:
        coin_num += 200
      elif fac4_flag1 == True:
        coin_num += 100
      # 5オート
      if fac5_flag4 == True:
        coin_num += 1000
      elif fac5_flag3 == True:
        coin_num += 700
      elif fac5_flag2 == True:
        coin_num += 450
      elif fac5_flag1 == True:
        coin_num += 300
        # アイテム効果
      if item5 == True:
        coin_num += 100
      if item5 == True:
        coin_num += 100
      if item1 == True:
        coin_num += 100
      if item6 == True:
        coin_num += 1000
      if item9 == True:
        coin_num += 3000
    pygame.display.flip()
    clock.tick(60)
    sprite_group.update()

game_start()
