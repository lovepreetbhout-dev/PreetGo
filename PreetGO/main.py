# PREET GO - FINAL VERSION

import pygame
import sys
import random
import os

pygame.init()
pygame.mixer.init()

# =========================
# WINDOW
# =========================
WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Preet Go")

clock = pygame.time.Clock()

# =========================
# LOAD IMAGES
# =========================
background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background, (400, 600))

shopbg = pygame.image.load("assets/shopbg.jpeg")
shopbg = pygame.transform.scale(shopbg, (400, 600))

settingsbg = pygame.image.load("assets/settingsbg.png")
settingsbg = pygame.transform.scale(settingsbg, (400, 600))

face1 = pygame.image.load("assets/face.png")
face1 = pygame.transform.scale(face1, (70, 70))

face2 = pygame.image.load("assets/face2.png")
face2 = pygame.transform.scale(face2, (70, 70))

burger = pygame.image.load("assets/burger.png")
burger = pygame.transform.scale(burger, (50, 50))

pizza = pygame.image.load("assets/pizza.png")
pizza = pygame.transform.scale(pizza, (50, 50))

cooldrink = pygame.image.load("assets/cooldrink.png")
cooldrink = pygame.transform.scale(cooldrink, (50, 50))

boom = pygame.image.load("assets/boom.png")
boom = pygame.transform.scale(boom, (55, 55))

pipe = pygame.image.load("assets/pipe.png")
pipe = pygame.transform.scale(pipe, (90, 320))

play_btn = pygame.image.load("assets/play.png")
play_btn = pygame.transform.scale(play_btn, (120, 120))

settings_btn = pygame.image.load("assets/settings.png")
settings_btn = pygame.transform.scale(settings_btn, (70, 70))

shop_btn = pygame.image.load("assets/shop.png")
shop_btn = pygame.transform.scale(shop_btn, (70, 70))

home_btn = pygame.image.load("assets/home.png")
home_btn = pygame.transform.scale(home_btn, (120, 60))

gameover_img = pygame.image.load("assets/gameover.png")
gameover_img = pygame.transform.scale(gameover_img, (280, 120))

tick = pygame.image.load("assets/tick.png")
tick = pygame.transform.scale(tick, (30, 30))

# =========================
# SOUNDS
# =========================
jump_sound = pygame.mixer.Sound("sounds/jump.mp3")
collect_sound = pygame.mixer.Sound("sounds/burger.mp3")
pipehit_sound = pygame.mixer.Sound("sounds/pipehit.mpeg")
gameover_sound = pygame.mixer.Sound("sounds/gameover.mp3")
click_sound = pygame.mixer.Sound("sounds/click.mp3")

