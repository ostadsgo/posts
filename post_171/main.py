from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

FONT_FAMILY = "Source Code Pro"
FONT_SIZE = 32
TOP_EDGE = UP * 0.25 * config.frame_height
LEFT_EDGE = LEFT * 0.25 * config.frame_width


class MainScene(Scene):
    def construct(self):
        print("Left", LEFT, "LEFT / 2", LEFT / 2)
        # config
        d1 = Line(config.frame_width * LEFT, config.frame_width * RIGHT).to_edge(DOWN)
        d2 = Line(config.frame_width * LEFT, config.frame_width * RIGHT).to_edge(UP)
        d3 = Line(config.frame_height * UP, config.frame_height * DOWN).to_edge(LEFT)
        d4 = Line(config.frame_height * UP, config.frame_height * DOWN).to_edge(RIGHT)
        self.add(d1)
        self.add(d2)
        self.add(d3)
        self.add(d4)

        # ---------------------------
        #   Animation (0) - Blinks
        #----------------------------
        # Objects
        cursor = Rectangle(width=.25, height=.5, fill_opacity=1, color="#984936", )
        # Postions
        cursor.to_edge(UL)
        # Animations
        self.play(Blink(cursor, blinks=3))


        # ---------------------------
        #   Animation (1) - numbers
        #----------------------------
        # Objects
        text = Text("numbers = [5, 9, 1, 4, 2]", font=FONT_FAMILY, font_size=FONT_SIZE)
        # Positions
        text.to_edge(LEFT_EDGE)
        text.to_edge(TOP_EDGE)
        # Animations
        self.play(TypeWithCursor(text, cursor))









        self.wait(3)

