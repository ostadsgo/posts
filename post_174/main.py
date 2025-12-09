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

        self.box_group.arrange(buff=0.3)

        for box in self.box_group:
            self.play(FadeIn(box, shift=RIGHT), run_time=0.5)

        self.wait(1)

        # -- index method -- 
        t1 = MarkupText(f"numbers.<span foreground='{BLUE}'>index(4)</span>", **font_opt)
        t1.next_to(number_text, DOWN, buff=0.5)
        t1.to_edge(LEFT_EDGE)
        self.play(TypeWithCursor(t1, self.cursor))
        self.wait(1)

        # shift the index with element 4
        index = self.numbers.index(4)
        dim_anim = [
            box.animate.set_fill(opacity=0.25)
            .set_stroke(opacity=0.25) 
            for i, box in enumerate(self.box_group) 
        ]
        self.play(*dim_anim)
        self.wait(1)

        index_text = self.box_group[index][0]
        index_text.set_color(WHITE).set_opacity(1.0)
        self.play(index_text.animate.scale(1.5))
        self.wait(2)

        # reset dim and everyting
        reset_anim = [
            box.animate.set_fill(opacity=1.0)
            .set_stroke(opacity=1.0)
            for i, box in enumerate(self.box_group) 
        ]
        index_text.set_color(GRAY)
        self.play(*reset_anim, index_text.animate.scale(1/1.5))
        self.wait(1)

        # show index for element 3
        self.remove(t1)
        t2 = MarkupText(f"numbers.<span foreground='{BLUE}'>index(3)</span>", **font_opt)
        t2.next_to(number_text, DOWN, buff=0.5)
        t2.to_edge(LEFT_EDGE)
        self.play(ReplacementTransform(t1, t2))

        index = self.numbers.index(3)
        dim_anim = [
            box.animate.set_fill(opacity=0.25)
            .set_stroke(opacity=0.25) 
            for i, box in enumerate(self.box_group) 
        ]
        self.play(*dim_anim)
        self.wait(1)

        index_text = self.box_group[index][0]
        index_text.set_color(WHITE).set_opacity(1.0)
        self.play(index_text.animate.scale(1.5))
        self.wait(2)

        # reset dim and everyting
        reset_anim = [
            box.animate.set_fill(opacity=1.0)
            .set_stroke(opacity=1.0)
            for i, box in enumerate(self.box_group) 
        ]
        index_text.set_color(GRAY)
        self.play(*reset_anim, index_text.animate.scale(1/1.5))
        self.wait(1)

        # -- sort -- 
        self.remove(t1)
        self.remove(t2)
        t3 = MarkupText(f"numbers.<span foreground='{BLUE}'>sort()</span>", **font_opt)
        t3.next_to(number_text, DOWN, buff=0.5)
        t3.to_edge(LEFT_EDGE)
        self.play(TransformMatchingShapes(t2, t3))
        self.wait(1)

        sorted_numbers = sorted(self.numbers)
        for box, n in zip(self.box_group, sorted_numbers):
            box_text = box[2]
            box_square = box[1]
            n = Text(str(n), **font_opt)
            n.move_to(box_text.get_center())
            self.play(
                box_square.animate.set_color(RED).set_stroke(WHITE),
                Transform(box_text, n)
            )

        self.wait(1)


        # -- reverse -
        self.remove(t1)
        self.remove(t2)
        self.remove(t3)
        t4 = MarkupText(f"numbers.<span foreground='{BLUE}'>reverse()</span>", **font_opt)
        t4.next_to(number_text, DOWN, buff=0.5)
        t4.to_edge(LEFT_EDGE)
        self.play(TransformMatchingShapes(t3, t4))
        self.wait(1)

        animations = []
        n = len(self.box_group)
        for i in range(n // 2):
            animations.append(CyclicReplace(
                self.box_group[i], 
                self.box_group[n - i - 1]
            ))


        
        i = 0
        index_anims = []
        for box in self.box_group:
            box_index = box[0]
            new_index = Text(str(i), font="source code pro", font_size=20, color=GRAY)
            new_index.move_to(box_index.get_center())
            index_anims.append(Transform(box_index, new_index))
            i += 1

        self.play(*animations, *index_anims)
        self.wait(3)
