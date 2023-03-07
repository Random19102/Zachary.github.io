from ursina import *
from ursina.prefabs.first_person_controller import *

with open("wardrobe.py", "r") as f:
    exec(f.read())
thing=input('Fullscreen mode? ')
thing.lower()
if thing=='y':
    window.fullscreen=True
elif thing=='n':
    window.fullscreen=False
else:
    sys.quit()

"""thing2=input('FPS counter?')
thing2.lower()
if thing2=='y':
    window.fps_counter.enabled = True
elif thing2=='n':
    window.fps_counter.enabled = False
else:
    sys.quit()"""

window.title= 'PyDOORS'



app=Ursina()
player=FirstPersonController()
a=Audio('Soundtracks/Elevatorjam', autoplay=True, loop=False,volume=5)
area=Entity(collider='box', model='plane', scale=(100, 50, 100), texture='grass')
#arm=Entity(model='arm', parent=camera, scale=(0.8), x=0.5, y=-0.75, z=-0.5, texture='arm_texture')
item2=wardrobe()
item3=Entity(collider='box', model='Elevator', texture='wood', y=1)
rush=Entity(collider='box', model='quad', texture='Rush.png', x=10, z=10, y=2, rotation=180, scale=10, double_sided=True)
test=Entity(collider='box', model='cube', scale=(10,2.5,10), x=10, y=4.25, z=-20)

def input(key):
    if key=='backspace':
        application.quit()

def update():
    global timer
    print(timer)

app.run()