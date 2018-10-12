import pygame
from blob import Blob

WEIDTH = 800
HEIGHT = 600
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [0, 0, 255]

STARTING_RED_BLOB = 20
STARTING_BLUE_BLOB = 20
STARTING_GREEN_BLOB = 20

game_display = pygame.display.set_mode([WEIDTH, HEIGHT])
pygame.display.set_caption('Blob')
clock = pygame.time.Clock()


class Red_Blob(Blob):
    def __init__(self, x_boundry, y_boundry):
        super().__init__([255, 0, 0], x_boundry, y_boundry)


class Blue_Blob(Blob):
    def __init__(self, x_boundry, y_boundry):
        super().__init__([0, 0, 255], x_boundry, y_boundry)


class Green_Blob(Blob):
    def __init__(self, x_boundry, y_boundry):
        super().__init__([0, 255, 0], x_boundry, y_boundry)

# class Child_Blob(Blob):
#     def move_fast(self):
#         self.x += random.randrange(-7, 7)
#         self.y += random.randrange(-7, 7)

def draw_environment(blobs_list):
    game_display.fill(WHITE)
    for blobs_dict in blobs_list:
        for blob_id in blobs_dict:
            blob = blobs_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
    pygame.display.update()




def main():
    red_blob = dict(enumerate([Red_Blob(WEIDTH, HEIGHT) for _ in range(STARTING_RED_BLOB)]))
    blue_blob = dict(enumerate([Blue_Blob(WEIDTH, HEIGHT) for _ in range(STARTING_BLUE_BLOB)]))
    green_blob = dict(enumerate([Green_Blob(WEIDTH, HEIGHT) for _ in range(STARTING_GREEN_BLOB)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([red_blob, blue_blob, green_blob])
        clock.tick(60)


if __name__ == '__main__':
    main()
