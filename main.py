import pygame
import size, score, collide, DicAction

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen=pygame.display.set_mode((size.bg.width,size.bg.height))
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load(r'assets\\midflap.png')
pygame.display.set_icon(icon)

# Các biến hình ảnh
Background = pygame.transform.scale2x(pygame.image.load(r'.\\assets\\background-night.png'))
Floor = pygame.transform.scale2x(pygame.image.load(r'.\\assets\\floor.png'))
Game_over = pygame.transform.scale2x(pygame.image.load(r'.\\assets\\gameover.png'))
Message = pygame.transform.scale2x( pygame.image.load(r'.\\assets\\message.png'))
Pipe = pygame.transform.scale2x( pygame.image.load(r'.\\assets\\pipe.png'))
Midflap = pygame.transform.scale2x(pygame.image.load(r'.\\assets\\midflap.png').convert_alpha())
Upflap = pygame.transform.scale2x( pygame.image.load(r'.\\assets\\upflap.png').convert_alpha())
Downflap = pygame.transform.scale2x(pygame.image.load(r'.\\assets\\downflap.png').convert_alpha())

# kích thước các hình ảnh x2
fl = size.floor
pipe = size.pipe
over = size.over
flap = size.flap
mes = size.mes
bird = size.bird

# Các biến xử lý
p = 0.1 # Trọng lực
game_play = False # Check va chạm
start = True # Hiển thị message start game
pipe_list = [] 
bird_index = 0
bird_list = [Midflap, Upflap, Downflap] # Danh sách random bird

# tạo timer cho pipe
spawnpipe = pygame.USEREVENT 
pygame.time.set_timer(spawnpipe,1200) 

# tạo timer cho bird vỗ cánh
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)

# Các biến liên quan đến màn hình
bird_rect = Midflap.get_rect(center=(bird.width,bird.height))
over_rect = Game_over.get_rect(center=(over.width,over.height+75))
message_rect = Message.get_rect(center=(mes.width,mes.height))

#Chèn âm thanh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')

score_sound_countdown = 200
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
# Vòng lặp game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_play:
                #chim bay lên
                bird.y = -6 
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_play == False:
                if start:
                    bird.y= 0
                    game_play = True
                    start = False
                    bird_rect.center = (bird.width,bird.height)
                    score.score = 0
                else:
                    start = True
        if event.type == spawnpipe: 
            pipe_list.extend(DicAction.create_pipe(Pipe))
        if event.type == birdflap:
            #Xử lí đập cánh chim
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index =0 
            Midflap, bird_rect = DicAction.bird_animation(bird_list, bird_index, bird_rect)    

    screen.blit(Background,(0,0))

    if start:
        screen.blit(Message,message_rect) # Màn hình khởi động
    elif game_play:
        # Bird rơi
        bird.y += p
        bird_rect.centery += bird.y
        rotated_Bird = DicAction.rotate_bird(Midflap, bird)
        screen.blit(rotated_Bird,bird_rect)
        #Xử lí va chạm 
        game_play = collide.check_vc(bird_rect,pipe_list)
        # Hành động của cái ống
        pipe_list = DicAction.move_pipe(pipe_list)
        DicAction.draw_pipe(pipe_list,Pipe,screen)
        # xử lí âm thanh tính điểm
        score.score +=0.005
        score.score_view(screen, game_play)
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 200
    else:
        score_sound_countdown = 200
        screen.blit(Game_over,over_rect) 
        if score.hscore < score.score:
            score.hscore = score.score
        score.score_view(screen, game_play)
        pipe_list.clear()
    
    #xử lí Floor
    fl.x -=1
    fl.y = size.bg.height-fl.height+50+56
    if -1*fl.x == fl.width:
        fl.x = 0
    screen.blit(Floor,(fl.x,fl.y))
    screen.blit(Floor,(fl.width+fl.x,fl.y))

    pygame.display.update()

pygame.quit()