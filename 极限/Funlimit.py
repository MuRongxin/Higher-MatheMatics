from manim import *
import numpy as np

from manim.utils.rate_functions import (ease_in_out_cubic )
from typing import Callable, Sequence

# 配置LaTeX支持中文
config.tex_template = TexTemplate(
    preamble=r"""
\usepackage{ctex}
\usepackage{amsmath,amssymb}
"""
)
_color_1="#39c5bb"  
_color_2="#C1003C"  
_color_3="#07A1B1"  
_color_3="#11999e"
_color_4="#ff2e63"
_color_4=ManimColor("#ff2e63")
_color_5="#79D87E"
_color_6="#0B3B6A"
_color_7="#ffaaa5"
_color_8="#FFFFFF"

deyi_hei_path = r"./font/SmileySans-Oblique-2.ttf"
font_path=r".\font\SmileySans-Oblique-2.ttf"
font_1="FZCuYuan-M03"
# font_2="FZZhengHeiS-EB-GB"
font_3="H.H. Samuel"
font_4="Harlow Solid"
font_5="Kristen ITC"
font_6="Playbill"
font_7="STCaiyun"
# font_8="WenYue XinQingNianTi J"
font_8="文悦新青年体 (须授权)"
font_9="FZZongYi-M05S"
font_foreign="Forte"
font_2="得意黑"
font_10="Smiley Sans"

#SmileySans-Oblique_6.ttf

