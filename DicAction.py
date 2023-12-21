import pygame,random
pipe_height = [300,400,500]

def draw_pipe(pipes,pipe_surface,screen):
    for pipe in pipes:
        if pipe.bottom >= 688:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False, True)
            screen.blit(flip_pipe,pipe)
            
def create_pipe(pipe_surface):
    random_height = random.choice(pipe_height)
    bottom = pipe_surface.get_rect(midtop=(500,random_height))
    top = pipe_surface.get_rect(midtop=(500,random_height-700))
    return bottom, top

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -=2
    return pipes

def rotate_bird(Bird,bird):
	new_bird = pygame.transform.rotozoom(Bird,-bird.y*3,1)
	return new_bird

def bird_animation(bird_list, bird_index, bird_rect):
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect
    
    