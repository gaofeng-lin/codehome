import pygame
import random
import numpy as np

# 初始化Pygame
pygame.init()

# 屏幕大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumping Heart with Fireworks")

# 心形参数
heart_color = (255, 0, 0)
heart_scale = 10
heart_speed = 5
heart_x = screen_width // 2
heart_y = screen_height // 2

# 烟花参数
fireworks = []

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清空屏幕
    screen.fill((0, 0, 0))

    # 绘制心形
    heart_points = [(heart_x + heart_scale * 16 * (np.sin(t) ** 3),
                     heart_y - heart_scale * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)))
                    for t in np.linspace(0, 2 * np.pi, 1000)]
    pygame.draw.polygon(screen, heart_color, heart_points)

    # 更新心形位置
    heart_y += heart_speed
    if heart_y > screen_height:
        heart_y = -50

    # 生成烟花
    if random.random() < 0.05:
        x = random.randint(0, screen_width)
        y = screen_height
        fireworks.append([x, y])

    # 绘制烟花
    for firework in fireworks:
        pygame.draw.circle(screen, (255, 255, 0), firework, 5)
        firework[1] -= 5
        if firework[1] < 0:
            fireworks.remove(firework)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
