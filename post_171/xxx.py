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

sq_opt = dict(side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0)

class MainScene(Scene):
    def construct(self):
        self.numbers = [5, 9, 3, 1, 4]
        self.box_g = VGroup()
        cursor = self.get_cursor()

        # cursor point
        h = self.header("Python built-in functions")

        # Blink cursor
        cursor.next_to(h, DOWN, buff=1.0)
        cursor.to_edge(LEFT_EDGE)
        self.play(Blink(cursor, blinks=1))
        self.remove(cursor)

        t1 = self.type_text("numbers = [5, 9, 3, 1, 4]", h)
        
        # self.boxes()
        
        # max
        t2 = self.type_text("max(numbers)", t1)
        # self.box_dim([0, 2, 3, 4])
        # self.box_shift([1])
        # self.wait()
        # self.box_shift([1], DOWN)
        # self.box_undim()

        # min
        self.bs_text(t2)


        self.wait(10)

    def header(self, text):
        t = Text(text, **FONT)
        t.to_edge(TOP_EDGE)
        # self.play(Write(t))
        return t

    def get_cursor(self):
        cur = Rectangle(
            color = "#984936",
            fill_color = "#984936",
            fill_opacity = 0.8,
            height = 0.47,
            width = 0.2,
        )
        return cur

    def type_text(self, text, after, buff=1.0):
        t = Text(text, **FONT)
        t.next_to(after, DOWN, buff=buff)
        t.to_edge(LEFT_EDGE)

        cursor = self.get_cursor().move_to(t[0])
        self.add(cursor)

        self.play(TypeWithCursor(t, cursor))
        self.play(Blink(cursor, blinks=2))
        self.play(FadeOut(cursor))
        self.remove(cursor)
        del(cursor)
        return t

    def bs_text(self, text):
        t = text.copy()
        x = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 2.1,
            width = 0.5,
        ).move_to(t[0])
        self.play(UntypeWithCursor(t, x))
        self.play(Blink(x, blinks=2))
        self.play(FadeOut(x))


    def boxes(self):
        for number in self.numbers:
            text = Text(str(number), **FONT)
            square = Square(**sq_opt)
            box = VGroup(square, text)
            self.box_g.add(box)

        self.box_g.arrange(RIGHT, buff=0.5)
        self.box_g.to_edge(LEFT_EDGE)

        # Animation on each box
        for box in self.box_g:
            self.play(GrowFromCenter(box))

    def box_shift(self, indexes, dir=UP):
        anims = []
        for index in indexes:
            anims.append(self.box_g[index].animate.shift(dir * .5))
        self.play(*anims)

    def box_dim(self, indexes):
        anims = []
        for index in indexes:
            anims.append(self.box_g[index].animate.set_fill(opacity=0.2).set_stroke(opacity=0.2))
        self.play(*anims)

    def box_undim(self):
        anims = []
        for index in range(len(self.numbers)):
            anims.append(self.box_g[index].animate.set_fill(opacity=1.0).set_stroke(opacity=1.0))
        self.play(*anims)








