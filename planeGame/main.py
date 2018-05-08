import pygame
import sys
from pygame.locals import *
import math
from random import *
from tkinter import *
import webbrowser
from tkinter import colorchooser
from planeGame import music
from planeGame import myplane
from planeGame import enemy
from planeGame import bullet
from planeGame import boom

pygame.init()
pygame.mixer.init()

BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

bg_size = width, height = 690,700
#bg_size = width, height = pygame.display.list_modes()[6]
screen = pygame.display.set_mode(bg_size)
bg_image = r"E:\JetBrains\workspace_2\project1\00XX\006XWZdqgy1fmwzau1djcj30j60pkgr5.jpg"
background = pygame.image.load(bg_image).convert()
pygame.display.set_caption("嘟嘟")
clock = pygame.time.Clock()

#我方飞机
myplane_image1 = r"E:\JetBrains\image\wsparticle_jiabailie.png"
myplane_image2 = r"E:\JetBrains\image\wsparticle_hulu12.png"
myplane_image3 = r"E:\JetBrains\image\wsparticle_hulu13.png"
myplane_image4 = r"E:\JetBrains\image\wsparticle_guanyu9.png"
plane_image = [myplane_image1,myplane_image2,myplane_image3,myplane_image4]
plane = myplane.Plane(*plane_image,bg_size)


#音乐
music_init = music.Music(r"E:\JetBrains\game music\bgm_cunshiqujinbi.mp3")
music_fit = music.Music(r"E:\JetBrains\game music\bgm_zhandou1.mp3")



#敌方小飞机
small_enemy_image_red = r"E:\JetBrains\image\wsparticle_daoju7.png"
small_enemy_image_yellow = r"E:\JetBrains\image\wsparticle_daoju6.png"
small_enemy_image_green = r"E:\JetBrains\image\wsparticle_daoju5.png"
small_list = [small_enemy_image_red,small_enemy_image_yellow,small_enemy_image_green]

mid_enemy_image1 = r"E:\JetBrains\image\wsparticle_honghaier01.png"
mid_enemy_image2 = r"E:\JetBrains\image\wsparticle_jingzhu01.png"
mid_image_list = [mid_enemy_image1]

big_enemy_image = r"E:\JetBrains\image\wsparticle_change005.png"


#sound_init = music.Music(r"E:\JetBrains\game music\effcet_sfx_bianqiaokeli.mp3")
#sound_next = music.Music(r"E:\JetBrains\game music\effcet_sfx_bossjiesuan.mp3")

def add_small_enemies(group1,group2,num):
    for i in range(num):
        smallEnemy = enemy.SmallEnemy(*small_list, bg_size)
        group1.add(smallEnemy)
        group2.add(smallEnemy)
def add_mid_enemies(group1,group2,num):
    for i in range(num):
        midEnemy = enemy.MidEnemy(*mid_image_list, bg_size)
        group1.add(midEnemy)
        group2.add(midEnemy)
def add_big_enemies(group1,group2,num):
    for i in range(num):
        bigEnemy = enemy.BigEnemy(big_enemy_image, bg_size)
        group1.add(bigEnemy)
        group2.add(bigEnemy)

def add_boom_blue(group1,group2,num,bg_size):
    for i in range(num):
        blue_boom = boom.BlueBoom(bg_size)
        group1.add(blue_boom)
        group2.add(blue_boom)

def add_bullet_yellow(group1,group2,num,bg_size):
    for i in range(num):
        yellow_bullet = boom.YellowBullet(bg_size)
        group1.add(yellow_bullet)
        group2.add(yellow_bullet)

def add_red_supply(group1,group2,num,bg_size):
    for i in range(num):
        supply = boom.RedPackge(bg_size)
        group1.add(supply)
        group2.add(supply)

def showEnergyColor(m,w): #me  who
    pygame.draw.line(screen, BLACK,
    (m.rect.left, m.rect.top - 5),
    (m.rect.right, m.rect.top - 5),3)

    # if w == enemy.SmallEnemy:
    #     energy_remain = m.energy // w.energy
    # else:
    energy_remain = m.energy / w.energy
    if w == enemy.SmallEnemy:
        if energy_remain <= 0.5:
            energy_color = RED
        else:
            energy_color = GREEN
    else:
        if energy_remain <= 0.3:
            energy_color = RED
        else:
            energy_color = GREEN

    pygame.draw.line(screen, energy_color,
                     (m.rect.left, m.rect.top - 5),
                     (m.rect.left + m.rect.width * energy_remain,
                      m.rect.top - 5), 3)

