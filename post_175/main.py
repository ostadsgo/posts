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

    def box_undim(self, indexes):
        anims = []
        for index in indexes:
            anims.append(
                self.box_group[index]
                .animate.set_fill(opacity=1.0)
                .set_stroke(opacity=1.0)
            )
        return anims

    def create_header_logo(self, text):
        header = Text(f"{text}")
        logo = ImageMobject("logo.png")

        header.to_edge(UP_EDGE)
        logo.to_edge(DOWN_EDGE)
        logo.scale(.5)


        return header, logo
    
    def create_text(self, text_part_1, text_part_2="", color=WHITE, pos_n=2.0):
        text = MarkupText(f'{text_part_1}<span foreground="{color}">{text_part_2}</span>', **font_opt)
        text.to_edge(LEFT_EDGE)
        text.to_edge(UP_EDGE * pos_n)
        return text



    def construct(self):
        self.cursor = Rectangle( width=0.25, height=0.5, fill_opacity=1, color=RED)
        self.box_group = VGroup()
        codes = ('s = "Joe,12,LA"', "s = ", '"Joe,12,LA"', "Joe,12,LA")
        code_split_text = ("r = s.", 'split(",")')
        
        self.cursor.to_edge(UP_EDGE * 2.0)
        self.cursor.to_edge(LEFT_EDGE)
        header, logo = self.create_header_logo("String split")
        self.play(
            FadeIn(header, shift=DOWN),
            FadeIn(logo, shift=UP),
            Blink(self.cursor, blinks=2)
        )

        # type s content
        t1 = self.create_text(codes[1], codes[2], GREEN, 2.0)
        self.cursor.move_to(t1[0])
        self.play(TypeWithCursor(t1, self.cursor))
        self.wait(1)

        # draw s in boxes
        self.draw_boxes(codes[3])
        self.play(FadeIn(self.box_group))
        self.wait(1)

        # split method
        t2 = self.create_text(code_split_text[0], code_split_text[1], BLUE, 2.5)
        self.cursor.move_to(t2[0])
        self.play(TypeWithCursor(t2, self.cursor))
        self.wait(1)


        # make `,` red and remove `,'
        boxes_to_remove = []
        for box in self.box_group:
            if box[1].text == ',':
                self.play(box[0].animate.set_color(RED).set_stroke(WHITE))
                boxes_to_remove.append(box)

        for box in self.box_group:
            if box[1].text == ',':
                self.play(FadeOut(box))

        for box in boxes_to_remove:
            self.box_group.remove(box)

        self.wait(1)

        
        t3 = Text("r[0]", **font_opt)
        t3.to_edge(LEFT_EDGE)
        t3.to_edge(UP_EDGE * 3.0)
        self.cursor.move_to(t3[-1])
        self.play(TypeWithCursor(t3, self.cursor))
        self.wait(1)

        # shift
        shift_anims = self.box_shift([0, 1, 2], direction=UP)
        dim_anims = self.box_dim([3, 4, 5, 6])
        self.play(*shift_anims, *dim_anims)
        self.wait(1)

        unshift_anims = self.box_shift([0, 1, 2], direction=DOWN)
        undim_anims = self.box_undim([3, 4, 5, 6])
        self.play(*unshift_anims, *undim_anims)
        self.wait(1)

        # transform
        t4 = self.create_text("r[-1", "]", WHITE, 3.0)
        self.cursor.move_to(t4[-1])
        self.play(ReplacementTransform(t3, t4))
        self.wait(1)

        shift_anims = self.box_shift([5, 6], direction=UP)
        dim_anims = self.box_dim([0, 1, 2, 3, 4])
        self.play(*shift_anims, *dim_anims)
        self.wait(1)

        unshift_anims = self.box_shift([5, 6], direction=DOWN)
        undim_anims = self.box_undim([0, 1, 2, 3, 4])
        self.play(*unshift_anims, *undim_anims)
        self.wait(1)

        self.remove(self.cursor)
        self.remove(t3)
        self.remove(t2)
        self.remove(header)
        self.cursor = Rectangle( width=0.25, height=0.5, fill_opacity=1, color=RED)
        self.cursor.next_to(t4, RIGHT)
        new_header, _ = self.create_header_logo("Unpacking")
        self.play(ReplacementTransform(header, new_header), Blink(self.cursor, blinks=1))
        self.wait(1)

        self.play(UntypeWithCursor(t4, self.cursor))
        self.cursor.move_to(t2[-1])
        self.cursor.to_edge(UP_EDGE * 2.5)
        self.play(UntypeWithCursor(t2, self.cursor))
        self.wait(1)

        t5 = MarkupText(f"name, age, city = s.<span foreground='{BLUE}'>split</span><span foreground='{WHITE}'>(</span><span foreground='{GREEN}'>','</span><span foreground='{WHITE}'>)</span>", **font_opt)
        t5.to_edge(LEFT_EDGE)
        t5.to_edge(UP_EDGE * 2.5)
        self.play(TypeWithCursor(t5, self.cursor))
        self.wait(1)

        t6 = self.create_text("name", pos_n=3.0)
        self.cursor.move_to(t6[0])
        self.play(TypeWithCursor(t6, self.cursor))
        self.wait(1)

        # shift
        shift_anims = self.box_shift([0, 1, 2], direction=UP)
        dim_anims = self.box_dim([3, 4, 5, 6])
        self.play(*shift_anims, *dim_anims)
        self.wait(1)

        unshift_anims = self.box_shift([0, 1, 2], direction=DOWN)
        undim_anims = self.box_undim([3, 4, 5, 6])
        self.play(*unshift_anims, *undim_anims)
        self.wait(1)

        self.cursor.move_to(t6[-1])
        self.play(UntypeWithCursor(t6, self.cursor))
        self.remove(t6)
        self.wait(1)

        t7 = self.create_text("age", pos_n=3.0)
        self.cursor.move_to(t7[0])
        self.play(TypeWithCursor(t7, self.cursor))
        self.wait(1)

        # shift
        shift_anims = self.box_shift([3, 4], direction=UP)
        dim_anims = self.box_dim([0, 1, 2, 5, 6])
        self.play(*shift_anims, *dim_anims)
        self.wait(1)

        unshift_anims = self.box_shift([3, 4], direction=DOWN)
        undim_anims = self.box_undim([0, 1, 2, 5, 6])
        self.play(*unshift_anims, *undim_anims)
        self.wait(1)
        









