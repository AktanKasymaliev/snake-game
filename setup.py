import pygame
from random import randrange

class SnakeGame:

    RES = 800
    SIZE = 50

    x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    fps = 60
    dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
    score = 0
    speed_count, snake_speed = 0, 10

    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode([self.RES, self.RES])
        self.clock = pygame.time.Clock()
        self.font_score = pygame.font.SysFont('Arial', 26, bold=True)
        self.font_end = pygame.font.SysFont('Arial', 66, bold=True)
        self.img = pygame.image.load('1.jpg').convert()

    @staticmethod
    def close_game():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def play(self):
        while True:
            self.surface.blit(self.img, (0, 0))

            # drawing snake, apple
            [pygame.draw.rect(self.surface, pygame.Color('green'), (i, j, self.SIZE - 1, self.SIZE - 1)) for i, j in self.snake]
            pygame.draw.rect(self.surface, pygame.Color('red'), (*self.apple, self.SIZE, self.SIZE))

            # show score
            render_score = self.font_score.render(f'SCORE: {self.score}', 1, pygame.Color('orange'))
            self.surface.blit(render_score, (5, 5))

            # snake movement
            self.speed_count += 1
            if not self.speed_count % self.snake_speed:
                self.x += self.dx * self.SIZE
                self.y += self.dy * self.SIZE
                self.snake.append((self.x, self.y))
                self.snake = self.snake[-self.length:]

            # eating food
            if self.snake[-1] == self.apple:
                self.apple = randrange(self.SIZE, self.RES - self.SIZE, self.SIZE), randrange(self.SIZE, self.RES - self.SIZE, self.SIZE)
                self.length += 1
                self.score += 1

            # game over
            if self.x < 0 or self.x > self.RES - self.SIZE or self.y < 0 or self.y > self.RES - self.SIZE or len(self.snake) != len(set(self.snake)):
                while True:
                    render_end = self.font_end.render('GAME OVER', 1, pygame.Color('orange'))
                    self.surface.blit(render_end, (self.RES // 2 - 200, self.RES // 3))
                    pygame.display.flip()
                    self.close_game()

            pygame.display.flip()
            self.clock.tick(self.fps)
            self.close_game()

            # controls
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                if self.dirs['W']:
                    self.dx, self.dy = 0, -1
                    self.dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
            elif key[pygame.K_s]:
                if self.dirs['S']:
                    self.dx, self.dy = 0, 1
                    self.dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
            elif key[pygame.K_a]:
                if self.dirs['A']:
                    self.dx, self.dy = -1, 0
                    self.dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
            elif key[pygame.K_d]:
                if self.dirs['D']:
                    self.dx, self.dy = 1, 0
                    self.dirs = {'W': True, 'S': True, 'A': False, 'D': True, }


if __name__ == "__main__":
    game = SnakeGame()
    while True:
        game.play()