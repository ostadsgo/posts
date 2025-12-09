from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

font_opt = dict(font="Source Code Pro", font_size=26)
font_sans = dict(font="Noto Sans", font_size=40, weight=BOLD)
UP_EDGE = UP * 0.25 * config.frame_height
LEFT_EDGE = LEFT * 0.25 * config.frame_width
DOWN_EDGE = DOWN * 0.25 * config.frame_height

MY_RED = "#984936"
MY_GREEN = "#B4F6C0"


class MainScene(Scene):
    def draw_boxes(self, items):
        for item in items:
            square = Square(
                side_length=0.6, color=WHITE, fill_color=GREEN, fill_opacity=1.0
            )
            square_text = Text(str(item), **font_opt)
            box = VGroup(square, square_text)
            self.box_group.add(box)

        # Position
        self.box_group.arrange(buff=0.1)

    def box_shift(self, indexes, direction=UP):
        anims = []
        for index in indexes:
            anims.append(self.box_group[index].animate.shift(direction * 0.5))
        return anims

    def box_dim(self, indexes):
        anims = []
        for index in indexes:
            anims.append(
                self.box_group[index]
                .animate.set_fill(opacity=0.2)
                .set_stroke(opacity=0.2)
            )
        return anims

    def box_undim(self):
        anims = []
        for index in range(len(self.numbers)):
            anims.append(
                self.box_group[index]
                .animate.set_fill(opacity=1.0)
                .set_stroke(opacity=1.0)
            )
        return anims

    def play_header(self):
        # -- header -- 
        header = Text("str.split", **font_sans)
        logo = ImageMobject("logo.png")

        header.to_edge(UP_EDGE)
        logo.to_edge(DOWN_EDGE)
        logo.scale(.5)

        self.play(
            FadeIn(header, shift=DOWN),
            FadeIn(logo, shift=UP),
        )
    
    def type_text(self, text_part_1, text_part_2, color, pos_n):
        text = MarkupText(f'text_part_1<span foreground="{color}">"{text_part_2}"</span>', **font_opt)
        text.to_edge(LEFT_EDGE)
        text.to_edge(UP_EDGE * pos_n)
        return text


    def play_init_text(self, s):
        text = MarkupText(f's = <span foreground="{MY_GREEN}">"{s}"</span>', **font_opt)
        text.to_edge(LEFT_EDGE)
        text.to_edge(UP_EDGE * 2.0)
        return text



    def construct(self):
        self.cursor = Rectangle( width=0.25, height=0.5, fill_opacity=1, color=red)
        self.box_group = VGroup()
        

        # colors

        self.play_header()
        self.wait(1)

        s = "Joe,12,LA"
        self.cursor.next_to(number_text, DOWN, buff=.5)
        self.play_init_text(s)

        self.draw_boxes(s)
        self.play(FadeIn(self.box_group))


        # play_first_example
        text = MarkupText(f's.<span foreground="{BLUE}">split(",")</span>', **font_opt)
        self.wait(1)


