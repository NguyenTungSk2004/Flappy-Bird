import pygame

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')

def check_vc(bird,pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            hit_sound.play()
            return False
    if bird.bottom >= 688 or bird.top <= -75:
        return False
    return True