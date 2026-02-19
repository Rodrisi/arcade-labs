import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Granja con Moto y Avión")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        # Moto
        self.moto_x = 600
        self.moto_y = 120
        self.velocidad_moto = 3

        # Avión
        self.avion_x = -100
        self.avion_y = 550
        self.velocidad_avion = 9

    def on_draw(self):
        self.clear()

        # --- PASTO ---
        # Corregido: de draw_lrtb a draw_lrbt y el orden de los números (0 a 200)
        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.BITTER_LIME)

        # --- GRANERO ---
        arcade.draw_lrbt_rectangle_filled(30, 350, 170, 210, arcade.color.BISQUE)
        arcade.draw_lrbt_rectangle_filled(30, 350, 210, 350, arcade.color.BROWN)
        
        # Ventanas granero
        arcade.draw_rect_filled(arcade.XYWH(70, 260, 30, 40), arcade.color.BONE)
        arcade.draw_rect_filled(arcade.XYWH(70, 260, 20, 30), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(310, 260, 30, 40), arcade.color.BONE)
        arcade.draw_rect_filled(arcade.XYWH(310, 260, 20, 30), arcade.color.BLACK)
        
        # Puerta
        arcade.draw_rect_filled(arcade.XYWH(190, 230, 100, 100), arcade.color.BLACK_BEAN)
        arcade.draw_rect_filled(arcade.XYWH(190, 280, 180, 5), arcade.color.BONE)
        
        # Techo
        arcade.draw_polygon_filled([[20, 350], [100, 470], [280, 470], [360, 340]], arcade.color.BROWN)
        arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BROWN)

        # ==========================================
        #       DIBUJO DE LA MOTO NEGRA
        # ==========================================
        # Chasis y Cuerpo
        arcade.draw_rect_filled(arcade.XYWH(self.moto_x, self.moto_y, 90, 20), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(self.moto_x - 10, self.moto_y + 15, 50, 25), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(self.moto_x + 25, self.moto_y + 12, 40, 10), arcade.color.DARK_GRAY)
        
        # Manillar
        arcade.draw_rect_filled(arcade.XYWH(self.moto_x - 30, self.moto_y + 35, 5, 30), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(self.moto_x - 35, self.moto_y + 45, 15, 5), arcade.color.BLACK)

        # Rueda Delantera
        arcade.draw_circle_filled(self.moto_x - 45, self.moto_y - 10, 25, arcade.color.BLACK)
        arcade.draw_circle_filled(self.moto_x - 45, self.moto_y - 10, 18, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(self.moto_x - 45, self.moto_y - 10, 12, arcade.color.OLD_LACE)
        arcade.draw_circle_filled(self.moto_x - 45, self.moto_y - 10, 4, arcade.color.RED)

        # Rueda Trasera
        arcade.draw_circle_filled(self.moto_x + 45, self.moto_y - 10, 25, arcade.color.BLACK)
        arcade.draw_circle_filled(self.moto_x + 45, self.moto_y - 10, 18, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(self.moto_x + 45, self.moto_y - 10, 12, arcade.color.OLD_LACE)
        arcade.draw_circle_filled(self.moto_x + 45, self.moto_y - 10, 4, arcade.color.RED)

        # Detalles (Faro y Escape)
        arcade.draw_circle_filled(self.moto_x - 40, self.moto_y + 25, 6, arcade.color.WHITE_SMOKE)
        arcade.draw_rect_filled(arcade.XYWH(self.moto_x + 30, self.moto_y - 5, 50, 7), arcade.color.GRAY)

        # ==========================================
        #               AVIÓN
        # ==========================================
        # Fuselaje
        arcade.draw_ellipse_filled(self.avion_x, self.avion_y, 120, 40, arcade.color.BLACK)
        # Cabina
        arcade.draw_ellipse_filled(self.avion_x + 45, self.avion_y + 5, 25, 15, arcade.color.LIGHT_BLUE)
        # Ala superior
        arcade.draw_polygon_filled([
            [self.avion_x - 20, self.avion_y + 10],
            [self.avion_x + 10, self.avion_y + 10],
            [self.avion_x - 10, self.avion_y + 45],
            [self.avion_x - 30, self.avion_y + 45]
        ], arcade.color.GRAY)
        # Cola
        arcade.draw_polygon_filled([
            [self.avion_x - 45, self.avion_y + 10],
            [self.avion_x - 60, self.avion_y + 40],
            [self.avion_x - 40, self.avion_y + 40],
            [self.avion_x - 30, self.avion_y + 10]
        ], arcade.color.DARK_GRAY)

    def on_update(self, delta_time):
        # Mover moto
        self.moto_x += self.velocidad_moto
        if self.moto_x > SCREEN_WIDTH + 150:
            self.moto_x = -150

        # Mover avión
        self.avion_x += self.velocidad_avion
        if self.avion_x > SCREEN_WIDTH + 100:
            self.avion_x = -100

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()