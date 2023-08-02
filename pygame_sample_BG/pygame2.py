import pygame

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 512

def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))

def runGame():
    global gamepad, aircraft, clock

    x = pad_width * 0.05 # 비행기의 최초 위치 설정
    y = pad_height * 0.8 # 비행기의 최초 위치 설정
    y_change = 0 # 비행기가 아래 위로 움직이므로 y좌표 변화를 y_change 변수로 나타낸다

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

        y += y_change # 키보드 입력에 따라 y좌표 변경

        gamepad.fill(WHITE)
        airplane(x, y) # 비행기의 새 위치를 그리기
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("PyFlying")
    aircraft = pygame.image.load("image/images/plane.png")

    clock = pygame.time.Clock()
    runGame()

initGame()