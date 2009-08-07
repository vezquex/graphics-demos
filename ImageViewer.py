import pyglet, random
window = pyglet.window.Window()
image = pyglet.resource.image('HelloWorld.png')

@window.event
def on_draw():
	window.clear()
	image.blit(0, 0)
	
pyglet.app.run()
