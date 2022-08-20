from manim import *

config.background_color = WHITE

class HarmonicPotential(Scene):

    def construct(self):
        axes = Axes(
            x_range=[-5,5],
            y_range=[-1, 6, 1],
            x_length=5,
            axis_config={"color": GREEN},
         
            tips=False,
        )

        axes_labels = axes.get_axis_labels()
        harmonic_graph = axes.plot(lambda x: self.harmonic_potential(x), color=BLUE)

        harmonic_label = MathTex("V(x) = \\frac{1}{2} m \\omega^{2} x^{2}", color=BLUE).next_to(harmonic_graph, RIGHT * 3)

        gs_plot = axes.plot(lambda x: self.ground_state_HO_wavefunction(x), color=YELLOW)
        ex_1 = axes.plot(lambda x: self.excited_state_1(x), color=RED)
        ex_2 = axes.plot(lambda x: self.excited_state_2(x), color=PURPLE)
        ex_3 = axes.plot(lambda x: self.excited_state_3(x), color=ORANGE)

        x = axes.coords_to_point(1.25, self.harmonic_potential(1.25))
        y = axes.coords_to_point((-1.25), self.harmonic_potential(1.25))
        dashed_1 = DashedLine(x,y, dash_length=0.1, color=YELLOW)


        x1 = axes.coords_to_point(2.66, self.harmonic_potential(2.66))
        y1 = axes.coords_to_point((-2.66), self.harmonic_potential(2.66))
        dashed_2 = DashedLine(x1,y1, dash_length=0.1, color=RED)

        x2 = axes.coords_to_point(3.53, self.harmonic_potential(3.53))
        y2 = axes.coords_to_point((-3.53), self.harmonic_potential(3.53))
        dashed_3 = DashedLine(x2,y2, dash_length=0.1, color=PURPLE)

        x3 = axes.coords_to_point(4.25, self.harmonic_potential(4.25))
        y3 = axes.coords_to_point((-4.25), self.harmonic_potential(4.25))
        dashed_4 = DashedLine(x3,y3, dash_length=0.1, color=ORANGE)
        
        plot = VGroup(axes, harmonic_graph)
        labels = VGroup(axes_labels)

        self.wait(0.5)
        self.play(Create(axes))
        self.play(Create(harmonic_graph), Write(harmonic_label), run_time=4)
        
        self.wait(1)
        
        self.play(Create(dashed_1), Create(dashed_2), Create(dashed_3), Create(dashed_4))
        self.play(Create(gs_plot))

        self.play(Create(ex_1))
        self.play(Create(ex_2))
        self.play(Create(ex_3))

        self.wait(3)
    
    def harmonic_potential(self, x):
        return 0.25*x**2
    
    
    def ground_state_HO_wavefunction(self,x):
        return  ((1/(np.pi))**(1/4)) * np.exp((-1*x**2)/(2))

    def excited_state_1(self,x):
        return 1.75 + ((4/(np.pi))**(1/4)) * x * np.exp((-1*x**2)/(2))   

    def excited_state_2(self,x):
        return 3.15 + ((1/(4*np.pi))**(1/4)) * (2*x**2 - 1) * np.exp((-1*x**2)/(2))    

    def excited_state_3(self,x):
        return 4.5 + ((1/(9*np.pi))**(1/4)) * (2*x**3 - 3*x) * np.exp((-1*x**2)/(2))   