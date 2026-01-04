from email.mime import text
from os import write
from tkinter import CENTER
from turtle import down, up
from manim import *
from networkx import center
import numpy as np

from Anime import *
# from concurrent.interpreters import create

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
_color_10=ManimColor("#779977")

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
        res4[1].next_to(res4[0],DOWN,aligned_edge=LEFT).set_color(RED)
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

        self.wait()

        res5=MathTex(
            r"\sin x \approx x-\frac{x^3}{6}",
            stroke_width=2,
            font_size=33,
        ).to_edge(DOWN,buff=1).shift(UP*1.3+LEFT*2.7)

        sinx_T=MathTex(
            r"\sin(x) ",
            r"&= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots",
            font_size=30,
            color=_color_1,
            stroke_width=1,            
        ).to_edge(DOWN,buff=1)



        self.play(
            LaggedStart(
                text1.animate.to_corner(DL).shift(UP*2+RIGHT),
                Write(res5),
                lag_ratio=.3
            )
        )

        self.wait()
        self.play(Write(sinx_T))
        emRec = AnimeTools.EmphasizeTexts(self,[sinx_T],color=_color_4,buff=.2)
        
        text2=Text(
            "（麦克劳林公式）",
            font=font_1,
            font_size=27,
            stroke_width=1
        ).next_to(emRec,RIGHT,aligned_edge=DOWN)

        self.play(Write(text2))
        
        self.wait(2)
        self.play(Uncreate(emRec),FadeOut(text2))
        self.play(
            LaggedStartMap(
                FadeOut,VGroup(step1,text1,res2,res3,res4,res5,sinx_T,step4),
                lag_ratio=.3
            )

        )

        self.wait(2)

        #======================Next page===============
        subTit1=Text(
            "带佩亚诺余项的泰勒公式（麦克劳林形式）：",
            font=font_1,
            font_size=27,            
            color=_color_4
        ).next_to(titlepos,DOWN,aligned_edge=LEFT)

        self.play(Write(subTit1))

        formulas1=MathTex(
            r"f(x)=f(0)+f'(0)\,x+\frac{f''(0)}{2!}\," ,
            r"x^{2}+\frac{f^{(3)}(0)}{3!}\,x^{3}+\cdots +" ,
            r"\frac{f^{(n)}(0)}{n!}\,x^{n}+" ,
            r"o\!\left(x^{n}\right),\quad x\to 0",
            font_size=30,
            stroke_width=1,            
        ).next_to(subTit1,DOWN,aligned_edge=LEFT)

        formulas1_rec=AnimeTools.EmphasizeTexts(self,[formulas1[3][0:5]],buff=.1)
        f1_rec_tex=MathTex(
            r"&\text{佩亚诺余项}\\",
            r"&\text{表示比 } x^n \text{ 高阶的无穷小}",
            font_size=25,
            stroke_width=1,
            color=_color_8
        ).next_to(formulas1_rec,UP,aligned_edge=LEFT)
        formulas_line1=Line(
            formulas1.get_corner(DL),
            formulas1.get_corner(DR),
            color=_color_1
        ).next_to(formulas1,DOWN)

        self.play(LaggedStart(Write(formulas1),Create(formulas_line1),lag_ratio=.3))
        self.play(Write(f1_rec_tex))
        self.wait(2)

        subTil2=Text(
            "常见函数的展开式（必须熟记）：",
            font=font_1,
            font_size=27,            
            color=_color_4
        ).next_to(formulas1,DOWN,aligned_edge=LEFT,buff=.1)

        self.wait()
        self.play(LaggedStart(Uncreate(formulas_line1),Write(subTil2),lag_ratio=.3))

        formulas2=MathTex(
            r"&\sin x=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}+o(x^5)",
            r"=(-1)^{n}\frac{x^{2n+1}}{(2n+1)!}+o(x^{2n+1}),\quad x\to 0 \\",
            r"&\cos x=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}+o\!\left(x^{5}\right)",
            r"=(-1)^{n}\frac{x^{2n}}{(2n)!}+o(x^{2n})\\",
            r"&\ln(1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+o\!\left(x^{4}\right)",
            r"=(-1)^{n-1}\frac{x^{n}}{n}+o(x^{n})\\",
            r"&\mathrm{e}^{x}=1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\frac{x^{4}}{4!}+o\!\left(x^{4}\right)",
            r"=\frac{x^{n}}{n!}+o\!\left(x^{n}\right)\\",
            r"&(1+x)^{\alpha}=1+\alpha x+\frac{\alpha(\alpha-1)}{2!}\,x^{2}+o\!\left(x^{2}\right)",
            font_size=30,
            stroke_width=1, 
        ).next_to(subTil2,DOWN,aligned_edge=LEFT)

        formulas2_add=MathTex(
            r"=\frac{\alpha(\alpha-1) \cdots (\alpha -n+1 )}{n!}\,x^{n}+o\!\left(x^{n}\right)",
            font_size=30,
            stroke_width=1, 
        ).next_to(formulas2[-1],RIGHT)

        self.play(Succession(LaggedStart(
                    [Write(obj) for obj in formulas2],
                    lag_ratio=.5), 
                    Write(formulas2_add))
        )

        self.wait(2)

        self.play(
            LaggedStart(
                FadeOut(formulas1_rec,f1_rec_tex,subTit1,subTil2,formulas1),
                FadeOut(formulas2_add),
                FadeOut(formulas2[-1]),
                formulas2.animate.next_to(
                    titlepos,DOWN,aligned_edge=LEFT,buff=.1),             
                lag_ratio=.4
            )
        )

        # self.play(FadeOut(formulas2[-1]))

        formulasLines=VGroup(
            Line(
                formulas2[0].get_corner(DL),
                formulas2[0].get_corner(DR),
                color=_color_4
            ).shift(DOWN*.1),
            Line(
                formulas2[2].get_corner(DL),
                formulas2[2].get_corner(DR),
                color=_color_4
            ).shift(DOWN*.1),
            Line(
                formulas2[4].get_corner(DL),
                formulas2[4].get_corner(DR),
                color=_color_4
            ).shift(DOWN*.1),
            Line(
                formulas2[6].get_corner(DL),
                formulas2[6].get_corner(DR),
                color=_color_4
            ).shift(DOWN*.1),
        )

        self.play(LaggedStartMap(Create,formulasLines))

        self.wait()

        formulas_rec1=SurroundingRectangle(formulas2[0],color=_color_4,buff=.1)
        formulas_rec2=SurroundingRectangle(formulas2[2],color=_color_4,buff=.1)
        formulas_rec3=SurroundingRectangle(formulas2[4],color=_color_4,buff=.1)
        formulas_rec4=SurroundingRectangle(formulas2[6],color=_color_4,buff=.1)

        formulasEmpa1=AnimationGroup(
            ReplacementTransform(formulasLines[0],formulas_rec1),
            ReplacementTransform(formulasLines[1],formulas_rec2),
            ReplacementTransform(formulasLines[2],formulas_rec3),
            ReplacementTransform(formulasLines[3],formulas_rec4),
            lag_ratio=.3
        )

        self.play(formulasEmpa1)
        self.wait()

        supplementrayTex1=Text(
            "展开到足以消除不确定性的最低阶数",
            font=font_1,
            font_size=27,
            color=_color_4
        ).next_to(formulasLines[-1],DOWN,aligned_edge=LEFT)

        self.play(Write(supplementrayTex1))

        supplementrayTex2=VGroup(
            VGroup(
                Text("1、分母的阶数决定基准： 若分母为",font=font_1,font_size=25),
                MathTex("x^k",stroke_width=1,font_size=28),
                Text("则分子应展开到",font=font_1,font_size=25),
                MathTex("x^k",stroke_width=1,font_size=28),
                Text("项。",font=font_1,font_size=25)
            ).arrange(RIGHT),
            Text(
                "2、加减法的抵消： 若表达式中存在相减，可能产生抵消，需要展开到第一个非零项之后的一阶。",
                font=font_1,font_size=25
            ),
            Text(
                "3、经验法则： 将每个函数展开到相同的阶数，通常比分母的阶数多一阶以确保安全。",
                font=font_1,font_size=25
            )
        ).arrange(DOWN,aligned_edge=LEFT).next_to(supplementrayTex1,DOWN,
                 aligned_edge=LEFT).shift(RIGHT*.2)

        supplementrayTex2[0].shift(RIGHT*.05)
        self.play(Write(supplementrayTex2))

        self.play(LaggedStartMap(
            FadeOut,
            VGroup(formulas_rec4,formulas_rec3,
             formulas_rec2,formulas_rec1,
             supplementrayTex1,supplementrayTex2,formulas2[:-1]),
            lag_ratio=.3)
        )
        

        #==================Next page======================
        exampleStyle={
            "font_size": 30,
            "stroke_width": 2,
            "color": _color_8
        }
        sloveStepStyle={
            "font_size": 28,
            "stroke_width": 1.2,
            "color": _color_6
        }
        sloveStyle={
            "font_size": 28,
            "stroke_width": 2,
        }
        exmaple1=MathTex(
            r"\text{示例： }",
            r"\lim_{x\to 0}\frac{\mathrm{e}^{x}-1-x}{x^{2}}",
            **exampleStyle
        ).next_to(titlepos,DOWN,aligned_edge=LEFT).shift(RIGHT*.1)

        self.play(Write(exmaple1))

        sloveStep1=MathTex(
            r"&\cdot \text{ 确认是 } \frac{0}{0} \text{ 型,且适合用泰勒公式。} \\",
            r"&\cdot \text{ 分母是 } x^2\text{，所以至少展开到2阶 } x^2 \\",
            r"&\cdot \text{ }\mathrm{e}^{x}=1+x+\frac{x^{2}}{2!}+o(x^{2}) \\",
            **sloveStepStyle
        ).next_to(exmaple1,DOWN,aligned_edge=LEFT).shift(RIGHT*.1)
        
        self.play(Write(sloveStep1))

        self.play(sloveStep1.animate.shift(RIGHT*7),
                  )

        self.wait()

        slove1=MathTex(
            r"&=\lim_{x \to 0}\frac{\left(1+x+\frac{x^{2}}{2}+o(x^{2})\right)-1-x}{x^2}\\",
            r"&=\lim_{x \to 0}\frac{\frac{x^2}{2}+o(x^2)}{x^2} \\",
            r"&=\lim_{x \to 0}(\frac{\frac{x^2}{2}}{x^2}+",
            r"\frac{o(x^2)}{x^2})\\",
            r"&=\lim_{x \to 0}(\frac{1}{2}+\frac{o(x^2)}{x^2})\\",
            r"&=\frac{1}{2}",
            **sloveStyle
        ).next_to(exmaple1[1],DOWN,aligned_edge=LEFT)

        self.play(LaggedStart(*[Write(slove) for slove in slove1],
                              lag_ratio=.5))

        self.wait(2)
        slove1_box=AnimeTools.EmphasizeTexts(self,[slove1[4][12:20]],buff=.1)

        slovel1_sep=MathTex(
            r"o(1)",
            font_size=28,
            stroke_width=2,
            color=_color_4,
        ).next_to(slove1_box,RIGHT)
        
        self.wait(1.5)
        self.play(Write(slovel1_sep))
        self.wait(1)
        
        self.play(FadeOut(slovel1_sep,slove1_box))
        slovel1_sep.move_to(slove1[4][12:20].get_center())
        self.play(Transform(slove1[4][12:20],slovel1_sep))

        self.wait(1.5)

        self.play(FadeOut(sloveStep1))

        example2=MathTex(
            r"\lim_{x\to 0}\frac{\sin x - x}{x^3}",
            **exampleStyle
        ).next_to(exmaple1,RIGHT).shift(RIGHT*5)

        self.play(Write(example2))

        sloveStep2=MathTex(
            r"&\text{分母是 }x^3\text{，所以至少展开到3阶 } x^3 \\",
            r"&\sin x=x-\frac{x^3}{3!}+o(x^3) \\",
            **sloveStepStyle
        ).next_to(example2,DOWN,aligned_edge=LEFT)

        self.play(Write(sloveStep2))
        self.wait(2.5)

        slove2=MathTex(
            r"&=\lim_{x \to 0}\frac{\left(x-\frac{x^3}{3!}+o(x^3)\right)-x}{x^3}\\",
            r"&=\lim_{x \to 0}\frac{-\frac{x^3}{3!}+o(x^3)}{x^3} \\",
            r"&=\lim_{x \to 0}\left(-\frac{1}{3!}+\frac{o(x^3)}{x^3}\right)\\",
            r"&=\lim_{x \to 0}\left(-\frac{1}{6}+o(1)\right)\\",
            r"&=-\frac{1}{6}",
            **sloveStyle
        ).next_to(example2,DOWN,aligned_edge=LEFT)

        self.play(ReplacementTransform(sloveStep2,slove2))

        self.wait(2)
        self.play(FadeOut(exmaple1,slove1,slovel1_sep,example2,slove2))
 
        #==================Next page======================

        example3=MathTex(
            r"\lim _{x\to0}\frac{\cos x-e^\frac{-x^2}{2}}{x^4} ",
            **exampleStyle
        ).next_to(titlepos,DOWN,aligned_edge=LEFT).shift(RIGHT*.1)

        self.play(Write(example3))

        sloveStep3=MathTex(
            r"&\cos x = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} + o(x^{4}) = 1 - \frac{x^{2}}{2} + \frac{x^{4}}{24} + o(x^{4})\\",
            r"&e^{\frac{-x^{2}}{2}}:\\" ,
            r"&\text{令 }u=-\frac{x^2}{2}\text{，则 }" ,
            r"e^u=1+u+\frac{u^{2}}{2!}+o(u^{2})\\"
            r"&e^{\frac{-x^{2}}{2}} = 1 + \left(-\frac{x^{2}}{2}\right) + \frac{1}{2!}\left(-\frac{x^{2}}{2}\right)^{2} + o(x^{4})",
            r"= 1 - \frac{x^{2}}{2} + \frac{x^{4}}{8} + o(x^{4})",
            **sloveStepStyle,
        ).next_to(example3,DOWN,aligned_edge=LEFT).shift(RIGHT*.3)
        
        sloveStep3_rec=SurroundingRectangle(sloveStep3,color=_color_4)

        self.play(Write(sloveStep3),Create(sloveStep3_rec))

        self.wait(2)

        solveS3_rec2=AnimeTools.EmphasizeTexts(self,[sloveStep3[1]],buff=.1)

        solveS3_arrow=Arrow(solveS3_rec2.get_right(),solveS3_rec2.get_right()+RIGHT,buff=.1,color=_color_4)
        solve3_tex=Text("复合函数",font=font_1,font_size=22,color=YELLOW
                        ).next_to(solveS3_arrow,RIGHT,buff=.1)
        self.play(Succession(Write(solveS3_arrow),Write(solve3_tex)))

        self.wait(2)

        sloveS3_rec3=AnimeTools.EmphasizeTexts(
            self,[sloveStep3[2][4:6]],color=RED,buff=.1)
        
        sloveS3_rec4=AnimeTools.EmphasizeTexts(
            self,[sloveStep3[3][15:17]],color=RED,buff=.1
        )

        self.wait(2)

        self.play(Succession(
            Uncreate(sloveS3_rec4),Uncreate(sloveS3_rec3),
            FadeOut(solve3_tex),Uncreate(solveS3_arrow),
            Uncreate(solveS3_rec2)
        ))
        sloveS3_rec=AnimeTools.EmphasizeTexts(self,[sloveStep3[-2][-4:-1]],buff=.2)

        sloveS3_sup=MathTex(
            r" o(\frac{1}{4}\,x^4)",
            r"\;[o(c\cdot g(x))=o(g(x))]",
            font_size=27,
            stroke_width=1,
            color=RED
        ).next_to(sloveS3_rec,DOWN,aligned_edge=LEFT)
        sloveS3_sup[1].set_color(BLUE)
        self.play(Write(sloveS3_sup))

        self.wait(2)
        
        self.play(
            Succession(
                FadeOut(sloveS3_sup),
                Uncreate(sloveS3_rec),
                VGroup(sloveStep3,sloveStep3_rec).animate.scale(.86).shift(DOWN*.5+RIGHT*5),
                
            )
        )
        temp_line=Line(sloveStep3.get_corner(UL),
                                sloveStep3.get_corner(DL),
                                color=_color_4,
                                stroke_width=8).shift(LEFT*.1)
        self.play(ReplacementTransform(sloveStep3_rec,
                           temp_line))

        slove3=MathTex(
            r"&= \lim_{x\to 0}\frac{\left(1 - \frac{x^{2}}{2} + \frac{x^{4}}{24}\right)" \
            r" - \left(1 - \frac{x^{2}}{2} + \frac{x^{4}}{8}\right) + o(x^{4})}{x^4}\\",
            r"&=\lim_{x\to 0}\frac{ \frac{x^{4}}{24} - \frac{x^{4}}{8} + o(x^{4})}{x^4}\\",
            r"&=\lim_{x\to 0}\frac{ -\frac{x^{4}}{12} + o(x^{4})}{x^{4}}\\",
            r"&=\lim_{x\to 0}(-\frac{1}{12} + o(1))\\",
            r"&=-\frac{1}{12}",
            **sloveStepStyle
        ).next_to(example3,DOWN,aligned_edge=LEFT)
        
        self.play(Write(slove3[0]))
        self.wait(1.7)

        sloveStep3_rec5=SurroundingRectangle(
            sloveStep3[0][-5:],
        )
        sloveStep3_rec6=SurroundingRectangle(
            sloveStep3[-1][-5:],buff=0.01
        )

        self.play(Create(sloveStep3_rec5),Create(sloveStep3_rec6))

        slove3_rec=AnimeTools.EmphasizeTexts(
            self,[slove3[0][36:41]],buff=.1,color=RED
        )

        self.wait()
        
        self.play(Uncreate(slove3_rec),Uncreate(sloveStep3_rec5),Uncreate(sloveStep3_rec6))

        self.play(Write(slove3[1:]))
        self.wait(2)

        self.play(
            FadeOut(sloveStep3,slove3,example3,temp_line)
        )

        example4=MathTex(
            r"\lim_{x \to 0} \frac{\ln(1+\sin x)-x}{x^2}",
            **exampleStyle
        ).next_to(titlepos,DOWN,aligned_edge=LEFT)
        self.play(Write(example4))
        self.wait(1.5)

        slove4_step1_rec=AnimeTools.EmphasizeTexts(
            self,[example4[0][6:16]],buff=.1
        )
        
        tempSolve=example4[0][6:16].copy()
        self.wait(.5)
        self.play(tempSolve.animate.shift(RIGHT*5.5),rate_func=smooth)
        self.wait()

        slove4_step1=MathTex(
            r"\text{令 }  u =\sin x,\text{ 则: }",
            r"\ln(1+u)=u-\frac{u^2}{2}+o(u^2)",
            color=YELLOW,
            font_size=27,
            stroke_width=1
        ).next_to(tempSolve,DOWN,aligned_edge=LEFT)        

        self.play(Write(slove4_step1))

        slove4_step1_rec2=AnimeTools.EmphasizeTexts(
            self,[slove4_step1[1][-5:]],color=RED,buff=.1
        )
        slove4_step1_tex=Text(
            "皮亚诺余项：是一个“定性描述”，而不是一个具体算出来的式子",
            font=font_1,font_size=23,color=_color_10
        ).next_to(slove4_step1_rec2,DOWN).shift(LEFT*2)

        self.play(Write(slove4_step1_tex))

        self.wait(2)

        self.play(FadeOut(slove4_step1_tex),Uncreate(slove4_step1_rec2))

        slove4_step2=MathTex(
            r"= \sin x-\frac{\sin^2x}{2}+o(\sin^2x)",
            color=_color_9,
            font_size=27,
            stroke_width=1
        ).next_to(tempSolve,RIGHT,aligned_edge=ORIGIN)

        self.play(Write(slove4_step2))

        slove4_step3=MathTex(
            r"\lim_{x \to 0} \frac{\sin x-\frac{\sin^2x}{2}-x+o(\sin^2x)}{x^2}",
            font_size=27,
            stroke_width=1,
            color=_color_10
        ).next_to(slove4_step1,DOWN,aligned_edge=LEFT)
        self.wait()
        self.play(Write(slove4_step3))
        self.wait(2)
        
        slove4_step4=MathTex(
            r"\sin x = x - \frac{x^{3}}{6} + o(x^{3})",
            r"\;\;[(-1)^n \frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+1})]",
            color=YELLOW,
            font_size=27,
            stroke_width=1
        ).next_to(slove4_step1,DOWN,aligned_edge=LEFT)

        self.play(
            ReplacementTransform(slove4_step3,slove4_step4[0])
        )
        slove4_step4[1].set_color(BLUE)
        self.wait()
        self.play(Write(slove4_step4[1]))
        self.wait()

        self.play(slove4_step4.animate.shift(DOWN*4),
                  slove4_step1.animate.shift(DOWN*4),
                  lag_ratio=0.3)
        
        slove4_step5=MathTex(
            r"= (x - \frac{x^{3}}{6} + o(x^{3}))-",
            r"\frac{(x - \frac{x^{3}}{6} + o(x^{3}))^2}{2}+",
            r"o(x^2)",
            color=_color_9,
            font_size=27,
            stroke_width=1,
        ).next_to(tempSolve,DOWN,aligned_edge=LEFT)

        self.play(
            ReplacementTransform(slove4_step2.copy(),slove4_step5)
        )
        self.wait(2)

        slove4_step5_rec=AnimeTools.EmphasizeTexts(
            self,[slove4_step5[1][:15]],buff=.1
        )

        slove4_step6=MathTex(
            r"(x - \frac{x^{3}}{6} + o(x^{3}))^2=",
            r"",
            color=BLUE,
            font_size=27,
            stroke_width=1,
        ).next_to(slove4_step5,DOWN,aligned_edge=LEFT)

        self.wait(1.3)
        self.play(ReplacementTransform(slove4_step5[1][:15].copy(),slove4_step6),
                  Uncreate(slove4_step5_rec))









