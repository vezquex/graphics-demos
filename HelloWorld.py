import pyglet, random
window = pyglet.window.Window()

def randomComponent():
	return random.randint(0, 255)

def randomColor():
	return (randomComponent(), randomComponent(), randomComponent(), randomComponent())

def randomLabels():
	batch = pyglet.graphics.Batch()
	for i in range(3):
		pyglet.text.Label(
			'Hello World Ex Machina',
			font_name='Consolas',
			color=randomColor(),
			font_size=42,
			x=random.randint(0, window.width),
			y=random.randint(0, window.height), 
			anchor_x='center',
			anchor_y='center',
			batch=batch
		)
	return batch

@window.event
def on_draw():
	window.clear()
	randomLabels().draw()
	
pyglet.app.run()
