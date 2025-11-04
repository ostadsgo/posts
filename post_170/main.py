from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

# Constants
CODE_FONT = "Source Code Pro"


# Python list slice
class MainScene(Scene):

    def write_text(self, text, buff=0.25, transform=False, from_text=""):
        text = Text(text, font=CODE_FONT, font_size=32)
        text.to_edge(UP, buff=buff * config.frame_height)
        text.to_edge(LEFT * 0.25 * config.frame_width)
        if transform:
            self.play(ReplacementTransform(from_text, text))
        else:
            self.play(Write(text))
        self.wait()
        return text

    def draw_squares(self):
        numbers = [5, 9, 4, 1, 7]
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

    def pop_square(self, group, indeces):
        print(indeces)
        animations = []
        # index or indeces
        for i, box in enumerate(group):
            if i in indeces:
                anim = (
                    group[i]
                    .set_fill(opacity=1)
                    .set_stroke(opacity=1)
                    .animate.shift(UP * 0.5)
                )
            else:
                anim = box.animate.set_fill(opacity=0.2).set_stroke(opacity=0.2)
            animations.append(anim)
        self.play(*animations)
        self.wait()

    def reset_pop_square(self, group, indeces):
        animations = []
        for i in indeces:
            animations.append(group[i].animate.shift(DOWN * 0.5))
        self.play(*animations)

    def construct(self):
        # header
        self.write_text("numbers = [5, 9, 3, 1, 7]")

        # square with number_text
        squares_group = self.draw_squares()
        self.wait()

        text_2 = self.write_text("numbers[1]", buff=0.30)
        self.pop_square(squares_group, [1])
        self.wait()

        text_3 = self.write_text("numbers[3]", 0.30, True, text_2)
        self.reset_pop_square(squares_group, [1])
        self.pop_square(squares_group, [3])
        self.wait()

        text_4 = self.write_text("numbers[0:3]", 0.30, True, text_3)
        self.reset_pop_square(squares_group, [3])
        self.pop_square(squares_group, [0, 1, 2])
        self.wait()

        text_4 = self.write_text("numbers[3:]", 0.30, True, text_4)
        self.reset_pop_square(squares_group, [0, 1, 2])
        self.pop_square(squares_group, [3, 4])
