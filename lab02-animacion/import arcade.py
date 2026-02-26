import arcade

# Inicializa la ventana (opcional si solo quieres sonidos)
arcade.open_window(640, 480, "Prueba de sonido")

# Cargar un sonido corto
sound = arcade.load_sound("resources/sounds/coin2.wav")
arcade.play_sound(sound)

# Cargar música larga
music = arcade.load_sound("resources/music/1918.mp3", streaming=True)
arcade.play_sound(music)

# Mantener el programa corriendo unos segundos para escuchar la música
arcade.run()
