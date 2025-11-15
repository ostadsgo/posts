from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

font_opt = dict(font="Source Code Pro", font_size = 30)
UP_EDGE = UP * 0.15 * config.frame_height
LEFT_EDGE = LEFT * 0.20 * config.frame_width
DOWN_EDGE = DOWN * 0.20 * config.frame_height


class MainScene(Scene):
    def construct(self):
        # ---------------------------
        #   GLOBALS
        # ---------------------------
        self.cursor = Rectangle(
            width=0.25,
            height=0.5,
            fill_opacity=1,
            color="#984936",
        )

        self.numbers = [10]
        self.indexes = list(range(len(self.numbers)))
        self.box_group = VGroup() 

        # --------------------------------------------
        #   First andimation header, img, cursor
        # --------------------------------------------
        header = Text("Variables", font="Noto Sans")
        logo = ImageMobject("logo.png")

        # position
        header.to_edge(UP_EDGE)
        logo.to_edge(DOWN_EDGE)
        logo.scale(0.5)
        self.cursor.to_edge(UP_EDGE * 2)
        self.cursor.to_edge(LEFT_EDGE)

        # animation
        self.play(
            Blink(self.cursor, blinks=3),
            FadeIn(header, shift=DOWN),
            FadeIn(logo, shift=UP),
            run_time=2,
            rate_func=smooth
        )

        # ---------------------------
        #   Type variable
        # ----------------------------
        text1 = self.create_text(f"a = 10", n=2.0)
        self.cursor.move_to(text1[0])
        self.play(TypeWithCursor(text1, self.cursor))
        self.wait(1)

        # -- Squares --
        square = Square( side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0)
        square_text = Text("10", **font_opt)
        box1 = VGroup(square, square_text)
        box1.to_edge(LEFT_EDGE)
        box1.to_edge(UP*18)
        self.play(GrowFromCenter(box1), run_time=1.0)
        self.wait(1)

        arrow_a = Arrow(start=UP, end=DOWN, color=GOLD)
        arrow_a.next_to(box1, direction=UP)
        a = Text("a")
        a.next_to(arrow_a, direction=UP)
        self.play(Create(arrow_a), FadeIn(a))
        self.wait(1)

        # ---------------------------
        #   Type variable
        # ----------------------------
        text2 = self.create_text("b = 20", n=2.5)
        self.cursor.move_to(text2[0])
        self.play(TypeWithCursor(text2, self.cursor))
        self.wait(1)

        # -- square -- 
        square = Square( side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0)
        square_text = Text("20", **font_opt)
        box2 = VGroup(square, square_text)
        box2.next_to(box1)
        box2.to_edge(UP*18)
        self.play(GrowFromCenter(box2), run_time=1.0)
        self.wait(1)

        arrow_b = Arrow(start=UP, end=DOWN, color=GOLD)
        arrow_b.next_to(box2, direction=UP)
        b = Text("b")
        b.next_to(arrow_b, direction=UP)
        self.play(Create(arrow_b), FadeIn(b))
        self.wait(1)

        # --------------
        #   Transform b
        # --------------
        text3 = self.create_text("b = 10", n=2.5)
        self.play(ReplacementTransform(text2, text3))
        self.wait(1)

        # -- move arrow to box a  (box1) diagnoly
        self.play(GrowArrow(arrow_b.shift(LEFT * 0.5).rotate(-25 * DEGREES).scale(1.2)))

        self.wait(1)

        # -- remove box2 (b)
        self.play(FadeOut(box2))
        self.wait(1)
        

        # --------------
        #   Transform b to a
        # --------------
        text4 = self.create_text("b = a ", n=2.5)
        self.play(ReplacementTransform(text3, text4), ReplacementTransform(text2, text4))
        self.wait(1)

        self.play(GrowArrow(arrow_b))
        self.wait(1)

        # --------------
        #   Swap
        # --------------
        header_new = Text("Swap tow variables", font="Noto Sans")
        header_new.to_edge(UP_EDGE)

        text5 = self.create_text("b = 20 ", n=2.5)
        self.play(ReplacementTransform(text3, text5), ReplacementTransform(text2, text5), ReplacementTransform(text4, text5))
        self.wait(1)

        square = Square( side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0)
        square_text = Text("20", **font_opt)
        box2 = VGroup(square, square_text)
        box2.next_to(box1)
        box2.to_edge(UP*18)
        self.play(GrowFromCenter(box2), run_time=1.0)
        self.wait(1)

        self.play(GrowArrow(arrow_b.shift(LEFT * -0.5).rotate(25 * DEGREES).scale(0.8)))

        # -- variable c --
        self.play(ReplacementTransform(header, header_new))
        self.wait(1)

        text6 = self.create_text("c = b ", n=3.0)
        self.play(Write(text6))

        # -- arrow --
        arrow_c = Arrow(start=UP, end=DOWN, color=GOLD)
        c = Text("c")
        c.next_to(arrow_c, direction=UP)
        self.play(GrowArrow(arrow_c.shift(LEFT * .65).rotate(-35 * DEGREES).scale(1.3)), FadeIn(c))
        self.wait(1)

        # -- 
        text7 = self.create_text("b = a", n=3.5)
        self.play(Write(text7))
        self.wait(1)

        self.play(GrowArrow(arrow_b.shift(LEFT * 0.5).rotate(-35 * DEGREES).scale(1.5)))
        self.wait(1)
        
        # -- a = c --
        text7 = self.create_text("a = c", n=4.0)
        self.play(Write(text7))
        self.wait(1)
        self.play(GrowArrow(arrow_a.shift(RIGHT * 0.5).rotate(35 * DEGREES).scale(1.5)))
        self.wait(1)

        # --- remove c arrow and text ---
        text8 = self.create_text("del(c)", n=4.5)
        self.play(Write(text8))

        self.play(FadeOut(arrow_c), FadeOut(c))
        self.wait(3)




    def create_text(self, s, n):
        text = Text(s, **font_opt)
        # Positions
        text.to_edge(UP_EDGE * n)
        text.to_edge(LEFT_EDGE)
        return text

    def draw_boxes(self):
        for number in self.numbers:
            square = Square(
                side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0
            )
            square_text = Text(str(number), **font_opt)
            box = VGroup(square, square_text)
            self.box_group.add(box)

        # Position
        self.box_group.arrange(buff=0.3)


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
