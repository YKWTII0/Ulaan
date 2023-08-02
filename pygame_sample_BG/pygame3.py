import pygame

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370
# background.png의 크기에 맞게 조절

def back(x, y): # 배경 이미지를 게임판 위에 그려주는 함수
    global gamepad, background
    gamepad.blit(background, (x, y))

def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))

def runGame():
    global gamepad, aircraft, clock, background

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background_x = 0 # 배경 이미지의 좌상단 모서리의 x좌표 초기화

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
            if event.type == pygame.KEYDOWN: # 키를 누르는 이벤트
                if event.key == pygame.K_UP: # 위 화살표 키를 눌렀을 때
                    y_change -= 5 # y좌표 : 위로 5 이동
                elif event.key == pygame.K_DOWN: # 아래 화살표 키를 눌렀을 때
                    y_change += 5 # y좌표 : 아래로 5 이동
            
            if event.type == pygame.KEYUP: # 키를 떼는 이벤트
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                # 위 화살표 키를 누르는 이벤트 또는 아래 화살표 키를 누르는 이벤트 발생 시
                # y_change = 0으로 초기화
                    y_change = 0
        
        y += y_change

        gamepad.fill(WHITE)
        back(background_x, 0) # 좌상단 모서리 x좌표, y좌표를 인자로 전달
        airplane(x, y)
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock, background

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("PyFlying")
    aircraft = pygame.image.load("image/images/plane.png")
    background = pygame.image.load("image/images/background.png")

    clock = pygame.time.Clock()
    runGame()

initGame()