def main():

    #music_init.music_play()
    #pygame.time.delay(100)
    #music_fit.music_play()
    ######sound_init.sound_play()
    ######sound_next.sound_play()

    #设置变量，用于切换图片
    switch_image = 1

    #标志是否暂停游戏
    pause = False

    level = 0

    #得分
    score = 0
    font = pygame.font.Font(r"E:\JetBrains\01.ttf", 35)
    #炸弹数目显示字体
    font_boom = pygame.font.Font(r"E:\JetBrains\01.ttf", 40)

    #显示炸弹图标
    boom_visible = boom.BoomVisible(bg_size)

    switch_mid_image = False

    enemies = pygame.sprite.Group()

    # 生成敌方小飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)

    #生成中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,2)

    #生成大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)

    #中弹图片索引
    small_destroy_index = 0
    mid_destroy_index = 0
    big_destroy_index = 0
    me_destroy_index = 0

    #生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(plane.rect.midtop))

    #生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 8
    for i in range(BULLET2_NUM // 2):
        bullet2.append(bullet.Bullet2((plane.rect.centerx - 33,plane.rect.centery)))
        bullet2.append(bullet.Bullet2((plane.rect.centerx + 33, plane.rect.centery)))

    #每30秒发放3个补给箱
    # 蓝色补给箱,补充炸弹数目
    boom_group = pygame.sprite.Group()
    blue_boom_group = pygame.sprite.Group()
    add_boom_blue(blue_boom_group, boom_group, 1,bg_size)

    #黄色补给箱，改变普通子弹形态
    yellow_bullet = pygame.sprite.Group()
    add_bullet_yellow(yellow_bullet,boom_group,3,bg_size)

    #红色补给箱,将普通子弹变成超级子弹
    red_supply = pygame.sprite.Group()
    add_red_supply(red_supply,boom_group,3,bg_size)

    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME,30 * 1000)

    #超级子弹定时器
    DOUBLE_BULLET_TIME = USEREVENT + 1
    pygame.time.set_timer(DOUBLE_BULLET_TIME,15 * 1000)

    #标志是否使用超级子弹
    is_double_bullet = False

    running = True

    k = 0

    #延迟加载
    delay = 100

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    #游戏暂停
                    pause = not pause
                    if pause:
                        pygame.time.set_timer(SUPPLY_TIME,0)
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
                if event.key == K_1:
                    #使用炸弹
                    if plane.boom_num:
                        plane.boom_num -= 1
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
            elif event.type == SUPPLY_TIME:
                for each in boom_group:
                    if choice([True,False]):
                        each.reset()
            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME,0)


        #检测键盘操作。如果是频繁的键盘操作，使用这种方式
        key_press = pygame.key.get_pressed()
        if key_press[K_w] or key_press[K_UP]:
            plane.moveUp()
            switch_image = 1
        if key_press[K_s] or key_press[K_DOWN]:
            plane.moveDown()
            switch_image = 4
        if key_press[K_a] or key_press[K_LEFT]:
            plane.moveLeft()
            switch_image = 3
        if key_press[K_d] or key_press[K_RIGHT]:
            plane.moveRight()
            switch_image = 2


        #根据用户得分设置难度
        if level == 0 and score > 30000:
            level = 1
            #每一帧添加两架小飞机。一架中型飞机
            add_small_enemies(small_enemies, enemies, 2)
            add_mid_enemies(mid_enemies, enemies, 1)
        if level == 1 and score > 50000:
            level = 2
            #每一帧添加3架小飞机。2架中型飞机
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
        if level == 2 and score > 100000:
            level = 3
            #每一帧添加5架小飞机。3架中型飞机,1架大飞机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 1)
        if level == 3 and score > 150000:
            #每一帧添加20架小飞机。10架中型飞机,15架大飞机
            add_small_enemies(small_enemies, enemies, 20)
            add_mid_enemies(mid_enemies, enemies, 10)
            add_big_enemies(big_enemies, enemies, 5)



        #绘制背景
        #screen.blit(background,(0,0))
        if not pause:
            screen.blit(background, (0, 0))
            #每10帧重置一颗子弹的位置,发射子弹
            if not(delay % 10):
                if is_double_bullet:
                    bullets = bullet2
                    bullet2[bullet2_index].reset((plane.rect.centerx - 33,plane.rect.centery))
                    bullet2[bullet2_index+1].reset((plane.rect.centerx + 33, plane.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
                else:
                    bullets = bullet1
                    bullet1[bullet1_index].reset(plane.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM
            #检测子弹是否击中敌机
            for each in bullets:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                    bullet_enemies_collide = pygame.sprite.spritecollide(each,enemies,False,pygame.sprite.collide_mask)
                    if bullet_enemies_collide:
                        each.active = False
                        for i in bullet_enemies_collide:
                            #if i in mid_enemies or i in big_enemies
                            i.energy -= 1
                            if i.energy == 0:
                                i.active = False
                else:
                    each.reset(plane.rect.midtop)
                    each.active = True
            #enemy还有被打中的图片，即self.hit = True
            #绘制敌方大型飞机
            for each in big_enemies:
                if each.active:
                    #不让两个大型机碰撞，虽然没啥意义 - - 偶就是复习一下这个 - -
                    big_enemies.remove(each)
                    while pygame.sprite.spritecollide(each,big_enemies,False,pygame.sprite.collide_mask):
                        each.rect.left = randint(0, each.width - each.rect.width)  # 0, self.width - self.rect.width
                        each.rect.top = randint(-10 * each.height, -each.height)  # -10 * self.height, -self.height
                    big_enemies.add(each)
                    each.move()
                    screen.blit(each.image,each.rect)

                    # 绘制血槽
                    showEnergyColor(each,enemy.BigEnemy)
                else:
                    #毁灭
                    # music_fit.music_play()  #如果写在这里，则绘画毁灭的过程中每一帧都会播放音乐
                    if not (delay % 3):
                        if big_destroy_index == 0:
                            pass
                            # music_fit.music_play() #毁灭的音效值播放一次。
                        screen.blit(each.destroy_images[big_destroy_index],each.rect)
                        big_destroy_index = (big_destroy_index + 1) % len(each.destroy_images) #总共4张图，余4结果只会在0到3之间
                        if big_destroy_index == 0:
                            score += 10000
                            each.reset()

            #绘制敌方中型飞机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain <= 0.2:
                        energy_color = RED
                    else:
                        energy_color = GREEN
                    showEnergyColor(each,enemy.MidEnemy)
                else:
                    #毁灭
                    if not (delay % 3):
                        screen.blit(each.destroy_images[mid_destroy_index],each.rect)
                        mid_destroy_index = (mid_destroy_index + 1) % len(each.destroy_images) #总共4张图，余4结果只会在0到3之间
                        if mid_destroy_index == 0:
                            score += 6000
                            each.reset()

            #绘制敌方小飞机
            for each in small_enemies:
                if each.active:
                    each.move()
                    small_enemy_list_image = [each.image_red, each.image_yellow, each.image_green]
                    screen.blit(small_enemy_list_image[randint(0,2)],each.rect)

                    # 绘制血槽
                    # pygame.draw.line(screen, BLACK,
                    #                  (each.rect.left, each.rect.top - 5),
                    #                  (each.rect.right, each.rect.top - 5),3)
                    #当生命大于20%显示绿色,否则显示红色
                    showEnergyColor(each,enemy.SmallEnemy)
                else:
                    if not (delay % 3):
                        screen.blit(each.destroy_images[small_destroy_index],each.rect)
                        small_destroy_index = (small_destroy_index + 1) % len(each.destroy_images) #总共4张图，余4结果只会在0到3之间
                        if small_destroy_index == 0:
                            score += 1000
                            each.reset()

            #检测我方飞机是否被撞
            me_enemies_collide = pygame.sprite.spritecollide(plane,enemies,False,pygame.sprite.collide_mask)  #检测me是否和enemies这组精灵中的任何一个精灵碰撞,返回enemies中与plane的元素列表
            if me_enemies_collide:
                plane.active = False
                for each in me_enemies_collide:
                    each.active = False

            #绘制我方飞机
            if plane.active:
                if switch_image == 1:
                    screen.blit(plane.image_up,plane.rect)
                    #screen.blit(plane.destroy_images[1],plane.rect)
                elif switch_image == 2:
                    screen.blit(plane.image_right, plane.rect)
                    switch_image = 1
                elif switch_image == 3:
                    screen.blit(plane.image_left, plane.rect)
                    switch_image = 1
                elif switch_image == 4:
                    screen.blit(plane.image_down, plane.rect)
                    switch_image = 1
            else:
                #毁灭
                if not (delay % 3):
                    screen.blit(plane.destroy_images[me_destroy_index], plane.rect)
                    me_destroy_index = (me_destroy_index + 1) % len(plane.destroy_images)  # 总共4张图，余4结果只会在0到3之间
                    if me_destroy_index == 0:
                        #plane.reset()
                        pass

            for each in boom_group:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                    #检测我方飞机是否吃到补给箱
                    me_boom_collide = pygame.sprite.spritecollide(plane,boom_group,False,pygame.sprite.collide_mask)
                    if me_boom_collide:
                        for each in me_boom_collide:
                            #蓝色补给箱，补充炸弹
                            if each in blue_boom_group:
                                if plane.boom_num < 3:
                                    plane.boom_num += 1
                                each.active = False
                                me_boom_collide.remove(each)
                            if each in yellow_bullet:
                                each.active = False
                                pass
                            if each in red_supply:
                                is_double_bullet = True
                                pygame.time.set_timer(DOUBLE_BULLET_TIME,15 * 1000)
                                each.active = False


        #绘制剩余炸弹数目:
        boom_text = font_boom.render("x%d" % plane.boom_num,True,GREEN)
        #boom_text_rect = boom_text.get_rect()
        screen.blit(boom_visible.image,boom_visible.rect)
        screen.blit(boom_text,(43,boom_visible.rect.top))

        #绘制分数
        score_text = font.render(("Score: %s" % str(score)),True,BLUE)
        screen.blit(score_text,(10,5))

        switch_mid_image = not switch_mid_image  #原本想给中型飞机两个素材不断切换的。没有好的素菜。画面很难看，就没用切换了，变量就放在这了，遇到合适的素材再重写代码吧

        delay -= 1
        if not delay:
            delay = 100
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()



