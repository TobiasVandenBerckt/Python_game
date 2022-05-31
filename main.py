import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle of Wezemaal")

white = (255, 255, 255)
black = (0, 0, 0)
width_players, height_players = (70, 70)

fps = 60
vel = 5

player_1_hit = pygame.USEREVENT + 1
player_2_hit = pygame.USEREVENT + 2

health_font = pygame.font.SysFont('comicsans', 40)

player_1 = pygame.image.load(os.path.join('extra', 'player1.png'))
player_1 = pygame.transform.scale(player_1, (width_players, height_players))

player_2 = pygame.image.load(os.path.join('extra', 'player2.png'))
player_2 = pygame.transform.scale(player_2, (width_players, height_players))
# image omdraaien: (heb ik al gedaan met de foto)
#player_2 = pygame.transform.rotate(pygame.transform.scale(player_2, (width_players, height_players)), 90)
# initialize a attack range
ATTACK_RANGE = 5


def can_attack(player_one, player_two):
    if player_one.x + ATTACK_RANGE > player_two.x or player_two - ATTACK_RANGE < player_one.x:
        return True
    else:
        return False


def draw_window(player_one, player_two):
    win.fill(white)
    win.blit(player_1, (player_one.x, player_one.y))
    win.blit(player_2, (player_two.x, player_two.y))
    pygame.display.update()


def movement_player1(keys_pressed, player_one, player_two):
    if keys_pressed[pygame.K_q] and player_one.x - vel > 0:  # left
        player_one.x -= vel

    if keys_pressed[pygame.K_d] and player_one.x + vel <= 820:  # right
        if player_one.x < player_two.x:
            player_one.x += vel


def movement_player2(keys_pressed, player_two, player_one):
    if keys_pressed[pygame.K_k] and player_two.x - vel > 0:  # left
        if player_two.x > player_one.x:
            player_two.x -= vel

    if keys_pressed[pygame.K_m] and player_two.x + vel <= 820:  # right
        player_two.x += vel


def player1_hit(player_one, player_two, keys_pressed):
    if keys_pressed[pygame.K_z]:
        player_two.x == 700


def main():
    player_one = pygame.Rect(100, 300, width_players, height_players)
    player_two = pygame.Rect(700, 300, width_players, height_players)

    player_one_health = 5
    player_two_health = 5

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        movement_player1(keys_pressed, player_one, player_two)
        movement_player2(keys_pressed, player_two, player_one)
        player1_hit(player_one, player_two, keys_pressed)
        print(can_attack(player_one, player_two))
        draw_window(player_one, player_two)

    pygame.quit()


if __name__ == "__main__":
    main()
