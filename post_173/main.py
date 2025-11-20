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
        pop_group = VGroup(Text("numbers.", **font_opt), Text("pop()", color=BLUE, **font_opt))
        pop_group.arrange(RIGHT, buff=0.1)
        pop_group.next_to(number_text, DOWN, buff=.5)
        pop_group.to_edge(LEFT_EDGE)

        self.cursor.move_to(pop_group[0].get_left())
        self.play(TypeWithCursor(pop_group[0], self.cursor))
        self.cursor.move_to(pop_group[1].get_left())
        self.play(TypeWithCursor(pop_group[1], self.cursor))

        # remove box pop(1)
        self.play(FadeOut(self.box_group[-1]))
        self.box_group.remove(self.box_group[-1])
        self.numbers.pop()
        self.wait(1)







        # # remove last box
        # last_box = self.box_group[-1]
        # self.play(FadeOut(last_box))
        # self.box_group.remove(last_box)
        # self.numbers.pop()
        # self.wait(1)
        #
        #
        # # pop(1)
        # pop_1_text = Text("1)", **font_opt)
        # pop_1_text.to_edge(LEFT_EDGE)
        # pop_1_text.next_to(pop_text, RIGHT, buff=-0.2)
        # self.play(TypeWithCursor(pop_1_text, self.cursor))
        # self.wait(1)
        #
        # # remove box pop(1)
        # box_at_1 = self.box_group[1]
        # self.play(FadeOut(box_at_1))
        # self.box_group.remove(box_at_1)
        # self.numbers.pop(1)
        # self.wait(1)
        #
        # # rearrange boxes
        # self.play(FadeOut(self.box_group), run_time=.3)
        # self.draw_boxes()
        # self.play(FadeIn(self.box_group), run_time=.5)
        #
        # # -- append -- 
        #
        # # remove pop(1)
        # self.remove(pop_1_text)
        # self.cursor.move_to(pop_1_text[-1])
        # self.play(UntypeWithCursor(pop_text[9:], self.cursor))
        # self.wait(1)
        #
        # append_text = Text("append(8)", **font_opt)
        # append_text.next_to(number_text, DOWN, buff=.5) 
        # append_text.to_edge(LEFT_EDGE)
        # append_text.next_to(pop_text, RIGHT, buff=.2)
        # self.cursor.move_to(pop_text[0])
        # self.play(TypeWithCursor(append_text, self.cursor))
        # self.wait(1)





        

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
