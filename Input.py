import pyglet, random
from pyglet.window import key
from pyglet.window import mouse

clearSound = pyglet.resource.media('rocket_locking_beep1.wav', streaming=False)

mousePos = {'x': 0, 'y': 0}
window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

def randomComponent():
	return random.randint(0, 255)

def randomColor():
	return (randomComponent(), randomComponent(), randomComponent(), 128)

def label(text, x, y):
	return pyglet.text.Label(
		text,
		font_name='Consolas',
		color=randomColor(),
		font_size=random.randint(10, 40),
		x=x,
		y=y, 
		anchor_x='center',
		anchor_y='center',
		batch=batch
	)

@window.event
def on_mouse_motion(x, y, dx, dy):
	global mousePos
	mousePos = {'x': x, 'y': y}

@window.event
def on_key_press(symbol, modifiers):
	global batch
	msg = key.symbol_string(symbol)
	label(msg, mousePos['x'], mousePos['y'])
	if symbol == key.SPACE:
		#clear the screen
		batch = pyglet.graphics.Batch()
		clearSound.play()

@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		b = 'L'
	elif button == mouse.MIDDLE:
		b = 'M'
	else:
		b = 'R'
	str = '%s(%d, %d)' % (b, x, y)
	label(str, x, y)

@window.event
def on_draw():
	window.clear()
	batch.draw()
	
pyglet.app.run()
