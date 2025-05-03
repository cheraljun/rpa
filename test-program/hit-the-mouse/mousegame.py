import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口大小
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("打地鼠游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 地鼠的数量，可按需调整
MOLE_COUNT = 6
# 地鼠半径
MOLE_RADIUS = 60

# 加载自定义图片
try:
    mole_image = pygame.image.load('mole.png')
    mole_image = pygame.transform.scale(mole_image, (2 * MOLE_RADIUS, 2 * MOLE_RADIUS))
except FileNotFoundError:
    print("未找到自定义图片，请确保 'mole.png' 文件存在。")
    pygame.quit()
    quit()

# 地鼠的状态列表，每个元素是一个元组 (位置, 计时器)
moles = [None] * MOLE_COUNT
score = 0

# 字体设置
font = pygame.font.Font(None, 36)

# 检查新地鼠位置是否与已有地鼠重叠
def is_overlapping(new_pos, existing_moles):
    for mole in existing_moles:
        if mole is not None:
            mole_pos, _ = mole
            distance = ((new_pos[0] - mole_pos[0]) ** 2 + (new_pos[1] - mole_pos[1]) ** 2) ** 0.5
            if distance < 2 * MOLE_RADIUS:
                return True
    return False

# 游戏主循环
running = True
clock = pygame.time.Clock()

while running:
    # 填充白色背景
    screen.fill(WHITE)

    # 处理每个地鼠
    for i in range(MOLE_COUNT):
        if moles[i] is None:
            if random.randint(1, 100) < 2:
                max_attempts = 100  # 最大尝试次数
                attempts = 0
                while attempts < max_attempts:
                    mole_x = random.randint(MOLE_RADIUS, width - MOLE_RADIUS)
                    mole_y = random.randint(MOLE_RADIUS, height - MOLE_RADIUS)
                    new_pos = (mole_x, mole_y)
                    if not is_overlapping(new_pos, moles):
                        moles[i] = (new_pos, 100)
                        break
                    attempts += 1
        else:
            mole_pos, mole_timer = moles[i]
            # 绘制自定义图片
            screen.blit(mole_image, (mole_pos[0] - MOLE_RADIUS, mole_pos[1] - MOLE_RADIUS))
            mole_timer -= 1
            if mole_timer <= 0:
                moles[i] = None
            else:
                moles[i] = (mole_pos, mole_timer)

    # 显示得分，调整位置避免与地鼠重叠
    score_text = font.render(f"得分: {score}", True, BLACK)
    screen.blit(score_text, (width - score_text.get_width() - 10, 10))

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(MOLE_COUNT):
                if moles[i] is not None:
                    mole_pos, _ = moles[i]
                    distance = ((mouse_pos[0] - mole_pos[0]) ** 2 + (mouse_pos[1] - mole_pos[1]) ** 2) ** 0.5
                    if distance < MOLE_RADIUS:
                        score += 1
                        moles[i] = None

    pygame.display.flip()
    clock.tick(200)

# 退出 Pygame
pygame.quit()
    