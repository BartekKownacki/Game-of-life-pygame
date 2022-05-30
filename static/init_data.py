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
        "image_path": "./assets/stop.png",
        "action": "stop",
        "is_visible": True
    },
    {
        "index": 1,
        "image_path": "./assets/play.png",
        "action": "play",
        "is_visible": True
    },
    {
        "index": 2,
        "image_path": "./assets/randomize.png",
        "action": "randomize",
        "is_visible": True
    },
    {
        "index": 3,
        "image_path": "./assets/step.png",
        "action": "step",
        "is_visible": True
    },
    {
        "index": 4,
        "image_path": "./assets/clear.png",
        "action": "clear",
        "is_visible": True
    }]
statuses=[{
        "index": 0,
        "image_path": "./assets/status.png",
        "is_visible": True
    },
    {
        "index": 1,
        "image_path": "./assets/status_run.png",
        "is_visible": False
    },
    {
        "index": 2,
        "image_path": "./assets/status_stop.png",
        "is_visible": True
    }]

status_dimensions_x = 104
status_dimensions_y = 42