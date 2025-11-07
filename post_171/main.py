from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

font_opt = dict(font="Source Code Pro", font_size = 32)
TOP_EDGE = UP * 0.25 * config.frame_height
LEFT_EDGE = LEFT * 0.25 * config.frame_width


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

        self.numbers = [5, 9, 1, 4, 2]
        self.box_group = VGroup()

        # ----------------------------
        #   Animation () - Blinks
        # ----------------------------
        self.cursor.to_edge(UP * 4)
        self.cursor.to_edge(LEFT * 2)
        self.play(Blink(self.cursor, blinks=3))

        # ---------------------------
        #   Type numbers
        # ----------------------------
        text1 = self.create_text("numbers = [5, 9, 1, 4, 2]", n=4)
        self.cursor.move_to(text1[0])
        self.play(TypeWithCursor(text1, self.cursor))

        # ---------------------------
        #   Animation () - squares
        # ----------------------------
        self.draw_boxes()
        for box in self.box_group:
            self.play(GrowFromCenter(box))
        
        # ---------------------------
        #   Animation () - max
        # ----------------------------
        text2 = self.create_text("max(numbers)", n=6)
        self.cursor.move_to(text2[0])
        self.play(TypeWithCursor(text2, self.cursor))
        
        # pop max item
        self.play(*self.box_shift([1]), *self.box_dim([0, 2, 3, 4]))
        
        # untype max
        self.cursor.move_to(text2[-1])
        self.play(UntypeWithCursor(text2, self.cursor))

        # Max shift down
        self.play(*self.box_shift([1], direction=DOWN))
        self.play(*self.box_undim())

        # ---------------------------
        #   Animation () - min
        # ----------------------------
        text3 = self.create_text("min(numbers)", n=6)
        self.cursor.move_to(text3[0])
        self.play(TypeWithCursor(text3, self.cursor))

        # pop min item
        self.play(*self.box_shift([2]), *self.box_dim([0, 1, 3, 4]))

        # Min shift down
        self.play(*self.box_shift([2], direction=DOWN))
        self.play(*self.box_undim())

        self.wait(3)



    def create_text(self, s, n):
        text = Text(s, **font_opt)
        # Positions
        text.to_edge(UP * n)
        text.to_edge(LEFT * 2)
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
