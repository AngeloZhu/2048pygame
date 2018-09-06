import game_mechanics
import pygame

NUMBER_COLORS = {'': (0, 0, 0),
                 '2': (150, 149, 244), 
                 '4': (170, 123, 209),
                 '8': (31, 176, 209),
                 '16': (230, 109, 255),
                 '32': (108, 65, 160),
                 '64': (255, 86, 159),
                 '128': (255, 86, 92),
                 '256': (97, 218, 226),
                 '512': (97, 226, 175),
                 '1024': (81, 188, 69),
                 '2048': (246, 255, 132),
                 '4096': (255, 195, 132)
                 }

def run(game):
    pygame.init()
    
    _resize_surface(game, (500, 500))
    game.spawn()
    game.waiting_for_move = True
    game.spawn()
    while game.running:
        if game.check_lose():
            #game._end_game()
            print('You lose!')
            print('Score: ' + str(game.score))
        game.handle_events()
        game.spawn()
        _redraw(game)
    
    pygame.quit()

def _redraw(game):
    surface = pygame.display.get_surface()
    surface.fill(pygame.Color(255, 255, 255))
    
    _draw_board(game)
    _draw_content(game)
    
    pygame.display.flip()


def _resize_surface(game, size):
    pygame.display.set_mode(size, pygame.RESIZABLE)
    _resize(game)
    _draw_board(game)
    
def _resize(game):
    surface = pygame.display.get_surface()
    game.width, game.height = pygame.Surface.get_size(surface)

def _draw_board(game):
    surface = pygame.display.get_surface()
    width, height = pygame.Surface.get_size(surface)
    
    for i in range(1, game.NUM_COL):
        pygame.draw.line(surface, (0, 0, 0), ((width / game.NUM_COL) * i, 0), \
            ((width / game.NUM_COL) * i, height), 1)

    for i in range(1, game.NUM_ROW):
        pygame.draw.line(surface, (0, 0, 0), (0, height / game.NUM_ROW * i), \
            (width, height / game.NUM_ROW * i), 1)

def _draw_content(game):
    surface = pygame.display.get_surface()
    width, height = pygame.Surface.get_size(surface)
    font = pygame.font.SysFont('microsoftyaheimicrosoftyaheiui', int(((width / game.NUM_COL + height / game.NUM_ROW) / 2) / 3))#int((width + height)/2 / (game.NUM_COL * 3)))
    
    for r in range(game.NUM_ROW):
        for c in range(game.NUM_COL):
            label = font.render(str(game.content[r][c]), 1, NUMBER_COLORS[str(game.content[r][c])])
            surface.blit(label, _get_center_pixel(game, r, c, game.content[r][c]))

def _get_center_pixel(game, row, col, number_obj):
    char_len = len(number_obj)
    surface = pygame.display.get_surface()
    width, height = pygame.Surface.get_size(surface)
    x = (width / game.NUM_ROW) * row  +  int(((width / game.NUM_COL + height / game.NUM_ROW) / 2) / 3) - ((char_len - 1) * int(((width / game.NUM_COL + height / game.NUM_ROW) / 2) / 10))
    y = (height / game.NUM_COL) * col + ((height / game.NUM_COL) / game.NUM_COL)
    return (x, y)
    