import os

import pygame

class ResourceManager:
    def __init__(self):
        self._images = {}
        self.base_path = "images"

    def load_image(self, name: str, scale: tuple = None) -> pygame.Surface:
        if name not in self._images:
            path = os.path.join(self.base_path, name)
            try:
                image = pygame.image.load(path).convert_alpha()
                if scale:
                    image = pygame.transform.scale(image, scale)
                self._images[name] = image
            except pygame.error as e:
                print(f"Не удалось загрузить картинку: {path}")
                raise e

        return self._images[name]

    def clear(self):
        self._images = {}