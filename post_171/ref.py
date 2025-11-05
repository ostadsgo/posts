from manim import * # type: ignore

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

# Constants
CODE_FONT = "Iosevka"
FONT_SIZE = 32
FONT = dict(font=CODE_FONT, font_size=FONT_SIZE)
TOP_EDGE = UP * 0.25 * config.frame_height
LEFT_EDGE = LEFT * 0.25 * config.frame_width


# Python list slice
class MainScene(Scene):

    def type_number_list(self):
        """ type text and move cursor to next text. """

        text = Text("numbers = [5, 9, 1, 4, 2]", **FONT)
        text.to_edge(TOP_EDGE)
        text.to_edge(LEFT_EDGE)
        self.cursor.move_to(text[0])
        
        self.play(TypeWithCursor(text, self.cursor))
        self.play(Blink(self.cursor, blinks=2))

        text2 = Text("print(numbers)", **FONT)
        text2.next_to(text, DOWN, aligned_edge=LEFT)
        
        # Move cursor to start of second line
        self.play(self.cursor.animate.move_to(text2[0]))
        
        self.play(TypeWithCursor(text2, self.cursor))
        self.play(Blink(self.cursor, blinks=2))
    def write_text(self, text):
        text = Text(text, font=CODE_FONT, font_size=32)
        text.to_edge(TOP_EDGE)
        text.to_edge(LEFT_EDGE)
        self.play(Write(text))
        return text

    def write_next_to(self, text, next_text, buff=0.5):
        text = Text(text, **FONT)
        text.next_to(next_text, DOWN, buff=buff)
        text.to_edge(LEFT_EDGE)
        self.play(Write(text))
        return text


    def transform_text(self, text, from_text):
        to_text = Text(text, **FONT)
        to_text.move_to(from_text.get_center())
        to_text.to_edge(LEFT_EDGE)
        self.play(ReplacementTransform(from_text, to_text))
        return to_text

    def type_text(self, text):
        text = Text(text, **FONT)
        cursor = Rectangle(
            color = "#984936",
            fill_color = "#984936",
            fill_opacity = 1.0,
            height = 0.47,
            width = 0.2,
        ).move_to(text[0]) # Position the cursor
        # self.play(AddTextLetterByLetter(text, time_per_char=.5))
        self.play(TypeWithCursor(text, cursor, time_per_char=.2))
        self.play(Blink(cursor, blinks=2))
        return text

    def backspace_text(self, text):
        text = Text(text, **FONT)
        self.play(RemoveTextLetterByLetter(text, time_per_char=.5))

    def backspace_with_cur(self, text):
        text = Text(text, color=PURPLE).scale(1.5).to_edge(LEFT)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0]) # Position the cursor

        self.play(UntypeWithCursor(text, cursor))
        self.play(Blink(cursor, blinks=2))


    def box(self, text):
        square_opt = dict(
            side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0
        )
        square = Square(**square_opt)
        text = Text(text, font=CODE_FONT, font_size=FONT_SIZE)
        box = VGroup(square, text)
        return box

    def boxes(self, items):
        g = VGroup()
        for item in self.items:
            box = self.box(str(item))
            g.add(box)
            box.scale(0.1)
        g.arrange(RIGHT, buff=1)
        g.to_edge(LEFT_EDGE)

        # Animate each box after arranging them in g
        for box in g:
            self.play(box.animate.scale(10), run_time=0.5)
    
    def boxes2(self, items):
        squares = [self.box(str(item)) for item in items]
        g = VGroup(*squares).arrange(buff=.5)

        # for box in g:
        #     self.play(GrowFromCenter(box))

        self.play(FadeIn(g))

        return g

    def pop_box(self, index):
        g = self.boxes2([7, 3, 9, 2, 3])
        g.save_state()
        self.play(g[index].animate.shift(UP * .5))
        return g
    
    def restor_group(self):
        g = self.pop_box(2)
        self.wait()
        self.play(Restore(g), run_time=2)


    def swap(self):
        self.wait()
        t = Text("hello world")
        t2 = Text("hi world")
        self.play(TransformFromCopy(t, t2))

    def circle(self):
        c = Circle(radius=1.0, color=BLUE)
        self.add(c)
        self.play(FadeIn(c))

    

    def progress(self):
        d1 = Dot(color=ORANGE)
        l1 = Line(LEFT, RIGHT, color=RED)
        l1.width = 5
        l1.height = 2
        l2 = VMobject() # filled line
        self.add(d1, l1, l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center(), color=BLUE)))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)

    def draw_squares(self):
        square_opt = dict(
            side_length=1.0, color=WHITE, fill_color=GREEN, fill_opacity=1.0
        )
        for item in self.items:
            square = Square(**square_opt)
            text = Text(str(item), font=CODE_FONT, font_size=FONT_SIZE)
            box = VGroup(square, text)
            self.squares.add(box)

        self.squares.arrange(RIGHT, buff=0.3)
        self.squares.to_edge(LEFT *.25 * config.frame_width)
        # self.play(FadeIn(self.squares))
        self.play(g.scale(2))

    def pop_square(self, group, indeces):
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
        self.items = [5, 9, 4, 1, 7]
        self.squares = VGroup()

        # header
        # t1 = self.write_text("numbers = [5, 9, 3, 1, 7]")
        # t2 = self.transform_text("hello world", t1)
        # t3 = self.write_next_to("goodbye", t2)
        # t4 = self.transform_text("something", t3)
        # self.square("1")
        # self.boxes(self.items)
        # print(help(AddTextLetterByLetter))
        # t = self.type_text("hello world")
        # self.backspace_text("hello world")
        # self.backspace_with_cur("hello world")
        # self.boxes2(self.items)
        # self.progress()
        # self.pop_box(2)
        # self.restor_group()
        # self.swap()
        self.circle()


        self.wait(10)

        # # square wtnumber_text
        # self.draw_squares()
        # self.wait()
        #
        # text_2 = self.write_text("len(numbers)", buff=0.30)
        # text_3 = self.write_text("5", buff=0.35)
        # self.wait()

        # text_3 = self.write_text("numbers[3]", 0.30, True, text_2)
        # self.reset_pop_square(self.squares, [1])
        # self.pop_square(self.squares, [3])
        # self.wait()
        #
        # text_4 = self.write_text("numbers[0:3]", 0.30, True, text_3)
        # self.reset_pop_square(self.squares, [3])
        # self.pop_square(self.squares, [0, 1, 2])
        # self.wait()
        #
        # text_4 = self.write_text("numbers[3:]", 0.30, True, text_4)
        # self.reset_pop_square(self.squares, [0, 1, 2])
        # self.pop_square(self.squares, [3, 4])
