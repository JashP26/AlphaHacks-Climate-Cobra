import pygame as pg
from Settings_CC import *
from Sprites_CC import *
import random
from os import path

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Climate Cobra")
clock = pg.time.Clock()

def draw_text(text, size, font, color, x, y):
    wanted_font = pg.font.match_font(str(font))
    font = pg.font.Font(wanted_font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text_surface, text_rect)

game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder, "img")
def load_img(img):
    return pg.image.load(path.join(imgs_folder, str(img))).convert()
fossil_fuel_img = load_img("fossil_fuel.png")
deforestation_img = load_img("deforestation.png")
oil_spill_img = load_img("oil_spill.png")
agriculture_img = load_img("agriculture.png")
cobra_img = load_img("cobra.png")
plastic_bag_img = load_img("plastic_bag.png")
background_img = load_img("background_map.png")
fossil_fuel = pg.transform.scale(fossil_fuel_img, (50, 50))
deforestation = pg.transform.scale(deforestation_img, (50, 50))
oil_spill = pg.transform.scale(oil_spill_img, (50, 40))
agriculture = pg.transform.scale(agriculture_img, (50, 50))
pollution_img = (fossil_fuel, deforestation, oil_spill, agriculture)
cobra = pg.transform.scale(cobra_img, (50, 50))
plastic_bag = pg.transform.scale(plastic_bag_img, (50, 50))

background = pg.transform.scale(background_img, (1027, 600))
background_rect = background.get_rect()