class Infinitesimal(ZoomedScene,MovingCameraScene):
    def __init__(self,renderer=None, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.5,
            renderer=renderer,
            zoomed_display_height=4,
            zoomed_display_width=7,
            image_frame_stroke_width=1,
            zoomed_camera_config={
                "default_frame_stroke_width": 2,
                "default_frame_stroke_color":_color_7
            },
            zoomed_camera_image_mobject_config={                
                "stroke_color": _color_7,
            },
            **kwargs
    )
    
    def construct(self):
        
        rec_playground = Rectangle(
            width=10,
            height=5,
            fill_color=_color_5,
            fill_opacity=1,
            stroke_width=4
        )


        self.play(Create(rec_playground),run_time=1.5)

        self.camera.frame.save_state()

        illus_text=Text(
            "假设这里有一块足球场",font=font_8,
            font_size=41).next_to(rec_playground,UP,aligned_edge=LEFT)
        self.play(Write(illus_text))
        self.wait(1)

        self.play(
            self.camera.frame.animate.move_to(
                rec_playground.get_corner(DR)+LEFT*1+UP),
            
        )

        hiveGroup = self.GenerateHive(rec_playground)
        
        self.play(FadeOut(illus_text))
        self.wait(1)

        self.play(Restore(self.camera.frame),run_time=5,rate_func=ease_in_out_cubic)

        summary_text_1=Text(
            "这个不断分割的过程中产生的每一块“蛋糕” ",          
            font_size=30,
            color=_color_6,
            font=font_2
        )
        summary_text_2=Text(
            "  相对于足球场来说都越来越微不足道， ",
             font_size=30,
             color=_color_6,
             font=font_2
        )
        summary_text_3=Text(
            "   但它们本身都大于 0 ",
             font_size=30,
             color=_color_6,
             font=font_2
             )
        summary_text=VGroup(
            summary_text_1,summary_text_2,summary_text_3
        ).arrange(DOWN,aligned_edge=LEFT).move_to(
            rec_playground.get_center()+RIGHT*.3).set_stroke(width=1.5,color=_color_8)
        self.play(Write(summary_text))
        self.wait(1)

        self.play(LaggedStart(
            Uncreate(rec_playground),
            FadeOut(summary_text),lag_ratio=.2))   

        conclusion_text= Paragraph(
            "这个“不断缩小的、越来越微不足道的、但始终大于零的量 ”",
            "在数学上我们就叫它“无穷小量（无穷小） ”",
            font=font_8,
            font_size=25,
            line_spacing=1,
            alignment="center"  # 或 "left"
        ).shift(DOWN*1.7)

        recs=VGroup()
        for i in range(40,0,-1):
            if i%5 !=0: continue
            rec=Rectangle(
                width=i*0.1,
                height=i*0.1,
                stroke_width=1,
                fill_opacity=1,
            )

            recs.add(rec)

        recs.arrange(RIGHT,aligned_edge=DOWN).move_to(ORIGIN+UP*1.5)

        self.play(Write(conclusion_text),LaggedStartMap(FadeIn,recs,lag_ratio=.2))  
        self.play(recs.animate.shift(LEFT*3),run_time=8,rate_func=linear)
        
        self.play(FadeOut(conclusion_text),FadeOut(recs))

        emphasize_text=Paragraph(
            "无穷小量不是0，或是接近于零的一个数，它在数学上是一个“量” ",           
            "可以把它看作一个“过程”，一个“趋势”",
            "无穷小量更像是在描述一个不断变小、无限接近零的状态或过程，而不是一个固定的、具体的数字。",
            font=font_8,
            font_size=25,
            line_spacing=1,
            alignment="left"
        )

        self.play(Write(emphasize_text))
        self.wait(2)
        self.play(FadeOut(emphasize_text))
        express_text = MathTex(
        r"""
            \begin{aligned}
                &\text{常用希腊字母 }  \alpha \text{ 或 }  \beta \text{ 来表示一个无穷小量}\\
                &\text{如果当 } x \to a \text{ 时，函数} f(x) - L \to 0 \\
                &\text{那么} f(x) - L \text{ 就是一个当 } x \to a \text{ 时的无穷小量}                                                            
            \end{aligned}
         """,
            font_size=30,
            stroke_width=1
        )
        self.play(Write(express_text),express_text.animate.shift(LEFT))

        express_mathText=MathTex(
            r"\text{如果函数} f(x) \text{满足} \lim_{x \to a} f(x)=0 \text{ 则称 } \
            f(x)\text{ 是 }x\to a \text{ 时的无穷小量}\\",
            font_size=30,
            stroke_width=1,
            color=_color_4
        )
        express_example=MathTex(
            r"""
            \begin{aligned}
                &\text{已知条件：} lim_{x \to 1}(x-1)^2=0  \\                
                &\text{根据定义，} \lim_{x\to 1}(x-1)^2=0
                \text{ 成立，因此}(x-1)^2 \text{ 是 }x \to 1 \text{ 时的无穷小量} \\ 
            \end{aligned}
            """,
            font_size=30,
            stroke_width=1,
            color=_color_3
        )

        self.play(express_text.animate.shift(UP*1.5))
        self.play(Write(express_mathText),
                  express_mathText.animate.next_to(
                      express_text,DOWN,aligned_edge=LEFT, buff=.5
                  ))
        self.wait(1)
        self.play(Write(express_example),
                  express_example.animate.next_to(
                      express_mathText,DOWN,aligned_edge=LEFT, buff=.5))
        
        self.wait(1)



        self.introduce_concept()    

        self.MisConception()
    
    def MisConception(self):
        text_1=Text(
            "对于趋近于0的相对速度的错误理解：",
            font=font_2
        )

        self.play(Write(text_1))
        self.wait(1)
        self.play(FadeOut(text_1))

        text_2_example=MathTex(
            r"\text{例子,当} x \to 0 \text{时，}x^2\text{是比 } x \text{ 高阶的无穷小，}",
            font_size=33,
            stroke_width=1,
            color=RED
        ).to_corner(UL).shift(DOWN)

        self.play(Write(text_2_example))

        def make_axes(x_range,x_length) -> Axes:
            return Axes(
                x_range=x_range,
                y_range=(-0.4,3,1),
                x_length=x_length,
                axis_config={
                    "color": WHITE,
                    "include_numbers": True,
                    "font_size": 25,
                    "tip_length": .1,
                    "tip_width": .1,
                }
            )
   

        def make_graphs(ax: Axes,
                        g_labOffsetMul:float,
                        f_labOffsetMul:float) -> tuple[ParametricFunction, ParametricFunction, Mobject, Mobject]:
            """返回 (g_curve, f_curve, g_label, f_label)"""
            g = ax.plot(lambda x: x, color=_color_3, x_range=[-0.3, 1.9])
            f = ax.plot(lambda x: x**2, color=_color_4, x_range=[-0.5, 1.7])

            g_lab = MathTex(
                "g(x)=x", color=_color_3, font_size=33,
                ).move_to(g.get_center()+UP+RIGHT*g_labOffsetMul)
    
            f_lab = MathTex(
                "f(x)=x^2", color=_color_4, font_size=33,
                ).move_to(f.get_center()+UP*2+RIGHT*f_labOffsetMul)  

            return g, f, g_lab, f_lab

        def make_area(
                ax: Axes,
                curve: ParametricFunction,
                x0: float,
                x1: float,
                color: ManimColor,
                opacity: float = 0.2,
                ) -> tuple[Mobject, Mobject, Mobject, Mobject | None]:
            """返回一个 VGroup(area, v_line_x0, v_line_x1, 可选标签)"""
            area = ax.get_area(curve, x_range=[x0, x1], color=color, opacity=opacity)
            v0 = ax.get_vertical_line(
                ax.c2p(x0, curve.underlying_function(x0)), stroke_width=3
            )
            v1 = ax.get_vertical_line(
                ax.c2p(x1, curve.underlying_function(x1)), stroke_width=3
            )
    
            grp = VGroup(area, v0, v1)
            lab=None
            if x1 < 0.5:  # 只在第一次放大时给 x1 写标签
                lab = MathTex(
                    f"{x1}", font_size=23
                ).next_to(ax.c2p(x1, 0), DOWN, buff=0.2)
                grp.add(lab)
            return area, v0, v1,lab

        init_axes=make_axes(x_range=(-0.4,1.7,1),x_length=4
                            ).to_edge(DOWN).shift(LEFT*4.3+DOWN*0.8).scale(.8)
        labels = init_axes.get_axis_labels(
            x_label=Text("t",font_size=23,stroke_width=1), 
            y_label=Text("y",font_size=23,stroke_width=1))

        g_curve, f_curve, g_label, f_label = make_graphs(init_axes,2,0.8)

        self.play(Create(init_axes),Create(labels))
        self.play(LaggedStartMap(Create, 
                                 VGroup(
            g_curve, f_curve, g_label, f_label
        ),lag_ratio=0.7,run_time=1.5))

        self.wait(1)

        zoom_rec=Rectangle(
            width=3.5,
            height=2,
            color=_color_7,
            stroke_width=2,
        ).move_to(init_axes.c2p(0.5,0.5))

        self.play(Create(zoom_rec))

        self.wait(1)
        

        # self.zoomed_camera.frame.set_stroke(BLUE, 2) # 设置放大镜边框颜色和宽度

        self.zoomed_camera.frame.move_to(init_axes.c2p(0.5, 0.5)) # 将放大镜移动到坐标原点
              

        self.zoomed_camera.frame.match_width(zoom_rec)
        self.zoomed_camera.frame.match_height(zoom_rec)

        self.zoomed_camera.frame.set_color(_color_7)

        # self.zoomed_display[0].set_stroke(_color_7) ?????


        # 激活放大动画
        self.activate_zooming()

        self.play(self.get_zoomed_display_pop_out_animation())

        self.wait(.7)

        # 切点滑动器
        x_tracker = ValueTracker(0.9) 
        dot = always_redraw(
            lambda: 
            Dot(init_axes.c2p(x_tracker.get_value(),
                f_curve.underlying_function(x_tracker.get_value())),
                color=_color_1,radius=0.04
            )
        )
        # 动态切线（长度固定 4 单位）
        def make_tangent():
            x0 = x_tracker.get_value()
            y0 = f_curve.underlying_function(x0)
            slope = 2 * x0                       # f'(x)=2x
            dl = 2                              # 单侧延伸长度
            p_left = init_axes.c2p(x0 - dl, y0 - dl * slope)# 直线方程推导
            p_right = init_axes.c2p(x0 + dl, y0 + dl * slope)
            return Line(p_left, p_right, stroke_width=2)

        tangent = always_redraw(make_tangent)
        # 动画：x 从 0.5 → 0.05
        self.play(FadeIn(dot, tangent))
        self.play(x_tracker.animate.set_value(0.05), run_time=2.5, rate_func=linear)
        self.wait()
        
        
        axes_1=make_axes(x_range=(-0.4,1.7,0.5),x_length=9
                            ).to_edge(DOWN).shift(LEFT*4.1+DOWN*0.8).scale(.8)
        labels_1 = axes_1.get_axis_labels(
            x_label=Text("t",font_size=23,stroke_width=1), 
            y_label=Text("y",font_size=23,stroke_width=1))

        g_curve_1, f_curve_1, g_label_1, f_label_1 = make_graphs(axes_1,3.8,2.8)

                
        
        
        # 先播放收起动画
        self.play(self.get_zoomed_display_pop_out_animation(), reverse_rate_function=True)
       
        # # 动画结束后，再彻底移除组件
        self.remove(self.zoomed_camera.frame, self.zoomed_display)
        self.play(Uncreate(zoom_rec),Uncreate(tangent),Uncreate(dot))
        self.wait()
        
        self.play(
            ReplacementTransform(init_axes, axes_1),
            ReplacementTransform(labels, labels_1),
            ReplacementTransform(g_curve, g_curve_1),
            ReplacementTransform(f_curve, f_curve_1),
            ReplacementTransform(g_label, g_label_1),
            ReplacementTransform(f_label, f_label_1),
        )

        #=========Table============
        



        area_1,line_1,line_2,lab_1=make_area(
            axes_1, g_curve_1,x0=1,x1=0.5, color=ManimColor(_color_1), opacity=0.3)

        self.play(LaggedStartMap(Create,VGroup(
                        area_1,line_1,line_2)))
        
        area_2,line_3,line_4,lab_2=make_area(
            axes_1, g_curve_1,x0=.5,x1=0.1, color=ManimColor(_color_7), opacity=0.3)
        self.play(LaggedStartMap(Create,
                 VGroup(area_2,line_3,line_4,lab_2)))
        
        area_3,line_5,line_6,lab_3=make_area(
            axes_1, g_curve_1,x0=.1,x1=0.01, color=ManimColor(_color_8), opacity=0.3)
        self.play(LaggedStartMap(Create,
                 VGroup(area_3,line_5,line_6,lab_3)))

    def introduce_concept(self):
        """引入无穷小量的基本概念"""
        # 清除标题
        self.play(FadeOut(*self.mobjects))
        
        # 重新添加标题
        title = Text("无穷小量的阶 ", font_size=30,font=font_2).to_edge(UL)
        self.play(Write(title))
        

        emphasize_text = Paragraph(
            "无穷小量的分类是必要的 ",
            "依据主要是它们趋近于0的相对速度",
            "当自变量 x 趋近于某个点时，不同的无穷小量趋近于0的速度可能不同。",
            font_size=30,
            font=font_2,
            line_spacing=1,
        ).to_edge(UP,buff=1.5).shift(LEFT*.3)
        
        
        surrend_part=SurroundingRectangle(
            emphasize_text[1],
            color=_color_4, stroke_width=4, fill_opacity=0)

        # 概念说明
        concept_text = MathTex(
            r"""
            \begin{aligned}
            &\text{当 } x \to a \text{ 时， }\alpha(x) \text{ 和 } \beta(x) \text{ 都是无穷小量}\\
            &\text{即 } \lim_{x \to a} \alpha(x) = 0, \lim_{x \to a} \beta(x) = 0 \\         
            &\text{通过计算极限} \lim_{x \to a} \frac{\alpha(x)}{\beta(x)} \text{比较趋近速度}\\
            \end{aligned}
            """,
            font_size=30,
            color=_color_1,
            stroke_width=1,
            ).next_to(emphasize_text,DOWN,aligned_edge=LEFT,buff=.7)
        
        ilustrate_text=MathTex(r"""
            \begin{aligned}   
                 &\text{若 } \alpha(x)\text{ 比 }\beta(x) \text{ 趋近于 0 的速度快，}\\
                 &\text{则} \lim_{x\to a}\frac{\alpha(x)}{\beta(x)} =0 \\
                 &\alpha(x) \text{就是比} \beta(x) \text{高阶的无穷小量}
            \end{aligned}
        """,
            font_size=28,  
            color=_color_4         
        ).next_to(concept_text,RIGHT,buff=1)
        
        rec_illustrate=SurroundingRectangle(
            ilustrate_text, color=_color_1, stroke_width=2, fill_opacity=0
        )

        self.play(Write(emphasize_text))
        self.wait(1)
        self.play(Write(concept_text))
        self.wait(1)
        self.play(Write(ilustrate_text),Create(rec_illustrate))

        self.wait(2)

        self.play(Create(surrend_part))

        emphasize_title_temp = emphasize_text[1].copy()

        emphasize_title=Text(
            "依据主要是它们趋近于0的相对速度",
            font_size=31,
            font=font_2,
        ).to_edge(UL)


        self.add(emphasize_title_temp)
        self.wait(.8)
        # 淡出文字
        self.play(LaggedStartMap(FadeOut,
                VGroup(
                    concept_text,
                    emphasize_text,
                    ilustrate_text,
                    rec_illustrate,
                    title))
        )

        
        self.wait(.7)
        self.play(Uncreate(surrend_part),
                  ReplacementTransform(emphasize_title_temp, emphasize_title))

        self.wait(1)


    def GenerateHive(self,target):
        COLS, ROWS     = 30, 30
        init_w, init_h = 0.1, 0.1
        gap_step       = 0.04          # 组间额外裂口距离
        MAX_DEPTH      = 10            # 总层数

        # ========== 1. 创建 100 块紧密方阵 ==========
        rects = VGroup(*[
            Rectangle(
                width=init_w+ 0.01, height=init_h+0.01, 
                stroke_width=0, fill_opacity=1,color=WHITE)
            .move_to(np.array(
                [(j-COLS/2+0.5)*init_w, (i-ROWS/2+0.5)*init_h, 0]))
                    for i in range(ROWS) for j in range(COLS)
        ]).move_to(target.get_corner(DR)+LEFT*1+UP).scale(0.02)
        self.play(FadeIn(rects))
        self.wait(.3)
        cakeTex=Text(
            "这里有一块蛋糕 ", font_size=4,color=_color_4,font=font_8
            ).next_to(rects,UP*.1)
         
        

        # ========== 2. BFS 预处理 ==========
        # 第 0 层：只有根组
        layers = [ [VGroup(*rects)] ]   # layers[depth] = 当前层所有组

        for depth in range(MAX_DEPTH):
            new_layer = []
            axis = depth % 2            # 0 横切 1 竖切
            for grp in layers[-1]:      # 对上一层每个组
                # 排序 + 对半分
                grp.submobjects.sort(key=lambda m: m.get_center()[axis])
                n = len(grp)
                left_g  = VGroup(*grp[:n//2])
                right_g = VGroup(*grp[n//2:])
                new_layer.extend([left_g, right_g])
            layers.append(new_layer)

        # ========== 2. 移动镜头 ==========

        # self.play(
        #     Restore(self.camera.frame)
        # )

        self.play(
            self.camera.frame.animate.set_width(1)
        )
        self.play(Write(cakeTex))
        self.wait(1)
        self.play(Uncreate(cakeTex))

        # ========== 3. 逐层同时分裂 ==========
        for depth in range(1, MAX_DEPTH + 1):
            axis = (depth - 1) % 2
            prev_groups = layers[depth - 1]  # 父层
            curr_groups = layers[depth]      # 子层（已是对半分好的顺序）

            anims = []
            if depth == 7:
                anims.append(
                    self.camera.frame.animate.set_width(1.8)
                )

            if depth == 9:
                anims.append(
                    self.camera.frame.animate.set_width(2.5)
                )
            for i, parent in enumerate(prev_groups):
                left_child  = curr_groups[i * 2]
                right_child = curr_groups[i * 2 + 1]

                # 计算裂口距离
                if axis == 0:  # 水平切 → 左右分离
                    gap = (left_child.width + right_child.width) / 2 + gap_step
                    anims += [
                    left_child.animate.shift(-gap * RIGHT),
                    right_child.animate.shift( gap * RIGHT),
                    ]
                else:  # 垂直切 → 上下分离
                    gap = (left_child.height + right_child.height) / 2 + gap_step
                    anims += [
                    left_child.animate.shift(-gap * UP),
                    right_child.animate.shift( gap * UP),
                    ]

            self.play(*anims, run_time=.7,rate_func=smooth)

        self.wait(1.5)

        self.play(
            self.camera.frame.animate.move_to(rects[100].get_center()).set_width(0.01),
            run_time=2.5,rate_functions=smooth)


class TheHigherInfinitesimal(Scene):
    def construct(self):
        def_card = MathTex(
            r"\lim_{x\to a}{\alpha(x)\over\beta(x)}=0\;\Rightarrow\;\alpha(x)=o(\beta(x))",
            font_size=36
        )

        temp=Text("Hello .worlfd，我真的好喜欢你！",font="得意黑")
        self.add(temp)
        self.play(Write(def_card))
        
        self.wait()        

# 不是在某个时间点离起点有多远，而是在接近终点（0）的过程中，谁“消失”得更快。
