from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

font_opt = dict(font="Source Code Pro", font_size=30)
font_sans = dict(font="Noto Sans", font_size=40, weight=BOLD)
UP_EDGE = UP * 0.25 * config.frame_height
LEFT_EDGE = LEFT * 0.25 * config.frame_width
DOWN_EDGE = DOWN * 0.25 * config.frame_height



class MainScene(Scene):
    def construct(self):

        # colors
        red = "#984936"

        self.cursor = Rectangle( width=0.25, height=0.5, fill_opacity=1, color=red)
        self.numbers = [3, 1, 4, 2, 5]
        self.indexes = list(range(len(self.numbers)))
        self.box_group = VGroup()

        # -- header -- 
        header = Text("List methods part 2", **font_sans)
        logo = ImageMobject("logo.png")

        header.to_edge(UP_EDGE)
        logo.to_edge(DOWN_EDGE)
        logo.scale(.5)

        self.play(
            FadeIn(header, shift=DOWN),
            FadeIn(logo, shift=UP),
        )
        self.wait(1)


        # -- numbers --
        number_text = Text(f"numbers = {self.numbers}", **font_opt)
        number_text.next_to(header, DOWN, buff=1)
        number_text.to_edge(LEFT_EDGE)
        self.cursor.next_to(number_text, DOWN, buff=.5)
        self.cursor.to_edge(LEFT_EDGE)
        self.play(
                Write(number_text), 
                Blink(self.cursor, blinks=2),
        )
        self.wait(1)

        # -- boxes --
        self.box_group = VGroup()
        for index, number in enumerate(self.numbers):

            square_box = Square(side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0)
            index_text = Text(str(index), font="source code pro", font_size=20, color=GRAY)
            square_text = Text(str(number), **font_opt)
            index_text.move_to(square_box.get_top() - [0, -0.5, 0])

            box = VGroup(index_text, square_box, square_text)
            self.box_group.add(box)

        self.box_group.arrange(buff=0.5)

        for box in self.box_group:
            self.play(GrowFromCenter(box), run_time=0.35)

        # -- index method -- 
        t1 = MarkupText(f"numbers.<span foreground='{BLUE}'>index(4)</span>", **font_opt)
        t1.next_to(number_text, DOWN, buff=0.5)
        t1.to_edge(LEFT_EDGE)
        self.play(TypeWithCursor(t1, self.cursor))


        self.wait(3)



    