class Game_Loop():
    def __init__(self):
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.collectables = pg.sprite.Group()
        self.pollutions = pg.sprite.Group()
        self.tail = pg.sprite.Group()
        self.maze = pg.Surface((600, 600))
        self.maze.fill(BLUE)
        self.maze_rect = self.maze.get_rect()
        self.cobra = Player(cobra)
        self.collectable = Collectables(plastic_bag)
        self.avoid = Pollution(random.choice(pollution_img))
        self.all_sprites.add(self.cobra)
        self.all_sprites.add(self.collectable)
        self.all_sprites.add(self.avoid)
        self.collectables.add(self.collectable)
        self.pollutions.add(self.avoid)
        self.scores = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
        self.spawn_rate = int(self.cobra.score / 3) + 1
        self.intro_box = Text_Box(WIDTH - 100, HEIGHT - 100, WIDTH / 2, HEIGHT / 2)
        self.info_box = Text_Box(290, HEIGHT - 20, WIDTH - 150, HEIGHT / 2 - 5)
        self.facts = [self.fff1, self.fff2, self.dff1, self.dff2, self.opf1, self.opf2, self.af1, self.af2]
        self.fact = random.choice(self.facts)
        self.start_screen()

    def start_screen(self):
        self.cobra_img = pg.transform.scale(cobra, (100, 100))
        self.cobra_rect = self.cobra_img.get_rect()
        self.plastic_bag = pg.transform.scale(plastic_bag, (100, 100))
        self.plastic_bag_rect = self.plastic_bag.get_rect()
        self.fossil_fuel = pg.transform.scale(fossil_fuel, (100, 100))
        self.fossil_fuel_rect = self.fossil_fuel.get_rect()
        self.deforestation = pg.transform.scale(deforestation, (100, 100))
        self.deforestation_rect = self.deforestation.get_rect()
        self.oil_spill = pg.transform.scale(oil_spill, (100, 100))
        self.oil_spill_rect = self.oil_spill.get_rect()
        self.agriculture = pg.transform.scale(agriculture, (100, 100))
        self.agriculture_rect = self.agriculture.get_rect()
        while self.running:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    self.running = False
            screen.blit(background, background_rect)
            screen.blit(self.intro_box.image, self.intro_box.rect)
            draw_text("CLIMATE COBRA", 80, "arial black", GREEN, WIDTH / 2, HEIGHT - 450)
            draw_text("Help the cobra by collecting plastic waste that was", 20, "arial", BLUE, WIDTH - 300, HEIGHT - 350)
            draw_text("littered and can either be recycled or disposed properly", 20, "arial", BLUE, WIDTH - 300, HEIGHT - 320)
            draw_text("Avoid fossil fuels, deforestation, agriculture, and oil spills as their", 20, "arial", RED, WIDTH - 300, HEIGHT - 175)
            draw_text("frequent use produces more greenhouse gasses and", 20, "arial", RED, WIDTH - 300, HEIGHT - 155)
            draw_text("damages the environment", 20, "arial", RED, WIDTH - 300, HEIGHT - 135)
            draw_text("Press any key to continue", 15, "arial", BLACK, WIDTH / 2, HEIGHT - 25)
            self.cobra_rect.center = (WIDTH - 750, HEIGHT - 335)
            self.plastic_bag_rect.center = (WIDTH - 625, HEIGHT - 335)
            self.fossil_fuel_rect.center = (WIDTH - 625, HEIGHT - 210)
            self.deforestation_rect.center = (WIDTH - 750, HEIGHT - 210)
            self.oil_spill_rect.center = (WIDTH - 750, HEIGHT - 110)
            self.agriculture_rect.center = (WIDTH - 625, HEIGHT - 110)
            screen.blit(self.cobra_img, self.cobra_rect)
            screen.blit(self.plastic_bag, self.plastic_bag_rect)
            screen.blit(self.fossil_fuel, self.fossil_fuel_rect)
            screen.blit(self.deforestation, self.deforestation_rect)
            screen.blit(self.oil_spill, self.oil_spill_rect)
            screen.blit(self.agriculture, self.agriculture_rect)
            pg.display.flip()
        self.game_loop()

    def game_loop(self):
        self.running = True
        while self.running:
            clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        self.end_screen()

    def end_screen(self):
        self.running = True
        while self.running:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            screen.blit(background, background_rect)
            screen.blit(self.intro_box.image, self.intro_box.rect)
            draw_text("CLIMATE COBRA", 80, "arial black", GREEN, WIDTH / 2, HEIGHT - 450)
            draw_text("Despite the cobra doing its part towards climate change, there was still an increase in", 25, "arial", BLUE, WIDTH / 2, HEIGHT - 350)
            draw_text("pollution. This is because everyone needs to do their part in living more sustainable", 25, "arial", BLUE, WIDTH / 2, HEIGHT - 300)
            draw_text("lives from how much energy we use daily to what companies we buy from. We need to", 25, "arial", BLUE, WIDTH / 2, HEIGHT - 250)
            draw_text("raise awareness towards climate change and do a little research to slow down and", 25, "arial", BLUE, WIDTH / 2, HEIGHT - 200)
            draw_text("stop its effects. To learn more about climate change, please visit the website down", 25, "arial", BLUE, WIDTH / 2, HEIGHT - 150)
            draw_text("below and thank you for playing our game.", 25, "arial", BLUE, WIDTH / 2, HEIGHT - 100)
            draw_text("https://climate.nasa.gov/", 25, "arial", BLUE, WIDTH / 2, HEIGHT - 25)
            pg.display.flip()


    def events(self):
        # events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            #hits = pg.sprite.spritecollide(self.cobra, self.collectables, True)
        hits = pg.sprite.collide_rect(self.cobra, self.collectable)
        if hits:
            self.cobra.score += 1
            self.collectable.kill()
            self.spawn_collectable()
            self.spawn_pollution()

        hits = pg.sprite.spritecollide(self.cobra, self.pollutions, True)
        for hit in hits:
                self.running = False

    def update(self):
        # update
        self.all_sprites.update()
        self.spawn_rate = int(self.cobra.score / 3) + 1

    def draw(self):
        # draw
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(self.info_box.image, self.info_box.rect)
        self.all_sprites.draw(screen)
        self.collectables.draw(screen)
        self.pollutions.draw(screen)
        draw_text(str(self.cobra.score), 60, "Comic Sans", BLUE, WIDTH - 150, HEIGHT - 40)
        self.fact()
        pg.display.flip()

    def spawn_collectable(self):
        self.collectable = Collectables(plastic_bag)
        self.all_sprites.add(self.collectable)
        self.collectables.add(self.collectable)

    def spawn_pollution(self):
        while len(self.pollutions) < self.spawn_rate:
            self.pollution = Pollution(random.choice(pollution_img))
            self.all_sprites.add(self.pollution)
            self.pollutions.add(self.pollution)
            self.fact = random.choice(self.facts)

    def dff1(self):
        draw_text("In Australia's wildfires in 2020,", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 550)
        draw_text("about 46 million acres of land", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 520)
        draw_text("were burned and about 3 billion", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 490)
        draw_text("animals died from them.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 460)

    def dff2(self):
        draw_text("The smoke from the Australian wildfires", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 550)
        draw_text("was the same amount of smoke that a", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 520)
        draw_text("volcano gives off. All of this smoke", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 490)
        draw_text("adds to the excess greenhouse gases.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 460)

    def opf1(self):
        draw_text("With the USA alone, about a thousand", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 550)
        draw_text("oil spills happen in the ocean each", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 520)
        draw_text("year that damage the marine life.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 490)

    def opf2(self):
        draw_text("In the Deepwater Horizon oil spill,", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 550)
        draw_text("about 134 tons of oil was spilled", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 520)
        draw_text("into the Gulf of Mexico, and it is", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 490)
        draw_text("still being cleaned to this day.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 460)

    def af1(self):
        draw_text("Agriculture contributes to climate", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 550)
        draw_text("change greatly from factory-based", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 520)
        draw_text("livestock farming and erosion in topsoil.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 490)

    def af2(self):
        draw_text("With the world's large population,", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 550)
        draw_text("large food exporters like India", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 520)
        draw_text("and China face difficulties in", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 490)
        draw_text("making agriculture sustainable.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 460)

    def fff1(self):
        draw_text("Many countries rely on fossil fuels", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 550)
        draw_text("as their main energy source. Since", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 520)
        draw_text("the burning of fossil fuels creates", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 490)
        draw_text("CO2, a greenhouse gas, they", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 460)
        draw_text("significantly worsen climate change.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 430)

    def fff2(self):
        draw_text("USA, China, India are the 3", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 550)
        draw_text("countries that emit the most CO2.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 520)
        draw_text("These countries have the most", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 490)
        draw_text("emissions, because they need much", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 460)
        draw_text("energy to support their large", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 430)
        draw_text("populations.", 20, "arial", BLUE, WIDTH - 150, HEIGHT - 400)

main_loop = Game_Loop()