pygame.mixer.music.load("sounds/bgmusic.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# =========================
# FONT
# =========================
font = pygame.font.SysFont(None, 40)

# =========================
# HIGH SCORE
# =========================
if not os.path.exists("highscore.txt"):
    with open("highscore.txt", "w") as f:
        f.write("0")

with open("highscore.txt", "r") as f:
    high_score = int(f.read())

# =========================
# VARIABLES
# =========================
bg_x = 0

face_x = 80
face_y = 250

velocity = 0
gravity = 0.35

pipe_x = 500
pipe_y = random.randint(-120, -50)

pipe_gap = 210

coin_x = 700
coin_y = random.randint(150, 450)

boom_x = 1000
boom_y = random.randint(120, 500)

score = 0

pipe_count = 0
show_boom = False

sound_on = True

# =========================
# SELECTED ITEMS
# =========================
selected_face = face1
selected_coin = burger

selected_face_name = "PREET"
selected_coin_name = "BURGER"

# =========================
# STATES
# =========================
menu = True
shop = False
settings = False
game_started = False
game_over = False

# =========================
# MAIN LOOP
# =========================
running = True

while running:

    # =====================
    # BACKGROUND
    # =====================
    if shop:
        screen.blit(shopbg, (0, 0))

    elif settings:
        screen.blit(settingsbg, (0, 0))

    else:
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + WIDTH, 0))

    if game_started and not game_over:
        bg_x -= 1

    if bg_x <= -WIDTH:
        bg_x = 0

    # =====================
    # EVENTS
    # =====================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            # ================= MENU =================
            if menu:

                # PLAY
                if 140 < mouse_x < 260 and 320 < mouse_y < 440:

                    click_sound.play()

                    menu = False
                    game_started = True

                # SETTINGS
                if 255 < mouse_x < 330 and 10 < mouse_y < 85:

                    click_sound.play()

                    menu = False
                    settings = True

                # SHOP
                if 325 < mouse_x < 400 and 10 < mouse_y < 85:

                    click_sound.play()

                    menu = False
                    shop = True

            # ================= SETTINGS =================
            elif settings:

                # WRONG BUTTON
                if 0 < mouse_x < 95 and 15 < mouse_y < 110:

                    click_sound.play()

                    settings = False
                    menu = True

                # SOUND BUTTON
                if 110 < mouse_x < 300 and 300 < mouse_y < 390:

                    click_sound.play()

                    if sound_on:

                        pygame.mixer.music.set_volume(0)

                        jump_sound.set_volume(0)
                        collect_sound.set_volume(0)
                        pipehit_sound.set_volume(0)
                        gameover_sound.set_volume(0)
                        click_sound.set_volume(0)

                        sound_on = False

                    else:

                        pygame.mixer.music.set_volume(0.3)

                        jump_sound.set_volume(1)
                        collect_sound.set_volume(1)
                        pipehit_sound.set_volume(1)
                        gameover_sound.set_volume(1)
                        click_sound.set_volume(1)

                        sound_on = True

            # ================= SHOP =================
            elif shop:

                # WRONG BUTTON
                if 0 < mouse_x < 95 and 15 < mouse_y < 110:

                    click_sound.play()

                    shop = False
                    menu = True

                # PREET
                if 70 < mouse_x < 180 and 150 < mouse_y < 310:

                    click_sound.play()

                    selected_face = face1
                    selected_face_name = "PREET"

                # NXZZZ
                if 220 < mouse_x < 330 and 150 < mouse_y < 310:

                    click_sound.play()

                    selected_face = face2
                    selected_face_name = "NXZZZ"

                # BURGER
                if 30 < mouse_x < 120 and 370 < mouse_y < 500:

                    click_sound.play()

                    selected_coin = burger
                    selected_coin_name = "BURGER"

                # PIZZA
                if 150 < mouse_x < 250 and 370 < mouse_y < 500:

                    click_sound.play()

                    selected_coin = pizza
                    selected_coin_name = "PIZZA"

                # COOLDRINK
                if 270 < mouse_x < 370 and 370 < mouse_y < 500:

                    click_sound.play()

                    selected_coin = cooldrink
                    selected_coin_name = "COOLDRINK"

            # ================= GAME =================
            elif game_started:

                if not game_over:

                    velocity = -7
                    jump_sound.play()

                # GAME OVER BUTTONS
                if game_over:

                    # PLAY AGAIN
                    if 140 < mouse_x < 260 and 300 < mouse_y < 420:

                        click_sound.play()

                        face_y = 250
                        velocity = 0

                        pipe_x = 500
                        pipe_y = random.randint(-120, -50)

                        coin_x = 700
                        coin_y = random.randint(150, 450)

                        boom_x = 1000
                        boom_y = random.randint(120, 500)

                        score = 0
                        pipe_count = 0
                        show_boom = False

                        game_over = False

                    # HOME
                    if 140 < mouse_x < 260 and 430 < mouse_y < 500:

                        click_sound.play()

                        game_started = False
                        game_over = False
                        menu = True

                        face_y = 250
                        velocity = 0

                        pipe_x = 500
                        coin_x = 700

                        score = 0
                        pipe_count = 0
                        show_boom = False

    # =====================
    # GAME LOGIC
    # =====================
    if game_started and not game_over:

        velocity += gravity
        face_y += velocity

        pipe_x -= 5
        coin_x -= 5

        if show_boom:
            boom_x -= 5

        # PIPE RESET
        if pipe_x < -90:

            pipe_x = 500
            pipe_y = random.randint(-120, -50)

            pipe_count += 1

            # Every 5 pipes show boom
            if pipe_count >= 5:

                show_boom = True

                boom_x = 700
                boom_y = random.randint(120, 500)

                pipe_count = 0

        # COIN RESET
        if coin_x < -50:

            coin_x = 700
            coin_y = random.randint(150, 450)

        # BOOM RESET
        if boom_x < -55:

            show_boom = False

        # =====================
        # COLLISION
        # =====================
        face_rect = pygame.Rect(face_x + 12, face_y + 12, 45, 45)

        top_pipe = pygame.Rect(pipe_x, pipe_y, 90, 320)

        bottom_pipe = pygame.Rect(
            pipe_x,
            pipe_y + 320 + pipe_gap,
            90,
            320
        )

        coin_rect = pygame.Rect(coin_x, coin_y, 50, 50)

        boom_rect = pygame.Rect(boom_x, boom_y, 55, 55)

        # COIN COLLISION
        if face_rect.colliderect(coin_rect):

            collect_sound.play()

            score += 1

            coin_x = 700
            coin_y = random.randint(150, 450)

        # PIPE COLLISION
        if (
            face_rect.colliderect(top_pipe)
            or
            face_rect.colliderect(bottom_pipe)
        ):

            if not game_over:

                pipehit_sound.play()
                gameover_sound.play()

            game_over = True

        # BOOM COLLISION
        if show_boom and face_rect.colliderect(boom_rect):

            if not game_over:

                pipehit_sound.play()
                gameover_sound.play()

            game_over = True

        # FALL
        if face_y > HEIGHT - 70:

            if not game_over:

                pipehit_sound.play()
                gameover_sound.play()

            game_over = True

        # DRAW PIPE
        screen.blit(pipe, (pipe_x, pipe_y))

        flip_pipe = pygame.transform.flip(pipe, False, True)

        screen.blit(
            flip_pipe,
            (pipe_x, pipe_y + 320 + pipe_gap)
        )

        # DRAW COIN
        screen.blit(selected_coin, (coin_x, coin_y))

        # DRAW BOOM
        if show_boom:
            screen.blit(boom, (boom_x, boom_y))

    # =====================
    # MENU
    # =====================
    if menu:

        screen.blit(selected_face, (150, 180))

        screen.blit(play_btn, (140, 320))

        screen.blit(settings_btn, (255, 10))

        screen.blit(shop_btn, (325, 10))

    # =====================
    # SETTINGS SCREEN
    # =====================
    if settings:

        screen.blit(settingsbg, (0, 0))

        hs_text = font.render(
            str(high_score),
            True,
            (255,255,255)
        )

        screen.blit(hs_text, (255, 220))

    # =====================
    # SHOP SCREEN
    # =====================
    if shop:

        screen.blit(shopbg, (0, 0))

        # BIG SHOP IMAGES
        big_face1 = pygame.transform.scale(face1, (82, 82))
        big_face2 = pygame.transform.scale(face2, (82, 82))

        big_burger = pygame.transform.scale(burger, (70, 70))
        big_pizza = pygame.transform.scale(pizza, (70, 70))
        big_cooldrink = pygame.transform.scale(cooldrink, (70, 70))

        # CHARACTER
        screen.blit(big_face1, (102, 190))
        screen.blit(big_face2, (252, 190))

        # COINS
        screen.blit(big_burger, (55, 425))
        screen.blit(big_pizza, (170, 425))
        screen.blit(big_cooldrink, (285, 425))

        # CHARACTER TICK
        if selected_face_name == "PREET":
            screen.blit(tick, (155, 182))

        if selected_face_name == "NXZZZ":
            screen.blit(tick, (305, 182))

        # COIN TICK
        if selected_coin_name == "BURGER":
            screen.blit(tick, (95, 415))

        if selected_coin_name == "PIZZA":
            screen.blit(tick, (210, 415))

        if selected_coin_name == "COOLDRINK":
            screen.blit(tick, (325, 415))

    # =====================
    # PLAYER
    # =====================
    if game_started:

        screen.blit(selected_face, (face_x, face_y))

    # =====================
    # SCORE
    # =====================
    if game_started:

        score_text = font.render(
            str(score),
            True,
            (255,255,255)
        )

        screen.blit(score_text, (185, 20))

    # =====================
    # SAVE HIGH SCORE
    # =====================
    if score > high_score:

        high_score = score

        with open("highscore.txt", "w") as f:
            f.write(str(high_score))

    # =====================
    # GAME OVER
    # =====================
    if game_over:

        screen.blit(gameover_img, (60, 170))

        # PLAY BUTTON
        screen.blit(play_btn, (140, 300))

        # HOME BUTTON
        screen.blit(home_btn, (140, 430))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()