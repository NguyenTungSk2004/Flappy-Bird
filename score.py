import pygame
pygame.init()
game_font = pygame.font.Font('04B_19.TTF',40)
score = 0 # Tính điểm
hscore = 0 # Điểm cao nhất
def score_view(screen, game_play):
    if game_play:
        score_f = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_f.get_rect(center=(200,100))
        screen.blit(score_f,score_rect)
    else:
        score_f = game_font.render(f'Score: {str(int(score))}',True,(255,255,255))
        score_rect = score_f.get_rect(center=(200,450))
        screen.blit(score_f,score_rect)
        score_f = game_font.render(f'High score: {str(int(hscore))}',True,(255,255,255))
        score_rect = score_f.get_rect(center=(200,350))
        screen.blit(score_f,score_rect)