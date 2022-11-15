import pygame
import sys
from sprites import *
from config import *
import time


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = Spritesheet('img/reindeer.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy3.png')
        self.santa_spritesheet = Spritesheet('img/santa.png')

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "D" or column == "L" or column == "R" or column == "T" or column == "Y" or column == "F" or column == "G" or column == "U" or column == "B":
                    Block(self, j, i, column)
                if column == "P":
                    Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "S":
                    Santa(self, j, i)

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.santa = pygame.sprite.LayeredUpdates()
        self.createTilemap()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def game_over(self):
        pass
    def intro_Screen(self):
        pass



g = Game()
g.intro_Screen()
g.new()
while g.running:
    g.main()
    g.new()

pygame.quit()
sys.exit()
