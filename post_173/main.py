from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

font_opt = dict(font="Source Code Pro", font_size=30)
UP_EDGE = UP * 0.25 * config.frame_height
LEFT_EDGE = LEFT * 0.25 * config.frame_width
DOWN_EDGE = DOWN * 0.25 * config.frame_height


class MainScene(Scene):
    def construct(self):

        # colors
        red = "#984936"
        gray = "#373737"
        blue = "#BAD7FF"

        self.cursor = Rectangle( width=0.25, height=0.5, fill_opacity=1, color=red)
        self.numbers = [5, 2, 9, 4, 6]
        self.indexes = list(range(len(self.numbers)))
        self.box_group = VGroup()

        # -- header -- 
        header = Text("List Methods")
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
        self.draw_boxes()
        for box in self.box_group:
            self.play(GrowFromCenter(box), run_time=.5)


        # -- pop -- 
        t0 = Text("numbers.", **font_opt)
        t1 = Text("pop()", color=BLUE, **font_opt)
        t0.next_to(number_text, DOWN, buff=.5)
        t0.to_edge(LEFT_EDGE)
        t1.next_to(t0, RIGHT, buff=.1)

        self.cursor.move_to(t0.get_left())
        self.play(TypeWithCursor(t0, self.cursor))
        self.cursor.move_to(t1.get_left())
        self.play(TypeWithCursor(t1, self.cursor), )
        self.wait(1)

        # remove box pop()
        self.play(FadeOut(self.box_group[-1]), number_text.animate.set_opacity(0.3))
        self.box_group.remove(self.box_group[-1])
        self.numbers.pop()
        self.wait(1)

        # -- pop(1) -- 
        self.remove(t1)
        t2 = Text("pop(1)", color=BLUE, **font_opt)
        t2.move_to(t1)
        self.play(TransformMatchingShapes(t1, t2))
        self.wait(1)

        # remove box pop(1)
        self.play(FadeOut(self.box_group[1]))
        self.box_group.remove(self.box_group[1])
        self.numbers.pop(1)
        self.wait(1)

        # reoreder boxes
        self.play(FadeOut(self.box_group), run_time=.5)
        self.draw_boxes()
        self.play(FadeIn(self.box_group), run_time=.2)
        self.wait(1)

        # -- append --
        self.remove(t1)
        self.remove(t2)
        t3 = Text("append(8)", color=BLUE, **font_opt)
        t3.next_to(t0, RIGHT, buff=-1.45)
        self.play(TransformMatchingShapes(t2, t3))
        self.wait(1)

        # append box
        sq_1 = Square(side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0)
        sq_1_text = Text("8", **font_opt)
        box_1 = VGroup(sq_1, sq_1_text)
        self.box_group.add(box_1)
        self.numbers.append(8)
        box_1.next_to(self.box_group, RIGHT, buff=0.3)
        self.play(FadeIn(box_1))
        self.wait(1)


        # -- insert ---
        self.remove(t3)
        t4 = Text("insert(0, 6)", color=BLUE, **font_opt)
        t4.next_to(t0, RIGHT, buff=-1.5)
        self.play(TransformMatchingShapes(t3, t4))
        self.wait(1)

        # insert box
        sq_2 = Square(side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0)
        sq_2_text = Text("6", **font_opt)
        box_2 = VGroup(sq_2, sq_2_text)
        self.box_group.add(box_2)
        self.numbers.insert(0, 6)
        box_2.next_to(self.box_group[0], LEFT, buff=0.3)
        self.play(FadeIn(box_2))
        self.wait(1)

        # -- remove ---
        self.remove(t4)
        t5 = Text("remove(9)", color=BLUE, **font_opt)
        t5.next_to(t0, RIGHT, buff=-1.45)
        self.play(TransformMatchingShapes(t4, t5))
        self.wait(1)

        # remove box with element 9
        self.play(FadeOut(self.box_group[1]))
        self.box_group.remove(self.box_group[1])
        self.numbers.remove(9)
        self.wait(1)

        # reoreder boxes
        self.play(FadeOut(self.box_group), run_time=.5)
        self.draw_boxes()
        self.play(FadeIn(self.box_group), run_time=.2)
        self.wait(3)



    
    # --- methods ---
    def draw_boxes(self):
        self.box_group = VGroup()
        for number in self.numbers:
            square = Square(
                side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0
            )
            square_text = Text(str(number), **font_opt)
            box = VGroup(square, square_text)
            self.box_group.add(box)

        # Position
        self.box_group.arrange(buff=0.3)
