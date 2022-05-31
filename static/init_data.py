"""
Initial data for Game of Life
"""
CELL_SIZE = 8
RADIUS = int(CELL_SIZE/2)
GAP_SIZE = 1
WIDTH = 64
HEIGHT = 48
MENU_HEIGHT = 100
BUTTON_DIMENSIONS_X = 80
BUTTON_DIMENSIONS_Y = 42
DIVIDER_SIZE = 2
BTN_GAP_SIZE = 10
BUTTONS = [{
        "index": 0,
        "image_path": "./assets/stop.bmp",
        "action": "stop",
        "is_visible": True
    },
    {
        "index": 1,
        "image_path": "./assets/play.bmp",
        "action": "play",
        "is_visible": True
    },
    {
        "index": 2,
        "image_path": "./assets/randomize.bmp",
        "action": "randomize",
        "is_visible": True
    },
    {
        "index": 3,
        "image_path": "./assets/step.bmp",
        "action": "step",
        "is_visible": True
    },
    {
        "index": 4,
        "image_path": "./assets/clear.bmp",
        "action": "clear",
        "is_visible": True
    }]
STATUSES =[{
        "index": 0,
        "image_path": "./assets/status.bmp",
        "is_visible": True
    },
    {
        "index": 1,
        "image_path": "./assets/status_run.bmp",
        "is_visible": False
    },
    {
        "index": 2,
        "image_path": "./assets/status_stop.bmp",
        "is_visible": True
    }]
STATUS_DIMENSIONS_X = 104
STATUS_DIMENSIONS_Y = 42
