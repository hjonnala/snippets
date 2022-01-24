from coral.enviro.board import EnviroBoard
from luma.core.render import canvas
import time

enviro = EnviroBoard()


def update_display(display, msg):
    with canvas(display) as draw:
        draw.text((0, 0), msg, fill='white')

update_display(enviro.display, "Hello world")
time.sleep(20)
