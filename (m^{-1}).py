from manim import *
from manim import MathTex


class RotateSquare(Scene):
    def construct(self):  
        
        

        square = Square(side_length=4, color=GRAY, fill_opacity=0.6)
        label_bottom_left = MathTex("\\texttt{1}").next_to(square.get_vertices()[0], DOWN+LEFT)
        label_bottom_right = MathTex("\\texttt{2}").next_to(square.get_vertices()[1], DOWN+RIGHT)
        label_top_right = MathTex("\\texttt{3}").next_to(square.get_vertices()[2], UP+RIGHT)
        label_top_left = MathTex("\\texttt{4}").next_to(square.get_vertices()[3], UP+LEFT)
        
        
        
        
        intro_words = Text("""
                    This video will illustrate the Actions
                    of the Dihedral group on a Square
        """)
        intro_words.to_edge(UP)
        
        intro = Text("""
                    Miko: hye!!
        """)
        intro.to_edge(DOWN)

        self.play(AddTextLetterByLetter(intro_words),run_time=3)
        self.wait(2)
        self.play(AddTextLetterByLetter(intro),run_time=3)
        self.wait(2)
        self.play(RemoveTextLetterByLetter(intro_words),run_time=1.5)
        self.play(RemoveTextLetterByLetter(intro),run_time=1.5)

        # Grid Creating
        grid = NumberPlane((-10, 10), (-5, 5))
        self.play(GrowFromCenter(grid),run_time=3)
        self.wait(2)
        
        

        

        # Add the square to the scene
        
        
        
        
        # Rotate the square by 90 degrees
        First = Text(""" 
                    The Action of Doing Nothing "I"      
                    """)
        
        First.to_edge(UP)
        
        self.play(AddTextLetterByLetter(First), target_position=UP,run_time=3.5)
        self.play(Create(square))
        self.play(FadeIn(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        self.play(ApplyMethod(square.scale, np.array([-1,-1, -1])))
        #self.play(RemoveTextLetterByLetter(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        #self.play(FadeOut(square),run_time=2)
        self.play(RemoveTextLetterByLetter(First), target_position=UP,run_time=2)
        self.wait(2)
        
        
        # Rotate the square by 90 degrees
        First = Text("""  
                            The Action of Rotating 
                                by 90 degree R      
                    """)
        First.to_edge(UP)
        
        
        self.play(AddTextLetterByLetter(First), target_position=UP,run_time=3.5)
        #self.play(Create(square))
        #self.play(AddTextLetterByLetter(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        self.play(ApplyMethod(square.rotate, 90* DEGREES),run_time=3)
        #self.play(RemoveTextLetterByLetter(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        #self.play(FadeOut(square),run_time=2)
        self.play(RemoveTextLetterByLetter(First), target_position=UP,run_time=2)
        self.wait(2)
        
        
        # Rotate the square by 180 degrees
        # Add the square to the scene
        
        
        First = Text("""
                        The Action of Rotating
                            by 180 degree R 
                    """)
        First.to_edge(UP)
        
        self.play(AddTextLetterByLetter(First), target_position=UP,run_time=3.5)
        #self.play(Create(square))
        #self.play(AddTextLetterByLetter(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        self.play(ApplyMethod(square.rotate, 90* DEGREES),run_time=3)
        #self.play(RemoveTextLetterByLetter(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        #self.play(FadeOut(square),run_time=2)
        self.play(RemoveTextLetterByLetter(First), target_position=UP,run_time=2)
        self.wait(2)
        
        
        
        self.play(FadeIn(label_bottom_left, label_bottom_right, label_top_right, label_top_left))
        self.wait(1)
        
        First = Text("""    The Action of Rotating
                            by 270 or -90 degree R2 
                    """)
        First.to_edge(UP)
        
        
        self.play(AddTextLetterByLetter(First), target_position=UP,run_time=3.5)
        #self.play(Create(square))
        #self.play(AddTextLetterByLetter(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        self.play(RemoveTextLetterByLetter(First), target_position=UP,run_time=2)
        self.play(ApplyMethod(square.rotate, 90* DEGREES),run_time=3)
        self.play(FadeOut(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        self.play(FadeOut(square),run_time=2)
        
        self.wait(2)
        
        
        
        
        
        
        #self.play(DrawBorderThenFill(square))
        #self.play(FadeIn(label_bottom_left, label_bottom_right, label_top_right, label_top_left))
        self.wait(3)
        
        First = Text(""" 
                            The Action of Reflection about
                                the Horizontal Axes H
                    """)
        First.to_edge(UP)
        # Reflect the square about its diagonal axis
        
        self.play(AddTextLetterByLetter(First), target_position=UP,run_time=3.5)
        self.play(Create(square))
        self.play(FadeIn(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        reflection_axes = (DOWN + LEFT) / np.sqrt(2)
        self.play(ApplyMethod(square.scale, np.array([1, -1, 1])),)
        self.play(RemoveTextLetterByLetter(First), target_position=UP,run_time=2)
        self.play(FadeOut(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        self.play(Uncreate(square),run_time=2)
        
        self.wait(2)
        
        
        
        
        
        
        
        #self.play(FadeIn(label_bottom_left, label_bottom_right, label_top_right, label_top_left))
        self.wait(3)
        
        First = Text(""" 
                    The Action of Reflection
                    about the Vertical Axes V 
                    """)
        First.to_edge(UP)
        
        # Reflect the square about its diagonal axis
        self.play(AddTextLetterByLetter(First), target_position=UP,run_time=3.5)
        self.play(Create(square))
        self.play(FadeIn(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        self.play(ApplyMethod(square.scale, np.array([-1, 1, -1])),run_time=3)
        self.play(RemoveTextLetterByLetter(First), target_position=UP,run_time=2)
        self.play(FadeOut(label_bottom_left, label_bottom_right, label_top_right, label_top_left),run_time=2)
        self.play(FadeOut(square),run_time=2)
        
        self.wait(2)
        
        
        intro_words = Text("""
                    There are also the reflection
                    about the diagonal
                            """)
        intro_words.to_edge(UP)
        
        
        
        self.play(FadeOut(grid),run_time=3)

        self.play(Create(intro_words),run_time=4)
        self.wait(3)
        self.play(FadeOut(intro_words),run_time=1.5)
        
        intro = Text("""
                        Thanks
                            """,font_size=50)
        
        self.play(GrowFromCenter(intro),run_time=3)
