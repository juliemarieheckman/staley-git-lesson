import pygame
player_x = 200
player_y = 300
class KeyHandler():
    def __init__(self, gamestate):
        self.gamestate = gamestate
        self.actions = {
            "overworld": {
                "z": self.overworld_talk,
                "x": self.overworld_run,
                "up": self.overworld_up,
                "down": self.overworld_down,
                "left": self.overworld_left,
                "right": self.overworld_right},
            "battle": {
                "z": self.battle_talk,
                "x": self.battle_run,
                "up": self.battle_up,
                "down": self.battle_down,
                "left": self.battle_left,
                "right": self.battle_right},
        }

    def overworld_talk():
        ""

    def handle_key(self, key):
        """Run the correct action for this key + current state"""
        action = self.actions.get(self.game_state, {}).get(key)
        if action == self.overworld_talk:
           'overworld_talk()'

class Camera:
    def __init__(self, player_x, player_y, screen_width, screen_height):
        self.player_x = player_x
        self.player_y = player_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset_x = 0
        self.offset_y = 0
    
    def update(self, player_x, player_y):
        # Center camera on player (key step!)
        self.offset_x = max(0, int(player_x - self.screen_width // 2))
        self.offset_y = max(0, int(player_y - self.screen_height // 2))

class GameManager:
    def __init__(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
        self.camera = Camera(player_x, player_y, 800, 608)
    
    def update(self, player_x, player_y):
        self.camera.update(player_x, player_y)