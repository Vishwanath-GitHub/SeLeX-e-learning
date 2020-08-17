def my_Player(vidPath):
    import pyglet
    window = pyglet.window.Window()
    window.set_size(640, 480)
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vidPath)
    player.queue(MediaLoad)
    player.play()


    @window.event
    def on_draw():
        if player.source and player.source.video_format:
            player.get_texture().blit(0, 0)


    pyglet.app.run()