from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

font_opt = dict(font="Source Code Pro", font_size = 30)
UP_EDGE = UP * 0.20 * config.frame_height
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

        self.numbers = [5, 2, 9, 4, 6]
        self.indexes = list(range(len(self.numbers)))
        self.box_group = VGroup() 

        # ----------------------------
        #   First andimation header, img, cursor
        # ----------------------------

        header = Text("max / min / filter")
        logo = ImageMobject("g17.png")

        # position
        header.to_edge(UP_EDGE)
        logo.to_edge(DOWN_EDGE)
        logo.scale(0.5)
        self.cursor.to_edge(UP_EDGE * 2)
        self.cursor.to_edge(LEFT_EDGE)

        # animation
        self.play(
            Blink(self.cursor, blinks=2),
            FadeIn(header, shift=DOWN),
            FadeIn(logo, shift=UP),
            run_time=2,
            rate_func=smooth
        )

        # ---------------------------
        #   Type numbers
        # ----------------------------
        text1 = self.create_text(f"numbers = {self.numbers}", n=2)
        self.cursor.move_to(text1[0])
        self.play(TypeWithCursor(text1, self.cursor))
        self.wait(1)
        
        # ---------------------------
        #   Squares
        # ----------------------------
        self.draw_boxes()
        for box in self.box_group:
            self.play(GrowFromCenter(box), run_time=.5)

        self.wait(1)

        # ---------------------------
        #   Max
        # ----------------------------
        text2 = self.create_text("max(numbers)", n=2.5)
        self.cursor.move_to(text2[0])
        self.play(TypeWithCursor(text2, self.cursor))
        self.wait(1)

        # pop max item

        elements = [max(self.numbers)]
        pop_indexes = [index for index, element in enumerate(self.numbers) if element in elements]
        dim_indexes = [index for index, element in enumerate(self.numbers) if element not in elements]
        self.play(*self.box_shift(pop_indexes), *self.box_dim(dim_indexes))
        self.wait(1)


        # untype max
        self.cursor.move_to(text2[-1])
        self.wait(1)

        # Max shift down
        self.play(UntypeWithCursor(text2, self.cursor), *self.box_shift(pop_indexes, direction=DOWN))
        self.play(*self.box_undim())
        self.play(Blink(self.cursor, Blinks=1))

        # ---------------------------
        #    Min
        # ----------------------------
        text3 = self.create_text("min(numbers)", n=2.5)
        self.cursor.move_to(text3[self.numbers.index(min(self.numbers))])
        self.play(TypeWithCursor(text3, self.cursor))
        self.wait(1)
        #
        # pop min item
        elements = [min(self.numbers)]
        pop_indexes = [index for index, element in enumerate(self.numbers) if element in elements]
        dim_indexes = [index for index, element in enumerate(self.numbers) if element not in elements]
        self.play(*self.box_shift(pop_indexes), *self.box_dim(dim_indexes))
        self.wait(1)

        # untype max
        self.cursor.move_to(text2[-1])
        self.wait(1)

        # Min shift down
        self.play(UntypeWithCursor(text3, self.cursor), *self.box_shift(pop_indexes, direction=DOWN))
        self.play(*self.box_undim())
        self.play(Blink(self.cursor, blinks=1))

        # ---------------------------
        #    Map
        # ----------------------------
        # type the text
        text3 = self.create_text("filter(lambda n: n > 5, numbers)", n=2.5)
        self.cursor.move_to(text3[self.numbers.index(min(self.numbers))])
        self.play(TypeWithCursor(text3, self.cursor))
        self.wait(1)

        # pop min item
        dim_indexes = self.indexes.copy()
        elements = list(filter(lambda n: n > 5, self.numbers))
        pop_indexes = [index for index, element in enumerate(self.numbers) if element in elements]
        dim_indexes = [index for index, element in enumerate(self.numbers) if element not in elements]
        self.play(*self.box_shift(pop_indexes), *self.box_dim(dim_indexes))
        self.wait(1)

        # untype max
        self.cursor.move_to(text2[-1])
        self.wait(1)

        # Min shift down
        self.play(UntypeWithCursor(text3, self.cursor), *self.box_shift(pop_indexes, direction=DOWN))
        self.play(*self.box_undim())
        self.play(Blink(self.cursor, blinks=1))


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
