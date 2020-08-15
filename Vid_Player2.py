def my_Player(vidPath):
    import pyglet
    window = pyglet.window.Window()
    #window.set_size(1280, 720)
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vidPath)
    player.queue(MediaLoad)
    player.play()


    @window.event
    def on_draw():
        if player.source and player.source.video_format:
            player.get_texture().blit(50, 50)


    pyglet.app.run()