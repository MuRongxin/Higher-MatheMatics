from manim import *
import numpy as np

from Anime import *

# 配置LaTeX支持中文
config.tex_template = TexTemplate(
    preamble=r"""
\usepackage{ctex}
\usepackage{amsmath,amssymb}
"""
)

_color_1="#39c5bb"  
_color_2="#C1003C"  
_color_3="#11999e"
_color_4=ManimColor("#ff2e63")
_color_5="#79D87E"
_color_6="#fff4e1"
_color_7="#ffaaa5"
_color_8="#b9d7ea"
_color_9="#7dace4"

font_1="得意黑"
font_2="文悦新青年体 (须授权)"


class TaylorSeries(Scene):
    def construct(self):
        title , titlepos=AnimeTools.AddTitle(self,title="泰勒公式")
        self.play(title)

        
        self.wait()

        axes1=Axes(
            x_range=[-3.35,3.35,PI/2],
            y_range=[-1.3,1.3,1],
            x_length=6,
            y_length=4,
            axis_config={
                "color":BLUE,
                "stroke_width":3,
                "include_tip":False,
                "include_ticks":True,
            },   
        ).shift(LEFT*3.3)

        func_sin=axes1.plot(
            lambda x:np.sin(x),
            x_range=[-3.4,3.4],
            stroke_width=5)

        sin_lable=MathTex(r"\sin(x)",font_size=28,stroke_width=1).next_to(func_sin,RIGHT)


        self.play(Succession(Create(axes1),Create(func_sin)),Write(sin_lable))
        
        text1=Text("在 x=0 处：",font=font_1,font_size=29,color=_color_4,
                   ).next_to(axes1,buff=.7).shift(UP*3)

        graph1=axes1.plot(lambda x:0,x_range=[-3.4,3.4],color=RED)
        self.wait()

        self.play(Write(text1))


        self.wait()

        step1=VGroup(
            VGroup(
                Text("零阶近似：模仿“位置”",font=font_1,font_size=27),
                MathTex(r"P_0(x) = c ",font_size=28,stroke_width=1)
            ).arrange(RIGHT),
            MathTex(r"P_0(x) = 0 \;(\sin(0)=0)",font_size=28,stroke_width=1)
        ).arrange(DOWN).next_to(text1,DOWN,aligned_edge=LEFT).shift(RIGHT*.2)
        
        step1[1].align_to(step1[0][0][5],LEFT)
        step1[0][0][0:5].set_color(_color_9)
        step1[1].set_color(YELLOW)
        step1[0][1].set_color(RED)
        self.play(Write(step1))
        self.play(Create(graph1))

        self.wait()

        graph2=axes1.plot(lambda x:x,x_range=[-1.3,1.3],color=YELLOW)

        stepText={
            "font_size":23,
            "font":font_1,           
        }

        stepMath={
            "font_size":28,
            "stroke_width":1,
        }

        step2=VGroup(
            VGroup(Text("一阶近似：",font=font_1,font_size=27),
                   Text("模仿“趋势” ",font=font_1,font_size=27),
                   MathTex(r"P_1(x) = c_0 + c_1x ",font_size=28,stroke_width=1)
            ).arrange(RIGHT),
            VGroup(
                VGroup(
                    Text("(a) 值相等：",font=font_1,font_size=23),
                    MathTex(r"\sin(0)=P_1(0)&=c_0+c_1\cdot 0 = 0 \\" ,
                            r"&\Rightarrow c_0=0 \\",
                            font_size=28,stroke_width=1),                    
                ).arrange(RIGHT,aligned_edge=UP),               
                
                Text("(b) 导数相等 (斜率相等):",font=font_1,font_size=23),

                VGroup(
                    VGroup(
                        MathTex(r"\sin'x=\cos x \Rightarrow",font_size=28,stroke_width=1),
                        Text("斜率是",**stepText),
                        MathTex(r"\cos(0) = 1",**stepMath)
                    ).arrange(RIGHT),
                    MathTex(r"P_1' (x) = c_1 =1 \Rightarrow  c_1 = 1",**stepMath),
                    MathTex(r"P_1(x) &= 0 + 1 \cdot x = x",**stepMath,color=YELLOW)
                ).arrange(DOWN,aligned_edge=LEFT)
               
            ).arrange(DOWN,aligned_edge=LEFT)

        ).arrange(DOWN).next_to(step1,DOWN,buff=.4,aligned_edge=LEFT)

        step2[0][0].set_color(_color_9)
        step2[0][2].set_color(RED)
        step2[1].align_to(step2[0][1],LEFT).shift(LEFT*.7)
        step2[1][2][2].shift(LEFT*.3+DOWN*.2)
        step2[1][2].shift(RIGHT*.3)

        self.play(Write(step2))

        self.wait()
        self.play(ReplacementTransform(graph1,graph2))

        self.wait(2)

        self.play(step1.animate.shift(UP*7),
                  step2.animate.shift(UP*7))

        step3_1 = Text(
            "二阶近似：模仿“弯曲”",
            font=font_1, font_size=27
        ).next_to(text1,DOWN,aligned_edge=LEFT).shift(RIGHT*.3)
        step3_2 = MathTex(
            r"P_2(x) = c_0+c_1 \cdot x+c_2 \cdot x^2 ",
            font_size=28,
            stroke_width=1,
            color=_color_9).next_to(step3_1[5],DOWN,aligned_edge=LEFT)

        step3_3 = Text(
            "(a) 值相等：",
            font=font_1,
            font_size=27
        ).next_to(step3_2,DOWN,aligned_edge=LEFT).shift(LEFT*.8)

        step3_4 = MathTex(
            r" P_2(0) = 0 \Rightarrow c_0 = 0",
            font_size=28,
            stroke_width=1
        ).next_to(step3_3,RIGHT)

        step3_5=Text(
            "(b) 一阶导相等：",
            font=font_1,
            font_size=27
        ).next_to(step3_3,DOWN,aligned_edge=LEFT)

        step3_6=MathTex(
            r" &P_2'(x) = c_1 + 2c_2x \\",
            r"\Rightarrow  &P_2'(0) = c_1 = 1 = \sin'(0) ",
            font_size=28,
            stroke_width=1
        ).next_to(step3_5,RIGHT,aligned_edge=UP)

        step3_7=Text(
            "(c) 二阶导相等 (弯曲程度相等)：",
            font=font_1,
            font_size=27
        ).next_to(step3_5,DOWN,aligned_edge=LEFT,buff=.7)

        step3_8=MathTex(
            r"&(\sin x)''=-\sin x \Rightarrow \sin''(0)=0 \\",
            r"&P_2''(x) = 2c_2 \Rightarrow  2c_2 = 0 \Rightarrow c_2 = 0",
            font_size=28,
            stroke_width=1
        ).next_to(step3_7[3],DOWN,aligned_edge=LEFT)

        step3_9=MathTex(
            r"P_2(x) = x",
            font_size=29,
            stroke_width=1,
            color=YELLOW
        ).next_to(step3_8,DOWN,buff=.5)

        step3=VGroup(
                step3_1,step3_2,step3_4,step3_3,
            step3_5,step3_6,step3_7,step3_8,step3_9
        )


        graph3=axes1.plot(lambda x:x,x_range=[-1.5,1.5],color=RED)

        self.play(
            LaggedStart(
                *[Write(mob) for mob in step3],
                lag_ratio=.3)
        )

        self.wait()

        self.play(ReplacementTransform(graph2,graph3))
        self.wait(2)

        self.play(step3.animate.shift(UP*7),)

        step4_1 = Text(
            "三阶近似 - 抓住“灵魂”",
            font=font_1,
            font_size=27,
            color=_color_9,
        ).next_to(text1,DOWN,aligned_edge=LEFT).shift(RIGHT*.3)

        step4_2=MathTex(
            r"P_3(x) = c_0 + c_1x + c_2x^2 + c_3x^3",
            font_size=28,
            stroke_width=1,
            color=_color_5
        ).next_to(step4_1[5],DOWN,aligned_edge=LEFT)

        step4_3=Paragraph(
            " (a) 值相等： c₀ = 0",
            "(b) 一阶导相等： c₁ = 1",
            "(c) 二阶导相等：",
            font=font_1,
            font_size=27,
            line_spacing=1,
            alignment="left"
        ).next_to(step4_1,DOWN,aligned_edge=LEFT,buff=.7).shift(RIGHT*.4)

        step4_4 = MathTex(
            r"&(\sin x)''=-\sin x \Rightarrow \sin''(0)=0 \\",
            r"&P_2''(x) = 2c_2 \Rightarrow  2c_2 = 0 \Rightarrow c_2 = 0",
            font_size=25,
            stroke_width=1,
            color=_color_6
        ).next_to(step4_3[2][3],DOWN,aligned_edge=LEFT)


        step4_5=Text(
            " (d) 三阶导相等：",
            font=font_1,
            font_size=27,
        ).next_to(step4_3,DOWN,aligned_edge=LEFT,buff=1.3)

        step4_6=MathTex(
            r"&\sin' x=\cos x \\",
            r"&\Rightarrow \cos'x=-\sin x \\",
            r"&\Rightarrow -sin'x=-\cos x \\",
            font_size=25,
            stroke_width=1
        ).next_to(step4_5,DOWN,aligned_edge=LEFT).shift(RIGHT*.3)

        step4_brace=Brace(step4_6,direction=RIGHT,sharpness=3,buff=.1,stroke_width=.1)

        step4_7=MathTex(
            " (sin x)''' = -cos x",
            font_size=25,
            stroke_width=1
        ).next_to(step4_brace,RIGHT,buff=.1)
        step4=VGroup(
            step4_1,step4_2,step4_3,step4_4,step4_5,step4_6,step4_brace,
            step4_7,
        )

        step4_8=MathTex(
            r"&(sin x)''' = -cos x \Rightarrow -\cos(0) = -1 \\",
            r"&P_3'''(x) = 6c_3 \Rightarrow  6c_3 = -1 \Rightarrow c_3 = -\frac{1}{6}",
            font_size=25,
            stroke_width=1
        ).next_to(step4_5[3],DOWN,aligned_edge=LEFT)

        self.play(LaggedStart(*[Write(mob) for mob in step4],lag_ratio=.3))

        self.wait(2)
        self.play(ReplacementTransform(VGroup(step4_6,step4_7,step4_brace),step4_8[0]))
        self.wait()
        step4_9=MathTex(
            "P_3'(x)=c_1+c_2x+3c_3x^2",
            font_size=25,
            stroke_width=1
        ).next_to(step4_8[0],DOWN,aligned_edge=LEFT)
        step4_10=MathTex(
            r"P_3''(x)=c_2+6c_3 \cdot x",
            font_size=25,
            stroke_width=1
        ).next_to(step4_8[0],DOWN,aligned_edge=LEFT)
        step4_11=MathTex(
            r"P_3'''(x)=6c_3",
            font_size=25,
            stroke_width=1
        ).next_to(step4_8[0],DOWN,aligned_edge=LEFT)

        self.play(Write(step4_9))
        self.wait()
        self.play(ReplacementTransform(step4_9,step4_10))
        self.wait()
        self.play(ReplacementTransform(step4_10,step4_11))

        self.wait()
        self.play(ReplacementTransform(step4_11,step4_8[1]))
        self.wait()

        step4_12=MathTex(
            r"P_3(x) = x - \frac{1}{6}x^3",
            font_size=27,
            stroke_width=1,
            color=YELLOW
        ).next_to(step4_8,DOWN)

        self.play(Write(step4_12))
        self.wait(2)
        step4.add(step4_10,step4_11,step4_12,step4_8)
        graph4=axes1.plot(
            lambda x: x-1/6*x**3,
            x_range=[-3,3],
            color=YELLOW,
        )

        self.play(ReplacementTransform(graph3,graph4))

        self.wait()


        fun_graph=VGroup(graph1,graph2,graph3,graph4,axes1,
                         sin_lable,func_sin)
        res2=VGroup(step2[0],step2[1][2][2]
                    ).arrange(DOWN,aligned_edge=RIGHT).shift(LEFT*3.8)

        res3=VGroup(
            step3_1.set_color(_color_9),step3_2.set_color(RED),step3_9
        ).arrange(DOWN,aligned_edge=LEFT).shift(UP*1.4+RIGHT*1.5)
        res3[2].next_to(res3[0],RIGHT)

        res4=VGroup(
            step4_1.copy(),step4_2.copy(),step4_12.copy()
        ).shift(LEFT*1+DOWN*2)
        res4[2].next_to(res4[0],RIGHT)
        res4[1].next_to(res4[0],DOWN,aligned_edge=LEFT)
        self.play(
            LaggedStart(
                FadeOut(fun_graph),
                step1.animate.to_corner(UL).shift(DOWN*1.2),
                Write(res2),
                Write(res3),
                Transform(step4,res4),
                lag_ratio=.3
            )
        )



















        

