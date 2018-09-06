import game_visual
import random
import pygame

class Game:
    def __init__(self, dimension):
        self.DIMENSIONS = dimension
        self.NUM_ROW = dimension
        self.NUM_COL = dimension
        self.content = [[Number(0) for r in range(self.NUM_ROW)] for c in range(self.NUM_COL)]
        self.running = True
        self.waiting_for_move = True
        self.score = 0

    def spawn(self):
        if self.waiting_for_move:
            empty_coord_list = []
            for r in range(self.NUM_ROW):
                for c in range(self.NUM_COL):
                    if self.content[r][c].value == 0:
                        empty_coord_list.append((r, c))
            
            random_one = random.randint(0, len(empty_coord_list) - 1)        
            if len(empty_coord_list) != 0:
                self.content[empty_coord_list[random_one][0]][empty_coord_list[random_one][1]] = Number(random.randint(1,2) * 2)
                self.waiting_for_move = False
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Score: "  + str(self.score))
                self._end_game()
            if event.type == pygame.VIDEORESIZE:
                game_visual._resize_surface(self, event.size)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._up()
                elif event.key == pygame.K_DOWN:
                    self._down()
                elif event.key == pygame.K_LEFT:
                    self._left()
                elif event.key == pygame.K_RIGHT:
                    self._right()
                    
    def _up(self):
        temp = False
        'Match contents'
        for r in range(self.NUM_ROW):
            for c in range(self.NUM_COL):
                for x in range(c, self.NUM_COL - 1):
                    if not self._check_match(self.content[r][c], self.content[r][x + 1]) and self.content[r][x + 1].value != 0:
                        break
                    if self._check_match(self.content[r][c], self.content[r][x + 1]):
                        self.content[r][c] = Number(self.content[r][c].value * 2)
                        self.content[r][x + 1] = Number(0)
                        self.score += self.content[r][c].value                        
                        c += 1
                        temp = True
                        break
        'Move all contents up'
        for r in range(self.NUM_ROW):
            for c in range(self.NUM_COL):
                if self.content[r][c].value == 0:
                    for x in range(c, self.NUM_COL):
                        if self.content[r][x].value != 0:
                            self.content[r][c], self.content[r][x] = self.content[r][x], Number(0)
                            temp = True
                            break
        self.waiting_for_move = temp
    
    def _down(self):
        temp = False
        'Match contents'
        for r in range(self.NUM_ROW):
            for c in range(1, self.NUM_COL + 1):
                for x in range(c, self.NUM_COL):
                    if not self._check_match(self.content[r][-c], self.content[r][-x - 1]) and self.content[r][-x - 1].value != 0:
                        break
                    if self._check_match(self.content[r][-c], self.content[r][-x - 1]):
                        self.content[r][-c] = Number(self.content[r][-c].value * 2)
                        self.content[r][-x - 1] = Number(0)
                        self.score += self.content[r][-c].value                        
                        c += 1
                        temp = True
                        break
        'Move all contents down'
        for r in range(self.NUM_ROW):
            for c in range(1, self.NUM_COL):
                if self.content[r][-c].value == 0:
                    for x in range(c, self.NUM_COL + 1):
                        if self.content[r][-x].value != 0:
                            self.content[r][-c], self.content[r][-x] = self.content[r][-x], Number(0)
                            temp = True
                            break
        self.waiting_for_move = temp
                    
                    
    
    def _left(self):
        temp = False
        'Match contents'
        for r in range(self.NUM_ROW):
            for c in range(self.NUM_COL - 1):
                for x in range(c, self.NUM_COL - 1):
                    if not self._check_match(self.content[c][r], self.content[x + 1][r]) and self.content[x + 1][r].value != 0:
                        break
                    if self._check_match(self.content[c][r], self.content[x + 1][r]):
                        self.content[c][r], self.content[x + 1][r] = Number(self.content[x + 1][r].value * 2), Number(0)
                        self.score += self.content[c][r].value
                        c += 1
                        temp = True
                        break
        'Move all contents up'
        for r in range(self.NUM_ROW):
            for c in range(self.NUM_COL - 1):
                if self.content[c][r].value == 0:
                    for x in range(c, self.NUM_COL):
                        if self.content[x][r].value != 0:
                            self.content[c][r], self.content[x][r] = self.content[x][r], Number(0)
                            temp = True
                            break
        self.waiting_for_move = temp
    
    def _right(self):
        temp = False
        'Match contents'
        for r in range(self.NUM_COL):
            for c in range(1, self.NUM_ROW):
                for x in range(c, self.NUM_ROW):
                    if not self._check_match(self.content[-c][r], self.content[-x - 1][r]) and self.content[-x - 1][r].value != 0:
                        break
                    if self._check_match(self.content[-c][r], self.content[-x - 1][r]):
                        self.content[-c][r], self.content[-x - 1][r] = Number(self.content[-x - 1][r].value * 2), Number(0)
                        self.score += self.content[-c][r].value
                        c += 1
                        temp = True
                        break
        'Move all contents up'
        for r in range(self.NUM_ROW):
            for c in range(1, self.NUM_COL):
                if self.content[-c][r].value == 0:
                    for x in range(c, self.NUM_COL + 1):
                        if self.content[-x][r].value != 0:
                            self.content[-c][r], self.content[-x][r] = self.content[-x][r], Number(0)
                            temp = True
                            break
        self.waiting_for_move = temp
        if self.check_lose() : self._end_game()
    
    def check_lose(self):
        for r in range(self.NUM_ROW):
            for c in range(self.NUM_COL):
                if self.content[r][c].value == 0:
                    return False
                else:
                    try:
                        if self.content[r][c] == self.content[r - 1][c]: return False
                    except IndexError:
                        pass
                    try:
                        if self.content[r][c] == self.content[r + 1][c]: return False
                    except IndexError:
                        pass
                    try:
                        if self.content[r][c] == self.content[r][c - 1]: return False
                    except IndexError:
                        pass
                    try:
                        if self.content[r][c] == self.content[r][c + 1]: return False
                    except IndexError:
                        pass
        return True
    
    def _check_match(self, first, second):
        return first == second and first.value != 0

    def _end_game(self):
        self.running = False
        
        
class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, right):
        if type(right) != Number: raise TypeError
        return self.value == right.value
    
    def __str__(self):
        return str(self.value) if self.value != 0 else ''
    
    def __len__(self):
        return len(str(self.value))
                