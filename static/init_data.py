font_size = 24
cell_size = 8
radius = int(cell_size/2)
gap_size = 1
width = 64
height = 48
menu_height = 100
button_dimensions_x = 80
button_dimensions_y = 42
divider_size = 2
btn_gap_size = 10
buttons = [{
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
statuses=[{
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

status_dimensions_x = 104
status_dimensions_y = 42