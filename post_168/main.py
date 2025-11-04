from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

# Constants
CODE_FONT = "Source Code Pro"


# Python list slice
class MainScene(Scene):

    def write_text(self, text, nxt=None):
        text = Text(text, font=CODE_FONT, font_size=32)
        text.to_edge(UP, buff=0.25 * config.frame_height)
        if nxt:
            text.next_to(nxt, DOWN, buff=0.5)
        text.to_edge(LEFT * 0.25 * config.frame_width)
        # text.to_edge(LEFT)
        self.play(Write(text))
        return text

    def draw_squares(self):
        numbers = [5, 9, 3, 1, 7]
        squares_group = VGroup()
        # squares_group.to_edge(LEFT *.25 * config.frame_width)

        for index, number in enumerate(numbers, 1):
            square = Square(
                side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0
            )
            number_text = Text(str(number), font=CODE_FONT, font_size=36)
            box_group = VGroup(square, number_text)
            box_group.to_edge(LEFT, buff=(index * 1.45) / 10 * config.frame_width)
            squares_group.add(box_group)
            box_group.scale(0.1)
            self.play(box_group.animate.scale(10), run_time=0.5)
        return squares_group

    def pop_square(group, indeces):
        animations = []
        for i, box in enumerate(group):
            if i in range(*indeces):
                anim = group[index].animate.shift(UP * 0.5)
            else:
                anim = box.animate.set_fill(opacity=0.2).set_stroke(opacity=0.2)
            animations.append(anim)
        self.play(*animations)
        self.wait()

        # Reset: shift down previouse element that shifted up
        for index in indeces:
            self.play(squares_group[index].animate.shift(DOWN * 0.5))

    def transform_text(self, text_1, text_2):
        pass

    def construct(self):
        # header
        text_1 = self.write_text("numbers = [5, 9, 3, 1, 7]")
        self.wait()

        # square with number_text
        squares_group = self.draw_squares()
        self.wait()

        self.write_text("numbers[1]", text_1)
        self.wait()

        self.pop_square(squares_group, (1,))
        # # Action on boxes
        # index = 1
        # animations = []
        # for i, box in enumerate(squares_group):
        #     if i == index:
        #         anim = squares_group[index].animate.shift(UP * .5)
        #     else:
        #         anim = box.animate.set_fill(opacity=.2).set_stroke(opacity=.2)
        #     animations.append(anim)
        # self.play(*animations)
        # self.wait()
        #
        # # Reset: shift down previouse element that shifted up
        # anim = squares_group[index].animate.shift(DOWN*.5)
        # self.play(anim)
        # # -----------------------
        #
        #
        # # -----------------------
        # # Explain slice: numbers[4]
        # # ------------------------
        # # code
        # new_code_text = Text("numbers[4]", font=CODE_FONT, font_size=32)
        # new_code_text.to_edge(DOWN, buff=0.25 * config.frame_height)
        # new_code_text.to_edge(LEFT * .25 * config.frame_width)
        # self.play(Transform(code_text, new_code_text))
        # self.wait()
        #
        # # Action on boxes
        # index = 4
        # animations = []
        # for i, box in enumerate(squares_group):
        #     if i == index:
        #         anim = squares_group[index].set_fill(opacity=1).set_stroke(opacity=1).animate.shift(UP * .5)
        #     else:
        #         anim = box.animate.set_fill(opacity=.2).set_stroke(opacity=.2)
        #     animations.append(anim)
        # self.play(*animations)
        # self.wait()
        #
        # # Reset: shift down previouse element that shifted up
        # anim = squares_group[index].animate.shift(DOWN*.5)
        # self.play(anim)
        # # --------------------------
        #
        # # -----------------------
        # # Explain slice: numbers[0:4]
        # # ------------------------
        # # code
        # new_code_text = Text("numbers[0:3]", font=CODE_FONT, font_size=32)
        # new_code_text.to_edge(DOWN, buff=0.25 * config.frame_height)
        # new_code_text.to_edge(LEFT * .25 * config.frame_width)
        # self.play(Transform(code_text, new_code_text))
        # self.wait()
        #
        # # --- Action on boxes ----
        # indeces = (0, 3)
        # animations = []
        # for i, box in enumerate(squares_group):
        #     if i in range(*indeces):
        #         anim = squares_group[i].set_fill(opacity=1).set_stroke(opacity=1).animate.shift(UP * .5)
        #     else:
        #         anim = box.animate.set_fill(opacity=.2).set_stroke(opacity=.2)
        #     animations.append(anim)
        # print(animations)
        # self.play(*animations)
        # self.wait()
        #
        #
        #
        #
        #
