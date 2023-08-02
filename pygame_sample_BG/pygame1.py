import pygame # pygame 모듈 불러오기 pygame ачааллын модуль

WHITE = (255, 255, 255) # RGB color (255, 255, 255) -> WHITE
pad_width = 1024 # 게임 공간의 너비 тоглоомын талбайн өргөн
pad_height = 512 # 게임 공간의 높이 тоглоомын талбайн өндөр

# initGame 함수로 게임을 초기화하고 시작, runGame 함수로 실제 게임 구동
# InitGame функцээр тоглоомыг эхлүүлж, эхлүүлж, runGame функцээр бодит тоглоомыг ажиллуул.
def runGame(): # runGame() : 실제 게임이 구동되는 함수 runGame() : Тоглоомыг үнэхээр ажиллуулдаг функц
    global gamepad, clock # 전역 변수 선언 глобал хувьсагчийн мэдэгдэл

    crashed = False # 게임을 종료하기 위한 플래그 тоглоомыг дуусгах туг
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gamepad.fill(WHITE) # if문이 아닐 경우 게임판을 흰색으로 다시 그린다
        pygame.display.update()
        clock.tick(60) # FPS 값을 60으로 설정하여 while문 반복

    pygame.quit() # pygame 라이브러리를 초기화 Pygame номын санг эхлүүлэх

def initGame(): # initGame() : 게임을 초기화하고 시작하는 함수 initGame() : Тоглоомыг эхлүүлэх, эхлүүлэх функц
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("Pyflying") # 게임판 타이틀 тоглоомын самбарын гарчиг

    clock = pygame.time.Clock() # 클락 생성해서 게임의 초당 프레임 설정 Тоглоомынхоо фрэймийн секундийг тохируулах цагийг үүсгэ
    runGame() # 게임 구동을 위한 함수 호출 Тоглоомыг ажиллуулах функцийг дуудаж байна

initGame()