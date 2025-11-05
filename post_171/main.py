from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

CODE_FONT = "Iosevka"
FONT_SIZE = 32
FONT = dict(font=CODE_FONT, font_size=FONT_SIZE)
TOP_EDGE = UP * 0.25 * config.frame_height
LEFT_EDGE = LEFT * 0.25 * config.frame_width


class MainScene(Scene):
    def construct(self):
        s1 = self.type_number_list()
        # self.bs_text(s1)


        # Wait before close the scene
        self.wait(3)

    def type_number_list(self):
        # cursor
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = .5,
            width = .25,
        )

        # Text
        s = "numbers = [5, 9, 1, 4, 2]"
        text = Text(s, **FONT)
        text.to_edge(TOP_EDGE)
        text.to_edge(LEFT_EDGE)

        cursor.move_to(text[0])
        
        # Animation
        self.play(TypeWithCursor(text, cursor))
        self.play(Blink(cursor, blinks=2))

        self.wait()

        self.play(UntypeWithCursor(text, cursor, keep_cursor_y=True, hell="some"))

        
        self.remove(cursor)

        return text

    def bs_text(self, rec_text):
        text = Text("hello world")

        self.cursor.move_to(text[0])

        self.wait(1)
        self.play(UntypeWithCursor(text, self.cursor))

