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
_color_3="#11999e"
_color_4=ManimColor("#ff2e63")
_color_5="#79D87E"
_color_6="#fff4e1"
_color_7="#ffaaa5"
_color_8="#b9d7ea"
_color_9="#7dace4"
_color_10=ManimColor("#aedefc")

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
            font=font_8,
            stroke_width=1
        )
        summary_text_2=Text(
            "  相对于足球场来说都越来越微不足道， ",
             font_size=30,
             color=_color_6,
             font=font_8,
             stroke_width=1
        )
        summary_text_3=Text(
            "   但它们本身都大于 0 ",
             font_size=30,
             color=_color_6,
             font=font_8,
             stroke_width=1
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

        def make_axes(x_range, y_range=(-0.4,3,1),x_length:float=1) -> Axes:
            return Axes(
                x_range=x_range,
                y_range=y_range,
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
        table_datas = [table_data_1, table_data_2, table_data_3, 
                       table_data_4,table_data_5, table_data_6]
        
        def get_table(data):
            table = Table(
                data, 
                include_outer_lines=True,
                line_config={"stroke_width": 1.5},
                arrange_in_grid_config={"cell_alignment": LEFT},
                h_buff=.5,               
            ).scale(.375)            
          

            return table
        table_group = VGroup()
        for td in table_datas:
            table_group.add(get_table(td))

        # 统一
        max_height = max(table.height for table in table_group)
        for table in table_group:
            # 设置表头行样式（第一行）
            header_row = table.get_rows()[0]
            for cell in header_row:
                cell.set_color(YELLOW).set_font_weight(BOLD)
            
            if table.height < max_height:
                # 计算缩放因子使高度一致
                scale_factor = max_height / table.height
                table.scale(scale_factor)
            
        table_group.arrange(RIGHT,buff=0).shift(RIGHT*9) 
        
        
        # 设置第一列样式（时间段列）
        first_column = table_group[0].get_columns()[0]
        for i, cell in enumerate(first_column):
            if i > 0:  # 跳过表头
                cell.set_color(BLUE)
        
        table_title=MathTex(
            r"g(x)=x\text{ 与 }f(x)=x^2\text{ 的对比}",
            font_size=35,
            stroke_width=1
        ).next_to(table_group,UP)
        
        x2=ValueTracker(1.5)
        dotgx=always_redraw(
            lambda: 
            Dot(axes_1.c2p(x2.get_value(),g_curve_1.underlying_function(x2.get_value())),
                color=_color_4,radius=0.1
            )
        )
        dotfx=always_redraw(
            lambda:
            Dot(axes_1.c2p(x2.get_value(),f_curve_1.underlying_function(x2.get_value())),
                color=_color_3,radius=0.1
            )
        )

        explain_1=Paragraph (
            "这是因为混淆了两种完全不同的“速度”",
            "我们列表计算出的速度",
            "相当于函数值 y 相对于自变量 x 的变化率 ",
            " Δy / Δx，近似于“瞬时速度”",            
            "“瞬时速度”只描述了“那一瞬间”的情况",
            "而忽略了“当前离 0 还有多远”",
            font_size=25,
            font=font_2,
            line_spacing=1
        )
        
        # 动画序列


        area_1,line_1,line_2,lab_1=make_area(
            axes_1, g_curve_1,x0=1,x1=0.5, color=ManimColor(_color_1), opacity=0.3)

        self.play(LaggedStartMap(Create,VGroup(
                        area_1,line_1,line_2)))
        
        area_2,line_3,line_4,lab_2=make_area(
            axes_1, g_curve_1,x0=.5,x1=0.1, color=ManimColor(_color_7), opacity=0.3)
        self.play(LaggedStartMap(Create,
                 VGroup(area_2,line_3,line_4,lab_2,table_group[0])))
        
        area_3,line_5,line_6,lab_3=make_area(
            axes_1, g_curve_1,x0=.1,x1=0.01, color=ManimColor(_color_8), opacity=0.3)
        self.play(LaggedStartMap(Create,
                 VGroup(area_3,line_5,line_6,lab_3)))
        
        self.wait()
        # =========Move Camera============
        self.play(
            self.camera.frame.animate.shift(RIGHT*9)
        )


        #=========Table============
        self.play(LaggedStartMap(Write,table_group[1:],lag_ratio=.5),Write(table_title))
        self.wait(2)
        
        #===========Restore=========
        tempGroup=VGroup(table_group[0],
            table_group[4],table_group[5]
        ).copy().arrange(RIGHT,buff=0).shift(RIGHT*4.1).scale(0.9)
        
        self.play(LaggedStart(
                self.camera.frame.animate.shift(LEFT*9),        
                FadeOut(table_title),
                ReplacementTransform(table_group,tempGroup),
                Create(dotgx),
                Create(dotfx),
                LaggedStartMap(Uncreate,[area_1,area_2,area_3]),
                run_time=4,rate_func=linear
            )
        )
        self.wait()

        # table4_rec=SurroundingRectangle(
        #         table_group[4],
        #         buff=0.1,
        #         stroke_width=3,
        # )
        
        flashs1= [Flash(tempGroup[1].get_cell((i, 1)),color=RED) for i in range(1,7)]
        flashs2= [Flash(tempGroup[2].get_cell((i, 1)),color=BLUE_D) for i in range(1,7)]
        self.play(
            LaggedStart(*flashs1,
                lag_ratio=0.3
            ),
            LaggedStart(*flashs2,
                lag_ratio=0.3
            )
        )
        
        self.play(
            x2.animate.set_value(0.2),
            run_time=3,rate_func=smooth
        )

        self.wait()
        
        

        self.play(tempGroup.animate.shift(UP*2))
        self.play(
            Create(explain_1),
            explain_1.animate.next_to(tempGroup,DOWN,aligned_edge=LEFT)
        )
        self.wait()

        exp_1_rec=SurroundingRectangle(explain_1[5], color=RED, buff=0.1)
        self.play(Create(exp_1_rec))
        self.wait(.7)
        self.play(Uncreate(exp_1_rec))

        to_remove = [m for m in self.mobjects if isinstance(m, VMobject)]
        self.play(*[FadeOut(objs) for objs in to_remove])
        
        #==================Next Page==============================
        title_p2=Text(
            "我们在意的不是“谁的函数数值跑得快”，而是 “谁更快地抵达终点 0 ” ",
            font=font_2,
            font_size=30,
            stroke_width=1
        ).to_edge(UP)
        title_p2.add_background_rectangle(color=BLUE, opacity=0.8, buff=0.1)
       
        
        axes_2=make_axes((-.5,1,1),(-.3,3,1),2)
        g_curve_2,f_curve_2,g_lab2,f_lab2=make_graphs(axes_2, 2,1)
       


        graph_group=VGroup(axes_2, g_curve_2,f_curve_2,g_lab2,f_lab2).shift(DOWN*.5)
        self.play(LaggedStart(
            Write(title_p2),
            Create(graph_group.to_edge(LEFT)),
           rate_func=linear,lag_ratio=0.4
        ))

        table2=Table(
            table_data_f,
            include_outer_lines=True,
            element_to_mobject_config={"font_size": 30,},                                      
            line_config={"stroke_width": 2.5},
            v_buff=.3,
            h_buff=.5,
            
        ).scale(.5).shift(RIGHT*3.2+UP)

        self.wait()

        first_column = table2.get_columns()[0]
        first_row = table2.get_rows()[0]
        for cell in first_row:
            cell.set_color(_color_4)
        for i, cell in enumerate(first_column):
            if i > 0:  # 跳过表头
                cell.set_color(BLUE)
        self.play(Write(table2),run_time=3)
        self.wait()

        #===========Emphasize Table============
        empha_table_1=[Indicate(table2.get_cell((i, 1)),color=_color_5,rate_func=there_and_back) for i in range(2,7)]
        empha_table_2=[Indicate(table2.get_cell((i, 4)),color=_color_7) for i in range(2,7)]
        
        self.play(
                  LaggedStart(*empha_table_1,lag_ratio=.3),
                  LaggedStart(*empha_table_2,lag_ratio=.3))
        self.wait()


        explain_2_1=MathTex(
            r"\text{当} x \text{趋近于 }0\text{ 时，}\frac{f(x)}{g(x)} \text{的值也趋近于}0",
            font_size=30,
            stroke_width=1,
        )    
        explain_2_2=Paragraph(    
            "这意味着，f(x)的位置相对于g(x)的位置",
            "已经『微不足道了』",
            "可以说, f(x)已经“到达”了终点，而 g(x) 还在路上",
            line_spacing=1,   
            font_size=27,
            font=font_2
        )

        explain_2=VGroup(explain_2_1,explain_2_2
        ).arrange(DOWN,aligned_edge=LEFT).next_to(table2,DOWN,aligned_edge=LEFT)

        self.play(Write(explain_2))

        self.wait()
        self.play(Uncreate(graph_group))

        descrip_1=Paragraph(
            "举个生活中的例子----",
            "一辆法拉利（g(x)）:",
            "在距离终点1公里的地方，以100km/h的速度飞驰",
            "一只蜗牛（f(x)）:",
            "已经到距离终点线1毫米的地方，速度是0.001km/h", 
            line_spacing=1,
            font=font_2,
            font_size=25,
        ).next_to(title_p2,DOWN).to_edge(LEFT,buff=0.1)

        descrip_1[1].add_background_rectangle(color=_color_2, opacity=0.8, buff=0.1)
        descrip_1[3].add_background_rectangle(color=_color_7, opacity=0.8, buff=0.1)
        self.play(Write(descrip_1))
        self.wait()

        ques_1=Text(
            "请问：谁会更快地抵达终点？",
            font_size=30,
            font=font_2,           
        ).next_to(descrip_1,DOWN,buff=.3)

        surr_ques=SurroundingRectangle(
            ques_1,
            color=_color_1,
            stroke_width=4,
            fill_opacity=0
        )

        answer_1=Paragraph(
            "显然是蜗牛！",
            "虽然它的瞬时速度极慢，但它离终点已经近到可以忽略不计了!",
            line_spacing=1,
            font_size=25,
            font=font_2,  
        ).next_to(
            ques_1,DOWN,buff=.3,
         ).align_to(descrip_1,LEFT).add_background_rectangle(color=_color_4, opacity=1, buff=0.15)

        self.play(Write(ques_1),Create(surr_ques),lag_ratio=0.5,run_time=2)
        self.wait()
        self.play(Write(answer_1))
        
        self.wait(2)
        
        to_remove = [m for m in self.mobjects ]
        self.play(*[FadeOut(objs) for objs in to_remove])


        #==================Next Page==============================

        descrip_2=Paragraph(
            "无穷小的阶数关注的是函数值本身趋近 0 的速度，而不是变化率",
            "直接比较 f(x) 和 g(x)数值的变化速度",
            "就像只看法拉利和蜗牛的仪表盘，却不看它们各自的位置，这显然是片面的",
            line_spacing=1,
            font_size=25,
            font=font_2,  
        ).to_corner(UL)

        self.play(Write(descrip_2))
        self.wait(1)

        descrip_3=Paragraph(
            "f(x) 和 g(x) 都在向0移动。我们想知道，在移动的过程中，f(x) 相对于 g(x) 来说，是不是",
            "更快地完成了它的旅程”",
            line_spacing=1.3,
            font_size=27,
            font=font_2, 
        )
        descrip_3[1].add_background_rectangle(
            color=_color_4, opacity=0.8, buff=0.1)
        descrip_3.next_to(descrip_2,DOWN,buff=.5,aligned_edge=LEFT)

        self.play(Succession(Write(descrip_3)))
        self.play(Indicate(descrip_3[1],color=BLUE,rate_func=there_and_back))
        self.wait(1)

        descrip_4=MathTex(
            r"R(x) = \frac{f(x)}{g(x)} = \frac{x^2}{x} = x",
            color=_color_4,
            font_size=30,
            stroke_width=1.3,
        )

        surr_des_4=SurroundingRectangle(
            descrip_4,
            color=_color_1,
            stroke_width=4, 
                 
        )

        self.play(Write(descrip_4),descrip_4.animate.next_to(
            descrip_3[1],RIGHT,buff=.5).shift(DOWN*.2),Create(surr_des_4),
            surr_des_4.animate.next_to( descrip_3[1],RIGHT,buff=.5).shift(DOWN*.2+LEFT*.1))
        self.wait(.7)

        descrip_5 = Paragraph(
            "这个 R(x) 就是“相对位置”。它回答了这样一个问题：",
            "“在 x 这个时刻，$f(x)$ 离终点的距离，是 g(x) 离终点距离的几分之几？”",           
            "当 x=0.1 时，R(0.1)=0.1。这意味着 f(x) 的路程只剩下 g(x) 的 10% 了。",
            "当 x=0.01 时，R(0.01)=0.01。这意味着 f(x) 的路程只剩下 g(x) 的 1% 了。",
            "当 x=0.001 时，R(0.001)=0.001。这意味着 f(x) 的路程只剩下 g(x) 的 0.1% 了。",
            alignment="left",       # 左对齐
            line_spacing=1,       # 行距
            font_size=25,           # 整体字号
            color=WHITE,            # 默认颜色
            font=font_2,
        ).to_edge(DOWN).shift(LEFT*1.5)

        # 高亮三个关键数字
        descrip_5.chars[2][-5:-2].set_color(YELLOW)   # 0.1
        descrip_5.chars[3][-4:-2].set_color(YELLOW)   # 0.01
        descrip_5.chars[4][-6:-2].set_color(YELLOW)   # 0.001

        self.play(Write(descrip_5))

        self.wait()

        descrip_6=Paragraph(
            "“趋近于0的相对速度”",
            "它描述的是一种“相对位置”的坍缩速度",
            "而不是“瞬时速度”的快慢",
            font=font_2,
            font_size=27,
            line_spacing=.8,
        ).next_to(surr_des_4,RIGHT).shift(DOWN*.3)
        descrip_6.add_background_rectangle(color=_color_1, opacity=0.8, buff=0.2)

        self.play(Write(descrip_6))

        self.wait()


        descrip_7=MathTex(
            r"\text{So 我们通过计算极限 }",
            r"\lim_{x \to a} \frac{\alpha(x)}{\beta(x)}",
            r"\text{ 来比较它们的趋近速度，并据此分类无穷小量}",
            font_size=33,
            stroke_width=2,
        ).to_edge(DOWN,buff=1.7)

        self.play(ReplacementTransform(descrip_5,descrip_7))
        self.wait(2)






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
# 第1列：时间段
table_data_1 = [
    ["时间段"],
    ["1→0.5"],
    ["0.5→0.1"],
    ["0.1→0.01"],
    ["0.01→0.001"],
    ["0.001→0.000001"]
]

# 第2列：Δt
table_data_2 = [
    ["Δt"],
    ["0.5"],
    ["0.4"],
    ["0.09"],
    ["0.009"],
    ["0.000999"]
]

# 第3列：A (x) Δ位置
table_data_3 = [
    [" g(x) Δ位置"],
    ["1→0.5 = -0.5"],
    ["0.5→0.1 = -0.4"],
    ["0.1→0.01 = -0.09"],
    ["0.01→0.001 = -0.009"],
    ["0.001→0.000001 =\n -0.000999"]
]

# 第4列：B (x²) Δ位置
table_data_4 = [
    ["f(x) Δ位置"],
    ["1→0.25 = -0.75"],
    ["0.25→0.01 = -0.24"],
    ["0.01→0.0001 = -0.0099"],
    ["0.0001→0.000001 = -0.000099"],
    ["0.000001→0.000000001 = \n-0.000000999"]
]

# 第5列：A 速度
table_data_5 = [
    ["g(x) 速度"],
    ["0.5/0.5 = 1"],
    ["0.4/0.4 = 1"],
    ["0.09/0.09 = 1"],
    ["0.009/0.009 = 1"],
    ["= 1"]
]

# 第6列：B 速度
table_data_6 = [
    ["f(x) 速度"],
    ["0.75/0.5 = 1.5"],
    ["0.24/0.4 = 0.6"],
    ["0.0099/0.09 ≈ 0.11"],
    ["0.000099/0.009 ≈\n 0.011"],
    ["≈ 0.001"]
]

table_data_f =[
            ["时间点 (x)", "g(x)的位置 (g(x)=x)", "f(x)的位置 (f(x)=x²)", "位置比 f(x)/g(x)"],
            ["1", "1", "1", "1"],
            ["0.5", "0.5", "0.25", "0.5"],
            ["0.1", "0.1", "0.01", "0.1"],
            ["0.01", "0.01", "0.0001", "0.01"],
            ["0.001", "0.001", "0.000001", "0.001"],
        ]

class EquivalentInfinitesimal(Scene):  # 定义一个名为EquivalentInfinitesimal的类，继承自Scene类
    def construct(self):  # 定义construct方法，这是Scene类的主要方法，用于构建场景
        title=Text(
            "等价无穷小",  # 标题文本内容    
            font=font_2,  
            font_size=35, 
            stroke_width=1.8     
            
        ).to_corner(UL)
        
        title_back=Rectangle(
            width=title.width,
            height=title.height,
            fill_opacity=1,
            color=_color_1
        ).move_to(title.get_center()+LEFT*3+DOWN*.2)


        title_back_pos=title_back.animate.move_to(title.get_center()+DOWN*.2+RIGHT*.2)
        
        
        self.add(title_back)  

        self.play(LaggedStart(
            Write(title),
            title_back_pos,
            lag_ratio=0.3,
        ),rate_func=smooth)

        self.wait(.7)

        defint=MathTex(r"""
            \begin{aligned}
                &\text{定义：若 }\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = 1
                      \text{，则称} \alpha(x)\text{ 与 }\beta(x)\text{ 是等价无穷小。} \\
                &\text{ 含义: }\alpha(x) \text{ 和 } \beta(x) \text{ 趋近于 0 的速度相同}\\
                &\text{ 记号: }\alpha(x) \sim \beta(x)\text{ (当 } x \to a)                      
            \end{aligned}
            """,
            font_size=30,
            stroke_width=1
        ).next_to(title_back,DOWN,buff=.7,aligned_edge=LEFT)

        self.play(Write(defint),rate_func=smooth)
        self.wait(1)

        example_title=Text(
            "例如：",
            font=font_2,  
            font_size=30, 
            stroke_width=1     
        ).next_to(defint,DOWN,buff=.7,aligned_edge=LEFT)
        example_title.add_background_rectangle(color=_color_3,buff=.08)

        self.play(Write(example_title),rate_func=smooth)
        

        exampl_1=MathTex(
            r"\text{当 } x \to 0 \text{时，} \sin(x) \text{ 和 }x\text{是等价无穷小量，}", 
            r"\text{因为：}\lim_{x\to 0}\frac{\sin(x)}{x} =1",
            font_size=33,
            stroke_width=1,
        ).next_to(example_title,RIGHT,buff=.4)

        self.play(Write(exampl_1))
        self.wait(1)

        rec_define=SurroundingRectangle(defint)
        example_1_copy=exampl_1.copy().next_to(title_back,DOWN+RIGHT*.1,buff=1.3)
        example_1_copy.add_background_rectangle(
            color=_color_3,buff=.08)
        self.play(
            defint.animate.next_to(
                title_back,RIGHT,buff=.3).shift(DOWN*.2).scale(.9),
                Create(rec_define),rec_define.animate.next_to(
                title_back,RIGHT,buff=.3).shift(DOWN*.3),
                ReplacementTransform(exampl_1,example_1_copy),
                FadeOut(example_title))
        
        
        axes_1=self.make_axes((-10,10,3),(-5,5,2),7,4).to_edge(DOWN,buff=0)
        graphs=self.make_graphs(
            axes_1,"g(x)=x","f(x)=sin(x)",
            [-10,10],[-4,4],RIGHT*1.8+UP,LEFT*1.2+UP*.7)

        self.play(Succession(Create(axes_1),Create(graphs)))
        self.wait(.8)

        axes_2=self.make_axes((-1,1,.2),(-.8,.8,0.4),7,4).to_edge(DOWN,buff=0)
        graphs_2=self.make_graphs(
            axes_2,"g(x)=x","f(x)=sin(x)",
            [-10,10],[-1,1],RIGHT*1.8+UP,LEFT*1.2+UP*.7)
        
        self.play(ReplacementTransform(axes_1,axes_2),
                  ReplacementTransform(graphs,graphs_2),
                  run_time=3)
        self.wait(1)

        axes_3=self.make_axes((-.4,.4,.2),(-.5,.5,.2),4,4).to_edge(DOWN,buff=0).shift(LEFT*4)
        graphs_3=self.make_graphs(
            axes_3,"g(x)=x","f(x)=sin(x)",
            [-.4,.4],[-.4,.4],RIGHT*1.8+UP,LEFT*1.2+UP*.7)

        self.play(ReplacementTransform(axes_2,axes_3),
                  ReplacementTransform(graphs_2,graphs_3))
        
        conclusion_1=Text("当 x → 0 时，sin(x) 与 x 无限接近",
                    font=font_2,font_size=30).next_to(axes_3,RIGHT,buff=.5)
        conclusion_2=Paragraph("虽然它们奔向 0 的“路径”不同",
                          "但它们的“速度”和“姿态”在终点附近几乎一模一样",line_spacing=1,
                    font=font_2,font_size=30).next_to(conclusion_1,DOWN,aligned_edge=LEFT)
        
        
        self.play(Write(conclusion_1))
        self.play(Write(conclusion_2))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        title_2=self.AddTitle("常用等价无穷小",font_size=35,font=font_2)
        self.play(title_2)
        self.wait(1)



        #=========== Function graph -1 ===================

        group_1_tex=MathTex(
            r"x \sim \sin x \sim \tan x \sim \arcsin x " ,
            r"\sim \arctan x",
            font_size=35,
            stroke_width=1
        ).to_corner(UL).shift(DOWN)

        self.play(Write(group_1_tex))
       
        func_group_1=VGroup()
        ax = Axes(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=4,
            axis_config={"include_numbers": True, "font_size": 22,"include_tip":False},
        )
        self.play(Create(ax))  # 先放坐标系，不再动画
        func_group_1.add(ax)

        # 2. 五条函数 + 右侧标签（范围按题目）
        items = [            
            (lambda x: x,          [-3, 3],      r"x",           WHITE),
            (np.arcsin,            [-0.9, 0.9],      r"\arcsin x",   GREEN),
            (np.sin,               [-4, 4],      r"\sin x",      YELLOW),
            (np.tan,               [-1.1, 1.1],  r"\tan x",      RED),            
            (np.arctan,            [-3, 3],      r"\arctan x",   TEAL),
        ]

        anims = []
        for f, xr, tex, color in items:
            g = ax.plot(f, x_range=xr, color=color, stroke_width=2.5)
            # 标签：取曲线右端点右侧 0.4 单位
            label = MathTex(tex, color=color, font_size=33).next_to(
                ax.c2p(xr[1], f(xr[1])), UP, buff=0.3
            )
            anims += [Create(g), Write(label)]
            func_group_1.add(g, label)

        # 3. 依次出现（可改 lag_ratio 调节奏）
        self.play(Succession(*anims), run_time=5)
        self.wait()

        self.play(
            func_group_1.animate.scale(0.5).shift(LEFT*5+UP*1.5),
            group_1_tex.animate.scale(0.7).shift(DOWN*2+LEFT*1.3)
        )
        self.wait()



        #=========== Function graph -2 ===================

        group_2_tex=MathTex(
            r"1 - cos(x) \sim \frac{x^2}{2} " ,           
            font_size=25,
            stroke_width=1
        ).to_edge(DOWN,buff=0.9).shift(LEFT*3.5)

        
       
        func_group_2=VGroup()
        ax_2 = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=4,
            axis_config={"include_numbers": True, "font_size": 22,"include_tip":False},
        ).to_edge(DOWN).shift(RIGHT*2.5)
        self.play(Create(ax_2))  # 先放坐标系，不再动画
        func_group_2.add(ax_2)

        # 2. 五条函数 + 右侧标签（范围按题目）
        items = [            
            (lambda x: 1-np.cos(x),          [-3, 3],      r"1 - cos(x)",   RED),
            (lambda x: x**2/2,            [-2.5, 2.5],      r"\frac{x^2}{2}",   BLUE),

        ]

        anims = []
        for f, xr, tex, color in items:
            g = ax_2.plot(f, x_range=xr, color=color, stroke_width=2.5)
            # 标签：取曲线右端点右侧 0.4 单位
            label = MathTex(tex, color=color, font_size=33).next_to(
                ax_2.c2p(xr[1], f(xr[1])), UP, buff=0
            ).shift(LEFT*.5)
            anims += [Create(g), Write(label)]
            func_group_2.add(g, label)

        # 3. 依次出现（可改 lag_ratio 调节奏）
        self.play(Succession(*anims), run_time=5)
        self.wait()

        self.play(
            func_group_2.animate.scale(0.65).shift(LEFT*7.7+DOWN*.5),
            Write(group_2_tex)
        )
        self.wait()

        #=========== Function graph -3 ===================

        group_3_tex=MathTex(
            r"e^x - 1 \sim \ln(1 + x) \sim x " ,           
            font_size=25,
            stroke_width=1
        ).to_edge(RIGHT,buff=0).shift(LEFT*2+UP*0.65)



        func_group_3=VGroup()
        ax_3 = self.make_axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],x_length=5, y_length=4
            ).shift(RIGHT*1.9).scale(1.2)
        self.play(Create(ax_3))  # 先放坐标系，不再动画
        func_group_3.add(ax_3)

        items = [            
            (lambda x: np.exp(x)-1,    [-3.3, 1.5],      r"e^x - 1",   YELLOW_D),
            (lambda x: np.log(1+x),       [-.9, 3.5],  r"\ln(1 + x)",   BLUE_D),
            (lambda x: x,                 [-3, 3],      r"x",           RED),

        ]

        anims = []
        for f, xr, tex, color in items:
            g = ax_3.plot(f, x_range=xr, color=color, stroke_width=2.5)
            # 标签：取曲线右端点右侧 0.4 单位
            label = MathTex(tex, color=color, font_size=30).next_to(
                ax_3.c2p(xr[1], f(xr[1])), UP, buff=0.2
            )
            anims += [Create(g), Write(label)]
            func_group_3.add(g, label)


        self.play(Succession(*anims), run_time=5)
        self.wait()
        
        self.play(
            func_group_3.animate.scale(0.57).shift(UP*1.7),
            Write(group_3_tex)
        )
        self.wait()




        #=========== Function graph -4 ===================

        group_4_tex=MathTex(
            r"a^x - 1 \sim x ln(a) " ,           
            font_size=25,
            stroke_width=1
        ).to_edge(DOWN,buff=0.33).shift(RIGHT*4.4)

        func_group_4=VGroup()
        
        ax_4 = self.make_axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],x_length=5.7, y_length=4
            ).to_edge(DOWN,buff=0).shift(RIGHT*3).scale(0.8)
        self.play(Create(ax_4))  # 先放坐标系，不再动画
        a=3
        items = [
            (lambda x: a**x-1,       [-3, 1.3],  r"a^x - 1 ",   BLUE_D),
            (lambda x: x*np.log(a),  [-2, 2.8],      r"x ln(a)",  RED),

        ]

        anims = []
        for f, xr, tex, color in items:
            g = ax_4.plot(f, x_range=xr, color=color, stroke_width=2.5)
            # 标签：取曲线右端点右侧 0.4 单位
            label = MathTex(tex, color=color, font_size=30).next_to(
                ax_4.c2p(xr[0], f(xr[0])), LEFT, buff=0.1
            )
            anims += [Create(g), Write(label)]
            

        self.play(Succession(*anims), run_time=5)
        self.wait()

        self.play(
            # func_group_4.animate.scale(0.7).shift(UP*1.1),
            Write(group_4_tex)
        )
        self.wait(3)



      

    def AddTitle(self,title="temp",font="UnVada" ,color:str="#FFFFFF",font_size=35,stroke_width=1.8):
        title=Text(
            title,  # 标题文本内容    
            font=font,  
            font_size=font_size, 
            stroke_width=stroke_width     
            
        ).to_corner(UL)
        
        title_back=Rectangle(
            width=title.width,
            height=title.height,
            fill_opacity=1,
            color=_color_1
        ).move_to(title.get_center()+LEFT*3+DOWN*.2)


        title_back_pos=title_back.animate.move_to(title.get_center()+DOWN*.2+RIGHT*.2)
        
        
        self.add(title_back)  

        return LaggedStart(
            Write(title),
            title_back_pos,
            lag_ratio=0.3,
        )


    
    def make_axes(self,x_range, y_range=(-0.4,3,1),x_length:float=1,y_length=1,include_numbers=True) -> Axes:
            return Axes(
                x_range=x_range,
                y_range=y_range,
                x_length=x_length,
                y_length=y_length,
                axis_config={
                    "color": WHITE,
                    "include_numbers": include_numbers,
                    "font_size": 22,
                    "tip_length": .1,
                    "tip_width": .1,
                },
                x_axis_config={
                    "include_ticks": True,
                    "include_tip": False }
            )
   

    def make_graphs(self,ax: Axes,lab_1,lab_2,f_x_range,g_x_range,
                        g_labOffsetMul,
                        f_labOffsetMul):
            """返回 (g_curve, f_curve, g_label, f_label)"""
            g = ax.plot(lambda x: x, color=_color_3, x_range=g_x_range)
            f = ax.plot(lambda x: np.sin(x), color=_color_4, x_range=f_x_range)

            g_lab = MathTex(
                lab_1, color=_color_3, font_size=30,
                ).move_to(g.get_center()+g_labOffsetMul)
    
            f_lab = MathTex(
                lab_2, color=_color_4, font_size=30,
                ).move_to(f.get_center()+f_labOffsetMul)  

            return VGroup(g, f, g_lab, f_lab)


class  SameorderInfitesimal(Scene):
    def construct(self):
        self.play(self.AddTitle("同阶无穷小"),font=font_2)
        self.wait(.7)


        #=========== Page-1=====================
        defint=MathTex(r"""
            \begin{aligned}
                &\text{定义：若 }\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = c \neq 0
                      \text{，则称} \alpha(x)\text{ 与 }\beta(x)\text{ 是同阶无穷小。} \\
                &\text{ 含义: }\alpha(x) \text{ 和 } \beta(x) \text{ 趋近于 0 的速度成比例，同步}\\
            \end{aligned}
            """,
            font_size=30,
            stroke_width=1
        ).to_edge(LEFT,buff=.7).shift(UP*1.7)

        self.play(Write(defint),rate_func=smooth)
        self.wait(1)

        example_title=Text(
            "例如：",
            font=font_2,  
            font_size=30, 
            stroke_width=1     
        ).next_to(defint,DOWN,buff=.7,aligned_edge=LEFT)
        example_title.add_background_rectangle(color=_color_3,buff=.08)

        self.play(Write(example_title),rate_func=smooth)
        

        exampl_1=MathTex(
            r"\text{当 } x \to 0 \text{时，} 2x \text{ 和 }x\text{是同阶无穷小量，}", 
            r"\text{因为：}\lim_{x\to 0}\frac{2x}{x} =2",
            font_size=33,
            stroke_width=1,
        ).next_to(example_title,RIGHT,buff=.4)

        self.play(Write(exampl_1))
        self.wait(1)

        rec_define=SurroundingRectangle(defint)
        example_1_copy=exampl_1.copy().to_corner(UL).shift(DOWN*2+RIGHT*.33)
        example_1_copy.add_background_rectangle(
            color=_color_3,buff=.08)
        self.play(
            defint.animate.next_to(
                example_1_copy,UP,buff=.4).shift(RIGHT*2).scale(.9),
                Create(rec_define),rec_define.animate.next_to(
                example_1_copy,UP,buff=.3).shift(RIGHT*2),
                ReplacementTransform(exampl_1,example_1_copy),
                FadeOut(example_title))
        self.wait(1)


        axes_1=Axes(
            x_range=[-1,5,1],
            y_range=[-1,4,1],
            x_length=5,
            y_length=4,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 22,
                "tip_length": .1,
                "tip_width": .1,
            },
            x_axis_config={
                
            }
        ).to_edge(DOWN,buff=.2)

        self.play(Create(axes_1),axes_1.animate.shift(LEFT*3))

        graph_1=axes_1.plot(lambda x: 2*x,color=_color_1,x_range=[-0.5,2])
        graph_2=axes_1.plot(lambda x: x,color=_color_4,x_range=[-0.8,3.5])

        self.play(Create(graph_1),Create(graph_2))

        # 3. 在 x=1 处画竖线
        x_val =ValueTracker(2)
        x0=x_val.get_value()
        
        vline_g =always_redraw(
            lambda: axes_1.get_vertical_line(
            axes_1.c2p(x_val.get_value(), x_val.get_value()), stroke_width=4, color=_color_4)
        )
        vline_f =always_redraw(
            lambda: DashedLine(
            axes_1.c2p(x_val.get_value(), x_val.get_value()), 
            axes_1.c2p(x_val.get_value(), 2*x_val.get_value()),
            stroke_width=4, color=_color_1)
        )
        vline_f_shadow =always_redraw(
            lambda: axes_1.get_vertical_line(            
            axes_1.c2p(x_val.get_value(), 2*x_val.get_value()),
            stroke_width=4, color=_color_1)
        )

        

        # 5. 两条大括号：标注 2x 与 x 的「高差」
        brace_g = Brace(
            Line(axes_1.c2p(x0, 0), axes_1.c2p(x0, x0)), 
            direction=RIGHT, color=BLUE)
        brace_f = Brace(
            Line(axes_1.c2p(x0, 0), axes_1.c2p(x0, 2*x0)), 
            direction=RIGHT, color=GREEN)
        
        label_g = MathTex("2x", color=BLUE).next_to(brace_g, RIGHT, buff=0.1)
        label_f = MathTex("x", color=GREEN).next_to(brace_f, RIGHT, buff=0.1)

        dot_x =always_redraw(lambda: Dot(axes_1.c2p(x_val.get_value(), 0), color=WHITE))
        dot_g =always_redraw(lambda: Dot(axes_1.c2p(x_val.get_value(), x_val.get_value()), color=_color_4))
        dot_f =always_redraw(lambda:Dot(axes_1.c2p(x_val.get_value(), 2*x_val.get_value()), color=BLUE))

        
        
        self.play(
            Succession(Create(dot_x), Create(vline_g),Create(dot_g)),
            Succession(Create(dot_f), Create(vline_f)),run_time=.5)
        

        vline_g_copy=vline_g.copy()
        vline_f_copy=vline_f_shadow.copy()
        vlineGrupe_1=VGroup(vline_g_copy,vline_f_copy)
        self.play(Create(vline_g_copy),vline_g_copy.animate.shift(RIGHT*8.8))
        self.play(Create(vline_f_copy),vline_f_copy.animate.shift(RIGHT*8))

        

        self.play(x_val.animate.set_value(1),run_time=2)

        vline_g_copy=vline_g.copy()
        vline_f_copy=vline_f_shadow.copy()
        vlineGrupe_2=VGroup(vline_g_copy,vline_f_copy)
        self.play(Create(vline_g_copy),vline_g_copy.animate.shift(RIGHT*7))
        self.play(Create(vline_f_copy),vline_f_copy.animate.shift(RIGHT*6.5))
        
       

        self.play(x_val.animate.set_value(.4),run_time=2)

        vline_g_copy=vline_g.copy()
        vline_f_copy=vline_f_shadow.copy()
        vlineGrupe_3=VGroup(vline_g_copy,vline_f_copy)
        self.play(Create(vline_g_copy),vline_g_copy.animate.shift(RIGHT*5.2))
        self.play(Create(vline_f_copy),vline_f_copy.animate.shift(RIGHT*4.8))

        for grup in [vlineGrupe_1,vlineGrupe_2,vlineGrupe_3]:
            self.play(
                Circumscribe(grup, buff=0.2, color=YELLOW),
            )
       
        
        

        self.wait() 



    def AddTitle(self,title="temp",font=font_2 ,color:str="#FFFFFF",font_size=35,stroke_width=1.8):
        title=Text(
            title,  # 标题文本内容    
            font=font,  
            font_size=font_size, 
            stroke_width=stroke_width     
            
        ).to_corner(UL)
        
        title_back=Rectangle(
            width=title.width,
            height=title.height,
            fill_opacity=1,
            color=_color_1
        ).move_to(title.get_center()+LEFT*3+DOWN*.2)


        title_back_pos=title_back.animate.move_to(title.get_center()+DOWN*.2+RIGHT*.2)
        
        
        self.add(title_back)  

        return LaggedStart(
            Write(title),
            title_back_pos,
            lag_ratio=0.3,
        )


class LoworderInfinitesimal(Scene):
    def construct(self):
        self.play(self.AddTitle("低阶无穷小"))
        self.wait(.7)

        #=========== Page-1=====================
        defint=MathTex(r"""
            \begin{aligned}
                &\text{定义：若 }\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = \infty
                      \text{，则称} \alpha(x)\text{ 是比 }\beta(x)\text{ 低阶的无穷小} \\
                &\text{ 含义: }\alpha(x) \text{ 趋近于 0 的速度比 } \beta(x) \text{ 慢}\\
                &\text{ 记作：} \alpha(x) = o(\beta(x)) \text{ (当 } x \to a\text{，且}\alpha(x)\neq 0)\\
            \end{aligned}
            """,
            font_size=30,
            stroke_width=1
        ).to_edge(LEFT,buff=.7).shift(UP*1.7)

        self.play(Write(defint),rate_func=smooth)
        self.wait(1)

        example_title=Text(
            "例如：",
            font=font_2,  
            font_size=30, 
            stroke_width=1     
        ).next_to(defint,DOWN,buff=.7,aligned_edge=LEFT)
        example_title.add_background_rectangle(color=_color_3,buff=.08)

        self.play(Write(example_title),rate_func=smooth)
        

        exampl_1=MathTex(
            r"\text{当 } x \to 0 \text{时，} x \text{ 是比 }x^2\text{低阶的无穷小}", 
            r"\text{因为：}\lim_{x\to 0}\frac{x}{x^2}=\lim_{x\to 0}\frac{1}{x} = \infty",
            font_size=33,
            stroke_width=1,
        ).next_to(example_title,RIGHT,buff=.4)

        self.play(Write(exampl_1))
        self.wait(1.5)

        self.play(*{FadeOut(mob) for mob in self.mobjects})
        
        
    def AddTitle(self,title="temp",font=font_2 ,color:str="#FFFFFF",font_size=35,stroke_width=1.8):
        title=Text(
            title,  # 标题文本内容    
            font=font,  
            font_size=font_size, 
            stroke_width=stroke_width     
            
        ).to_corner(UL)
        
        title_back=Rectangle(
            width=title.width,
            height=title.height,
            fill_opacity=1,
            color=_color_1
        ).move_to(title.get_center()+LEFT*3+DOWN*.2)


        title_back_pos=title_back.animate.move_to(title.get_center()+DOWN*.2+RIGHT*.2)
        
        
        self.add(title_back)  

        return LaggedStart(
            Write(title),
            title_back_pos,
            lag_ratio=0.3,
        )
    

class KorderInfinitesimal(Scene):
    def construct(self):
        self.play(self.AddTitle("k 阶无穷小"))
        self.wait(.7)

        #=========== Page-1=====================
        defint=MathTex(r"""
            \begin{aligned}
                &\text{定义：若存在常数 }k > 0\text{ 使得 }\lim_{x \to a} 
                       \frac{\alpha(x)}{|\beta(x)|^k} = c \; (c\ne 0)
                      \text{，那么} \alpha(x)\text{ 是关于 }\beta(x)\text{ 的 k 阶无穷小} \\
                &\text{ 含义: }\alpha(x) \text{ 趋近于0的速度与 } \beta(x) \text{ 的 k 次方相当}\\
                &\text{ 记作：} \alpha(x)= o(\beta(x)^k),x\rightarrow a\\
            \end{aligned}
            """,
            font_size=30,
            stroke_width=1
        ).to_edge(LEFT,buff=.7).shift(UP*1.7)

        self.play(Write(defint),rate_func=smooth)
        self.wait(1)

        example_title=Text(
            "例如：",
            font=font_2,  
            font_size=30, 
            stroke_width=1     
        ).next_to(defint,DOWN,buff=.7,aligned_edge=LEFT)
        example_title.add_background_rectangle(color=_color_3,buff=.08)

        self.play(Write(example_title),rate_func=smooth)
        

        exampl_1=MathTex(
            r"\text{当 } x \to 0 \text{时，} 1 - cosx \text{ 是关于 }x \text{ 的 2 阶无穷小}", 
            r"\text{，因为：}\lim_{x\to 0}\frac{1-cosx}{x^2} =\frac{1}{2}",
            font_size=33,
            stroke_width=1,
        ).next_to(example_title,RIGHT,buff=.4)

        self.play(Write(exampl_1))
        self.wait(1.5)
        

    def AddTitle(self,title="temp",font=font_2 ,color:str="#FFFFFF",font_size=35,stroke_width=1.8):
        title=Text(
            title,  # 标题文本内容    
            font=font,  
            font_size=font_size, 
            stroke_width=stroke_width     
            
        ).to_corner(UL)
        
        title_back=Rectangle(
            width=title.width,
            height=title.height,
            fill_opacity=1,
            color=_color_1
        ).move_to(title.get_center()+LEFT*3+DOWN*.2)


        title_back_pos=title_back.animate.move_to(title.get_center()+DOWN*.2+RIGHT*.2)
        
        
        self.add(title_back)  

        return LaggedStart(
            Write(title),
            title_back_pos,
            lag_ratio=0.3,
        )





class Equivalent_infinitesimal_substitution(Scene):
    def construct(self):
        self.play(self.AddTitle("等价无穷小替换求极限"))
        self.wait(.7)

        exa_title = Text("计算示例: ", 
                     font=font_2,font_size=30, color=WHITE).shift(LEFT*5+UP*1.7)
        exa_title.add_background_rectangle(color=_color_3,buff=.08)
        limit_expr = MathTex(r"\lim_{x \to 0}\frac{x\ln(1+x)}{1-\cos{x}}", 
                             stroke_width=1,font_size=28)
        limit_expr.next_to(exa_title, RIGHT)
        title_group = VGroup(exa_title, limit_expr)
        self.play(Write(title_group))
        self.wait(1)

        step1 = Text("Step1 判断等价无穷小", font_size=25, color=RED,font=font_2)
        step1.next_to(exa_title,DOWN,buff=.5,aligned_edge=LEFT)
        
        equiv_group = VGroup(
            MathTex(r"\ln(1+x) \sim x", font_size=22,stroke_width=1),
            MathTex(r"1-\cos{x} \sim \frac{1}{2}x^2", font_size=22,stroke_width=1)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        equiv_group.next_to(step1, DOWN, aligned_edge=LEFT, buff=0.3).shift(RIGHT*0.2)
        
        self.play(Write(step1))
        self.play(LaggedStartMap(Write, equiv_group, lag_ratio=0.4))
        self.wait(1)

        step2 = Text("Step2 代入替换", font_size=25, color=RED,font=font_2)
        step2.next_to(step1, RIGHT,  buff=1)
        
        substitution = MathTex(
            r"\frac{x\ln(1+x)}{1-\cos{x}} = \frac{x \cdot x}{\frac{1}{2}x^2}",
            font_size=27, stroke_width=1
        )
        substitution.next_to(step2, DOWN, aligned_edge=LEFT, buff=0.4).shift(RIGHT*.2)
        
        self.play(Write(step2))
        self.play(Write(substitution))
        self.wait(1)

        step3 = Text("Step3 简化计算", font_size=25, color=RED,font=font_2)
        step3.next_to(step2, RIGHT, buff=1.5)
        
        simplifications = VGroup(
            MathTex(r"\lim_{x \to 0} \frac{x\ln(1+x)}{1-\cos{x}} = \
                    \lim_{x \to 0}\frac{x ^2}{\frac{1}{2}x^2}", font_size=26,stroke_width=1),
            MathTex(r"= \frac{1}{\frac{1}{2}}=2", font_size=26,stroke_width=1),
           
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        simplifications.next_to(step3, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(Write(step3))
        for step in simplifications:
            self.play(Write(step))
            self.wait(0.5)
        
        self.wait(1)

        final_answer = MathTex(
            r"\lim_{x \to 0}\frac{x\ln(1+x)}{1-\cos{x}} = 2",
            font_size=32,
            color=_color_8,
            stroke_width=1
        )
        final_answer.to_edge(DOWN).shift(UP * .8)
        
        answer_box = SurroundingRectangle(final_answer, color=ORANGE, buff=0.3, corner_radius=0.1)
        
        self.play(Write(final_answer),Create(answer_box))
        
        
        self.wait(1)

        self.play(FadeOut(*self.mobjects))
        
        


        title_2 = Text("为什么可以替换？", font_size=33,font=font_2
                       ).to_corner(UL)
        title_2.add_background_rectangle(color=_color_3,buff=.08)
        self.play(Write(title_2))
        self.wait(1)

        p1 = MarkupText("想象一下，当 x→0 时，<b>sin x</b> 和 x 都在奔向 0。", 
                        font_size=28,font=font_2)
        p2 = MarkupText("虽然它们奔向 0 的“路径”不同，但它们的“速度”和“姿态”在终点附近几乎一模一样。",
                        font_size=28,font=font_2)
        p3 = MarkupText("等价无穷小的本质是：在 <b>x→0</b> 的过程中，两个无穷小量的“差异”是更高阶的，可以忽略不计。", 
                        font_size=28,font=font_2)
        
        lim_formula = VGroup(
            Text(
            "等价无穷小必然满足：",font=font_2,font_size=27,color=YELLOW
        ),        
            MathTex(
            r"\text{}\lim_{x\to 0}\frac{f(x)}{g(x)}=1", font_size=32,
            stroke_width=1).set_color(YELLOW)
        ).arrange(RIGHT)
        example = VGroup(
            Text("举个例子:",font=font_2,font_size=27,color=YELLOW),
        
            MathTex(
            r"\lim_{x\to 0}\frac{\sin x}{x}=1\quad\Rightarrow\quad\sin x\sim x", 
            font_size=32,stroke_width=1).set_color(YELLOW)
        ).arrange(RIGHT)
        p4 = MarkupText(
            "在求一个复杂的极限时，如果其中某个因子是 <b>sin x</b>，我们就可以大胆地把它换成 <b>x</b>，", 
            font_size=28,font=font_2)
        p5 = MarkupText(
            "因为它们的“比值”在极限状态下是 1，替换后不会改变整个极限的值。", 
            font_size=28,font=font_2)


        expalin_1 = VGroup(
            p1, p2, p3, lim_formula, example, p4, p5
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        # 4. 逐句出现
        for line in expalin_1[:4]:
            self.play(Write(line), run_time=0.5)
        self.wait(1.5)

        for line in expalin_1[4:]:
            self.play(Write(line), run_time=0.5)

        self.wait(2.5)
        self.play(FadeOut(*self.mobjects))

        self.play(self.AddTitle("常用等价无穷小替换",font_size=35,font=font_2))

        condition_1=Text(
            "当 x → 0 时",font=font_2,font_size=23).to_edge(UP).shift(LEFT*2.2+DOWN*.4)
        self.play(Write(condition_1))
        lines = VGroup(
            MathTex(r"\sin x \sim x", font_size=36,stroke_width=1),
            MathTex(r"\tan x \sim x", font_size=36,stroke_width=1),
            MathTex(r"\arcsin x \sim x", font_size=36,stroke_width=1),
            MathTex(r"\arctan x \sim x", font_size=36,stroke_width=1),
            MathTex(r"1-\cos x \sim \dfrac{x^{2}}{2}", font_size=36,stroke_width=1),
            MathTex(r"\ln(1+x) \sim x", font_size=36,stroke_width=1),
            MathTex(r"\mathrm{e}^{x}-1 \sim x", font_size=36,stroke_width=1),
            MathTex(r"a^{x}-1 \sim x\ln a", font_size=36,stroke_width=1),
            MathTex(r"(1+x)^{\alpha}-1 \sim \alpha x", font_size=36,stroke_width=1),            
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(LEFT).shift(DOWN*.5+RIGHT*.2)

        # 逐句淡入
        self.play(LaggedStartMap(Write, lines, lag_ratio=0.4), run_time=3)
        self.wait()

        emphasize_1=Paragraph(
            "需要注意的是，这里面的 x 应该看成一个整体",
            "该 整体→0 的情况下，都能替换",
            line_spacing=1,font=font_2,font_size=33,color=_color_3,weight=BOLD
            ).shift(RIGHT*2.2+DOWN*.4)
        self.play(Write(emphasize_1))
        self.wait(2)
        self.play(Uncreate(emphasize_1))

        example_2=Text(
            "比如：",font=font_2,font_size=30
            ).next_to(condition_1,DOWN).add_background_rectangle(color=_color_3,buff=.08)
        self.play(Write(example_2))

        
        lim = MathTex(r"\lim_{x\to 0}\frac{\sin 3x}{1-\cos 2x}",
                       font_size=40).shift(UP*2)


        # 2. 高亮「整体」并写出口诀
        box1 = SurroundingRectangle(lim[0][9:11], color=YELLOW)   # sin(3x)
        box2 = SurroundingRectangle(lim[0][17:20], color=TEAL)  # 1-cos(2x)
        tip = Text("整体 → 0", font_size=25,font=font_2).next_to(lim, DOWN, buff=0.3)

        # 3. 替换过程（分步）
        step1 = MathTex(r"{=}\lim_{x\to 0}\frac{3x}{\frac{1}{2}(2x)^2}", font_size=41)
        step2 = MathTex(r"=\lim_{x\to 0}\frac{3x}{2x^2}= \infty", font_size=41)
        step2.next_to(step1,DOWN,aligned_edge=LEFT)
        # # 4. 竖排
        box3=SurroundingRectangle(lines[0],color=YELLOW)
        box4=SurroundingRectangle(lines[4],color=TEAL)
        # 5. 动画
        self.play(Write(lim))
        self.play(Create(box1), Create(box3))
        self.play(Create(box2), Create(box4))
        self.play(Write(tip))
        self.play(Write(step1))
        self.play(Write(step2))
        self.wait()
        so_tex=Text("So",font=font_2,font_size=70,color=_color_4)
        self.play(Create(so_tex.shift(RIGHT*4)))
        
        tempGroup=VGroup(lim,box1,box2,box3,box4,tip,step1,step2,example_2,so_tex)
        self.play(LaggedStart(tempGroup.animate.scale(0.5),FadeOut(tempGroup),
                lag_ratio=0.3))
        
        lines = VGroup(
            MathTex(r"\sin \text{( )} \sim \text{( )}", font_size=36),
            MathTex(r"\tan \text{( )} \sim \text{( )}", font_size=36),
            MathTex(r"\arcsin \text{( )} \sim \text{( )}", font_size=36),
            MathTex(r"\arctan \text{( )} \sim \text{( )}", font_size=36),
            MathTex(r"1-\cos \text{( )} \sim \dfrac{\text{( )}^{2}}{2}", font_size=36),
            MathTex(r"\ln(1+\text{( )}) \sim \text{( )}", font_size=36),
            MathTex(r"\mathrm{e}^{\text{( )}}-1 \sim \text{( )}", font_size=36),
            MathTex(r"a^{\text{( )}}-1 \sim \text{( )}\ln a", font_size=36),
            MathTex(r"(1+\text{( )})^{\alpha}-1 \sim \alpha \text{( )}", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35
                  ).shift(DOWN * 0.5 + RIGHT * 0.5).scale(0.84)

        # 逐句淡入
        self.play(LaggedStartMap(Write, lines, lag_ratio=0.15), run_time=4)
        self.wait()

        self.play(FadeOut(*self.mobjects))        
        
        
        
        #=================exampale-1=================
        
        self.play(self.AddTitle("例题 1",font_size=35,font=font_2))

        limit_expr = MathTex(
            r"\lim_{x\to 0}(1+3x)^{\frac{2}{\sin x}}", font_size=36,stroke_width=1.8)
        limit_expr.to_edge(UP, buff=1.3).shift(LEFT*4.1)

        # 步骤1：识别1^∞型极限
        step1 = Text("步骤1: 识别极限类型", font_size=30, color=_color_1,font=font_2)
        step1.next_to(limit_expr, DOWN, buff=0.5, aligned_edge=LEFT)
        
        type_text = MathTex(
            r"1^\infty \text{型极限}",
            font_size=33,
            color=YELLOW
        )
        type_text.next_to(step1, RIGHT, aligned_edge=DOWN, buff=0.3)
        
        step1_rec1=SurroundingRectangle(
            limit_expr[0][6:12],color=RED_B,buff=.05)
        step1_rec2=SurroundingRectangle(
            limit_expr[0][12:18],color=GREEN_D,buff=.05)


        self.play(Write(limit_expr))
        self.wait(1)
        
        self.play(Write(step1))
        self.play(Create(step1_rec1),Create(step1_rec2))
        self.wait(1)
        self.play(Write(type_text),Uncreate(step1_rec1),Uncreate(step1_rec2))
        self.wait(1)

         # 步骤2：使用重要极限公式
        step2 = Text("步骤2: 使用重要极限公式", font_size=30,font=font_2, color=_color_1)
        step2.next_to(step1, DOWN, buff=0.5, aligned_edge=LEFT)
        
        important_limit = MathTex(
            r"\lim_{x\to 0}(1+x)^{\frac{1}{x}} = e",
            font_size=33,
            color=YELLOW
        )
        important_limit.next_to(step2, RIGHT, aligned_edge=DOWN, buff=0.3)
        
        self.play(Write(step2))
        self.play(Write(important_limit))
        self.wait(1)

         # 步骤3：变形原式
        step3 = Text("步骤3: 变形原式", font_size=30,font=font_2, color=_color_1)
        step3.next_to(step2, DOWN, buff=0.5, aligned_edge=LEFT)
        
        # 将原式变形为指数形式
        transformation1 = MathTex(
            r"(1+3x)^{\frac{2}{\sin x}} = e^{\ln\left[(1+3x)^{\frac{2}{\sin x}}\right]}",
            font_size=33,
            color=YELLOW
        )
        transformation1.next_to(step3, RIGHT, aligned_edge=DOWN, buff=0.3)
        
        transformation2 = MathTex(
            r"= e^{\frac{2}{\sin x} \cdot \ln(1+3x)}",
            font_size=33,
            color=YELLOW        
        )
        transformation2.next_to(transformation1, RIGHT, aligned_edge=DOWN, buff=0.2)
        
        self.play(Write(step3))
        self.play(Write(transformation1))
        self.wait(.5)
        self.play(Write(transformation2))
        self.wait(1)

        # 步骤3：变形原式  explain
        step3_explain = Text(
            "任何正数都能写成 e 的幂:", font_size=27,font=font_2, color=_color_8
        )
        step3_explain.next_to(transformation1, DOWN, buff=0.5, aligned_edge=LEFT)
        form1  = MathTex(r"A = e^{\ln A}>0", font_size=27,stroke_width=1
                         ).next_to(step3_explain, RIGHT, aligned_edge=DOWN, buff=0.3)
        step3_explain_2 = Text(
            "对数幂规则:", font_size=27,font=font_2, color=_color_8
        ).next_to(step3_explain,DOWN, buff=0.5, aligned_edge=LEFT)
        form2  = MathTex(r"\log_AB^c = c\log_A B}", font_size=27,stroke_width=1
                         ).next_to(step3_explain_2, RIGHT, aligned_edge=DOWN, buff=0.3)
        
        self.play(Succession(Write(step3_explain),Write(form1)))
        self.wait(.5)
        self.play(Succession(Write(step3_explain_2),Write(form2)))
        self.wait(1)
        
        self.play(FadeOut(step3_explain),FadeOut(form1),FadeOut(step3_explain_2),FadeOut(form2))
       

       # 步骤4：计算指数部分的极限
        step4 = Text("步骤4: 计算指数部分的极限", font_size=30, font=font_2,color=_color_1)
        step4.next_to(step3, DOWN, buff=0.5, aligned_edge=LEFT)
        
        exponent_limit = MathTex(
            r"\lim_{x\to 0} \frac{2}{\sin x} \cdot \ln(1+3x)",
            font_size=33,
            color=YELLOW
        )
        exponent_limit.next_to(step4, RIGHT, buff=0.3)
        
        self.play(Write(step4))
        self.play(Write(exponent_limit))
        self.wait(1)
        
        # 使用等价无穷小
        equiv_text = Text("使用等价无穷小:", font_size=27, font=font_2,color=_color_1)
        equiv_text.next_to(step4, DOWN, buff=0.3, aligned_edge=RIGHT)
        
        equiv_group = VGroup(
            MathTex(r"\ln(1+3x) \sim 3x \quad (x \to 0)",stroke_width=1, font_size=25),
            MathTex(r"\sin x \sim x \quad (x \to 0)",stroke_width=1, font_size=25)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        equiv_group.next_to(equiv_text, RIGHT, aligned_edge=UP, buff=0.2)
        
        self.play(Write(equiv_text))
        self.play(LaggedStartMap(Write, equiv_group, lag_ratio=0.3))
        self.wait(1)
        self.play(FadeOut(equiv_text), FadeOut(equiv_group))
        
         # 代入等价无穷小
        substitution = MathTex(
            r"= \lim_{x\to 0} \frac{2}{x} \cdot 3x",
            font_size=33,
            color=YELLOW
        )
        substitution.next_to(exponent_limit, RIGHT, buff=0.3)
        
        simplification = MathTex(
            r"= \lim_{x\to 0} 6 = 6",
            font_size=33,
            color=YELLOW
        )
        simplification.next_to(substitution, RIGHT, aligned_edge=DOWN, buff=0.2)
        
        self.play(Write(substitution))
        self.wait(1)
        self.play(Write(simplification))
        self.wait(1)

         # 步骤5：得到最终结果
        step5 = Text("步骤5: 得到最终结果", font_size=33,font=font_2, color=_color_1)
        step5.next_to(step4, DOWN, buff=0.5, aligned_edge=LEFT)
        
        final_result = MathTex(
            r"\lim_{x\to 0}(1+3x)^{\frac{2}{\sin x}} = e^6",
            font_size=33,
            color=YELLOW
        )
        final_result.next_to(step5, RIGHT, aligned_edge=DOWN, buff=0.3).shift(DOWN*.1)
        
        self.play(Write(step5))
        self.play(Write(final_result))       
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

        #===============example-2======================
        self.play(self.AddTitle("例题 2"))            
        limit_expr = MathTex(
            r"\lim_{x\to +\infty}\ln{(1+2^x)}\ln\left(1+\frac{3}{x}\right)", 
            font_size=32,stroke_width=1)
        limit_expr.to_edge(UP, buff=1.3).shift(LEFT*4.1)
        
       
        self.play(Write(limit_expr))
        self.wait(1)

        # 步骤1：分析极限类型
        step1 = Text("步骤1: 分析极限类型", font_size=30,font=font_2, color=_color_8)
        step1.next_to(limit_expr, DOWN, buff=0.5, aligned_edge=LEFT)
        
        analysis = VGroup(
            MathTex(r"x \to +\infty \Rightarrow 2^x \to +\infty", 
                    font_size=29,stroke_width=1),
            MathTex(r"\Rightarrow \ln(1+2^x) \to +\infty", 
                    font_size=29,stroke_width=1),
            MathTex(r"\frac{3}{x} \to 0 \Rightarrow \ln\left(1+\frac{3}{x}\right) \to 0",
                    font_size=22,stroke_width=1),
            MathTex(r"\infty \cdot 0 \text{ 型极限}", 
                    font_size=29,stroke_width=1, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        analysis.next_to(step1, RIGHT, aligned_edge=UP, buff=0.3)

        analysis_copy=analysis[3].copy().next_to(step1, RIGHT, aligned_edge=DOWN, buff=0.3)
        
        self.play(Write(step1))
        self.play(LaggedStartMap(Write, analysis, lag_ratio=0.3))
        self.wait(.7)
        self.play(ReplacementTransform(analysis,analysis_copy))
        self.wait(1)


         # 步骤2：处理∞·0型极限
        step2 = Text("步骤2: 处理∞·0型极限", font_size=30,font=font_2, color=_color_8)
        step2.next_to(step1, DOWN, buff=0.5, aligned_edge=LEFT)
        
        transform_text = Text(
            r"一般转化为 0/0 或 ∞/∞ 再处理",
            font_size=25,
            font=font_2,
            color=YELLOW
        )
        transform_text.next_to(step2, RIGHT, aligned_edge=DOWN, buff=0.3)
        
        self.play(Write(step2))
        self.play(Write(transform_text))
        self.wait(1)
        
        # 变形为分式
        transformation = MathTex(
            r"\ln(1+2^x)\ln\left(1+\frac{3}{x}\right) = \frac{\ln(1+2^x)}{\frac{1}{\ln\left(1+\frac{3}{x}\right)}}",
            font_size=27,
            stroke_width=1,
        )
        transformation.next_to(transform_text, RIGHT, buff=0.3)
        
        self.play(Write(transformation))
        self.wait(1)
        
        # 更好的变形方法
        better_transform = MathTex(
            r"\text{或：}  = \frac{\ln\left(1+\frac{3}{x}\right)}{\frac{1}{\ln(1+2^x)}}",
            font_size=25,
            stroke_width=1,
        )
        better_transform.next_to(transformation, DOWN, aligned_edge=RIGHT, buff=0.3)
        
        self.play(Write(better_transform))
        self.wait(1)


        # 步骤3：使用等价无穷小
        step3 = Text("步骤3: 使用等价替换", font_size=30,font=font_2, color=_color_8)
        step3.next_to(step2, DOWN, buff=2.1, aligned_edge=LEFT)       

        equiv_text =VGroup( MathTex(
            r"x \to +\infty",
            font_size=29,
            color=YELLOW,
            stroke_width=1),
            Text("时的重要近似：",font=font_2,font_size=25,color=YELLOW)
        ).arrange(RIGHT,buff=0.1,aligned_edge=DOWN
                  ).next_to(step2,DOWN,aligned_edge=LEFT, buff=0.5)
        
        equiv_group = VGroup(
            MathTex(r"\ln(1+2^x) \sim \ln(2^x) = x\ln 2", 
                    font_size=25,stroke_width=1),
            MathTex(r"\ln\left(1+\frac{3}{x}\right) \sim \frac{3}{x}", 
                    font_size=25,stroke_width=1)
        ).arrange(DOWN, aligned_edge=LEFT)
        equiv_group.next_to(equiv_text, RIGHT, aligned_edge=UP, buff=0.3)
        
        self.play(Write(step3))
        self.play(Write(equiv_text))
        self.play(LaggedStartMap(Write, equiv_group, lag_ratio=0.3))
        self.wait(2)

        # 步骤4：代入近似
        step4 = Text("步骤3: 代入近似计算", font_size=24, color=_color_8)
        step4.next_to(equiv_group, DOWN, buff=0.5, aligned_edge=LEFT)
        
        substitution = MathTex(
            r"\ln(1+2^x)\ln\left(1+\frac{3}{x}\right) \sim (x\ln 2) \cdot \left(\frac{3}{x}\right)",
            font_size=28,
            color=YELLOW,
            stroke_width=1
        )
        substitution.next_to(step3, RIGHT, buff=0.3)
        
        simplification = MathTex(
            r"= 3\ln 2",
            font_size=27,
            color=YELLOW,
            stroke_width=1
        )
        simplification.next_to(substitution, RIGHT, buff=0.2)
        
        # self.play(Write(step4))
        self.play(Write(substitution))
        # self.wait(1)
        self.play(Write(simplification))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))    





    def AddTitle(self,title="temp",font=font_2 ,color:str=_color_1,font_size=35,stroke_width=1.8):
        title=Text(
            title,  # 标题文本内容    
            font=font,  
            font_size=font_size, 
            stroke_width=stroke_width     
            
        ).to_corner(UL)
        
        title_back=Rectangle(
            width=title.width,
            height=title.height,
            fill_opacity=1,
            color=color
        ).move_to(title.get_center()+LEFT*3+DOWN*.2)


        title_back_pos=title_back.animate.move_to(title.get_center()+DOWN*.2+RIGHT*.2)
        
        
        self.add(title_back)  

        return LaggedStart(
            Write(title),
            title_back_pos,
            lag_ratio=0.3,
        )
    

class GeneralLimitMethod(Scene):
    def construct(self):
        self.play(self.AddTitle("函数极限",font_size=41))
        self.wait(.7)

        contect=Text("函数极限是非常重要的内容，是考察的重点！",
                     font_size=40,font=font_8,color=_color_4).shift(UP)
        
        self.play(Write(contect))
        self.wait(.7)
        self.play(FadeOut(contect))

        tex_list = [
            r"\lim_{x\to 0}\frac{\tan x-\sin x}{x^3}",
            r"\lim_{x\to 0^+}(\sin x)^x",
            r"\lim_{x\to +\infty}\left(1+\frac{1}{x}\right)^{x^2}",
            r"\lim_{x\to 0}\frac{\ln(1+x^2)}{1-\cos x}",
            r"\lim_{x\to 0}\frac{e^x-e^{-x}-2x}{x-\sin x}",
            r"\lim_{x\to 0^+}x^{\sin x}",
            r"\lim_{x\to +\infty}\frac{\ln(1+e^x)}{x}",
            r"\lim_{x\to 0}(1+3x)^{\frac{2}{\sin x}}",
            r"\lim_{x\to 0}\frac{\sqrt{1+x}-\sqrt{1-x}}{x}",
            r"\lim_{x\to +\infty}\left(\frac{x^2+1}{x^2-1}\right)^{x^2}",
            r"\lim_{x\to 0}\frac{\ln(1+x^2)}{1-\cos x}",
            r"\lim_{x\to 0}\frac{e^x-e^{-x}-2x}{x-\sin x}",
            r"\lim_{x\to 0^+}x^{\sin x}",
            r"\lim_{x\to +\infty}\frac{\ln(1+e^x)}{x}"
        ]

        # 随机种子（固定，方便复现）
        # np.random.seed(42)
        # np.random.seed(4)

        # 已占位置（简单半径避让）
        occupied = []

        def random_pos():
            while True:
                # 避开左上角 ±1.5 区域
                x = np.random.uniform(-5.8, 7)
                y = np.random.uniform(-3, 3)
                if x < -1.5 and y > 1.5:
                    continue
                # 简单半径重叠检测
                if all((x - ox)**2 + (y - oy)**2 > 1.2**2 for ox, oy in occupied):
                    occupied.append((x, y))
                    return np.array([x, y, 0])

        color_pool = [RED, ORANGE, YELLOW, TEAL, BLUE, PINK, GOLD, WHITE, LIGHT_BROWN]

        # 生成题目
        mobs = VGroup()
        for tex in tex_list:
            eq = MathTex(
                tex,
                font_size=30,
                stroke_width=1,
                # color=np.random.choice(color_pool),
            ).scale(np.random.uniform(0.8, 1.0)).move_to(random_pos())
            mobs.add(eq)


        # 逐题淡入（可调 lag）
        self.play(LaggedStartMap(Write, mobs, lag_ratio=0.4), run_time=5)
        self.wait()


        self.play(LaggedStartMap(FadeOut, mobs, lag_ratio=0.3), run_time=5)

        #=============Page 2================
        title_1=Text(
            "极限运算法则",font_size=29,font=font_2,
        ).to_corner(UL).shift(RIGHT*2.1+DOWN*.4)
        title_1.add_background_rectangle(color=_color_4)
        self.play(Create(title_1))
        self.wait(.7)

        # 创建法则列表
        rules = [
            ("和/差法则", r"\lim[f(x) \pm g(x)] = \lim f(x) \pm \lim g(x)", r"\lim f(x), \lim g(x)\text{存在}"),
            ("积法则", r"\lim[f(x) \cdot g(x)] = \lim f(x) \cdot \lim g(x)", r"\lim f(x), \lim g(x)\text{存在}"),
            ("商法则", r"\lim\left[\frac{f(x)}{g(x)}\right] = \frac{\lim f(x)}{\lim g(x)}", r"\lim f(x), \lim g(x)\text{存在}, \lim g(x) \neq 0"),
            ("常数倍法则", r"\lim[c \cdot f(x)] = c \cdot \lim f(x)", r"\lim f(x)\text{存在}, c\text{为常数}"),
            ("幂法则", r"\lim[f(x)]^n = [\lim f(x)]^n", r"\lim f(x)\text{存在}, n\in\mathbb{N}^+"),
            ("根式法则", r"\lim[\sqrt[n]{f(x)}] = \sqrt[n]{\lim f(x)}", r"\lim f(x)\text{存在且非负（n为偶数时）}"),
            ("复合函数法则", r"\lim f(g(x)) = f(\lim g(x))", r"\lim g(x)=L\text{存在}, f\text{在}L\text{处连续}"),
        ]
        
        # 创建规则组
        rule_group = VGroup()
        for i, (name, expr, condition) in enumerate(rules):
            rule_box = VGroup()
            
            # 名称
            name_text = Text(name, font_size=27, font=font_2,color=YELLOW)
            
            # 表达式
            expr_tex = MathTex(expr, font_size=28,stroke_width=1)
            
            # 条件
            cond_tex = MathTex(condition, font_size=23, color=_color_8,stroke_width=1)
            
            # 排列
            rule_box = VGroup(name_text, expr_tex, cond_tex)
            rule_box.arrange(RIGHT, buff=0.2)
            
            
            rule_group.add(rule_box)
        
        # 排列规则
        rule_group.arrange(DOWN,aligned_edge=LEFT,buff=.3)
      
        
        
        self.play(LaggedStartMap(Write,rule_group,lag_ratio=0.3),run_time=5)
        self.wait(1.5)
        
        # 强调前提条件
        reminder_text = Text("重要提醒：所有法则的前提是相关极限存在！", 
                           font_size=30,font=font_2, color=RED,weight=BOLD)
        reminder_text.to_edge(DOWN)
        
        self.play(Write(reminder_text))
        self.wait(1)
        self.play(LaggedStartMap(FadeOut,[reminder_text,rule_group,title_1],lag_ratio=0.3),run_time=2)

        #=============Page 3================
        title_2=Text(
            "极限存在准则",font_size=29,font=font_2,
        ).to_corner(UL).shift(RIGHT*2.1+DOWN*.4)
        title_2.add_background_rectangle(color=_color_4)
        self.play(Write(title_2))
        self.wait(.7)


        title_3=Text(
            "夹逼准则",font_size=25,font=font_2,weight=BOLD,
        ).next_to(title_2,RIGHT,aligned_edge=DOWN)
        
        self.play(Write(title_3))

        # 1. 夹逼定理核心思想（中文 + 面包夹火腿可视化）
        title1 = Text(
            "1. 夹逼定理的核心思想", 
            font_size=28,font=font_2).next_to(title_2,DOWN).shift(LEFT*1.2)
        title1.add_background_rectangle(color=_color_8,buff=.05)
        para1  = Paragraph(
            "想象一个简单的场景：",
            "你有两片面包，一片在另一片的上方，中间夹着一片火腿。",
            "如果两片面包同时向中间移动，最终汇合在一个面，",
            "那么中间的火腿毫无疑问也会被压到同一个面。",
            font_size=25,
            font=font_2,
            line_spacing=1
            ).next_to(title1, DOWN,aligned_edge=LEFT).shift(RIGHT*0.5)

        bread1 = Rectangle(width=4, height=0.4, color=WHITE, stroke_width=1).shift(UP*0.7)
        bread2 = Rectangle(width=4, height=0.4, color=WHITE, stroke_width=1).shift(DOWN*0.7)
        ham    = Rectangle(width=3.5, height=0.3, color=YELLOW, stroke_width=1)

        bread_group = VGroup(bread1, ham, bread2).arrange(DOWN, buff=0.1).next_to(para1, RIGHT, buff=0.3)

        self.play(Write(title1))
        self.play(Write(para1), FadeIn(bread_group))
        self.wait(1)

        # 2. 数学表述（中文 + 函数版本）
        title2 = Text(
            "2. 夹逼定理的数学表述", 
            font=font_2,
            font_size=28).next_to(title1, DOWN, buff=2.5,aligned_edge=LEFT)
        title2.add_background_rectangle(color=_color_8,buff=.05)
        para2  = Paragraph(
            "在数学上，这就是夹逼定理的思想：",
            "如果你能把一个“复杂”的函数 f(x) 夹在两个“简单”的函数 g(x) 和 h(x) 之间，",
            "并且这两个简单函数在 x 趋近于某个值 a 时，有相同的极限 L，",
            "那么被夹在中间的 f(x) 也别无选择，只能拥有相同的极限 L。",
            font_size=25, 
            font=font_2,
            line_spacing=1
            ).scale(0.9).next_to(title2,DOWN,aligned_edge=LEFT).shift(RIGHT*0.5)
        
        rule = MathTex(
            r"\text{若 }g(x)\le f(x)\le h(x),\;\lim_{x\to a}g(x)=L,\;\lim_{x\to a}h(x)=L,"
            r"\text{则}\,\lim_{x\to a}f(x)=L.",
            font_size=30, stroke_width=1, color=_color_4
        ).to_edge(DOWN, buff=1.5)
        
        self.play(Write(title2))
        self.play(Write(para2))
        self.wait()
        self.play(LaggedStart(FadeOut(para2),Write(rule),lag_ratio=.3))

        self.play(LaggedStartMap(FadeOut,
            [title1, title2, rule, para1, bread_group], lag_ratio=0.3), run_time=1.5)

        
        #=============Page 4================
        page_4Group=VGroup()
        example4=VGroup(
            Text(
            "例题：",font_size=30,font=font_2,
            ),
            MathTex(
                r"\lim_{x \to 0} x^2 \cdot \sin\left(\frac{1}{x}\right)",
                font_size=30, stroke_width=1, 
            )
        ).arrange(RIGHT).next_to(title_2,DOWN).shift(LEFT*1.3)

        self.play(Write(example4))
        page_4Group.add(example4)

        step2_title = Text(
            "寻找上下界：", font_size=29, color=YELLOW,font=font_2,
            ).next_to(example4, DOWN,buff=.3, aligned_edge=LEFT)
        
        self.play(Write(step2_title))
        page_4Group.add(step2_title)

        step2_ineq = MathTex(
            "-1 \\leq \\sin\\frac{1}{x} \\leq 1 \\quad",         
            font_size=27,
            stroke_width=1,
            color=_color_8
        ).next_to(step2_title, RIGHT)

        self.play(Write(step2_ineq))
        page_4Group.add(step2_ineq)
        self.wait(.7)


        # 第三步：构造不等式
        step3_title = Text(
            "构造不等式：", font_size=29, color=YELLOW,font=font_2,
            ).next_to(step2_title, DOWN,buff=.4, aligned_edge=LEFT)
        
        self.play(Write(step3_title))
        page_4Group.add(step3_title)
        self.wait(.7)

        inal_ineq = MathTex(
            "-x^2 \\leq x^2 \\cdot \\sin\\left(\\frac{1}{x}\\right) \\leq x^2", 
            font_size=28, 
            color=_color_8,
            stroke_width=1,
            ).next_to(step3_title, RIGHT)
        
        self.play(Write(inal_ineq))
        page_4Group.add(inal_ineq)
        self.wait(.7)

        # 第4步：计算边界函数的极限
        step4_title = Text(
            "计算边界函数的极限：", font_size=29, color=YELLOW,font=font_2,
            ).next_to(step3_title, DOWN,buff=.4, aligned_edge=LEFT)
        
        self.play(Write(step4_title))
        page_4Group.add(step4_title)
        self.wait(.7)

        step4_process=MathTex(
            r"\begin{aligned}&\lim_{x \to 0} (-x^2) =0 \\ &\lim_{x \to 0} x^2 = 0 \end{aligned}",
            font_size=28,
            stroke_width=1,
            color=RED
        ).next_to(step4_title,RIGHT,aligned_edge=UP)


        step3_rec1=self.EmphasizeText(inal_ineq[0][0:3],color=RED)
        step3_rec2=self.EmphasizeText(inal_ineq[0][16:18],color=RED)
        page_4Group.add(step3_rec1)
        page_4Group.add(step3_rec2)
         
        self.play(Write(step4_process))
        page_4Group.add(step4_process)
        self.wait(.7)


        # 第5步：计算边界函数的极限
        step5_title = Text(
            "应用夹逼定理得出结论：", font_size=29, color=YELLOW,font=font_2,
            ).next_to(step4_title, DOWN,buff=1.2, aligned_edge=LEFT)
        
        self.play(Write(step5_title))
        page_4Group.add(step5_title)
        self.wait(.7)

        conclusion=VGroup(
            VGroup(
                Text("由于函数",font=font_2,font_size=25),
                MathTex(r"f(x) = x^2 \cdot \sin\left(\frac{1}{x}\right)",
                    font_size=28, stroke_width=1),
                Text("被夹在两个函数之间：",font=font_2,font_size=25),
                MathTex(r"g(x) = -x^2, h(x) = x^2",font_size=28, stroke_width=1
                )        
            ).arrange(RIGHT),
            VGroup(
                Text("并且当",font=font_2,font_size=25),
                MathTex(r"x \to 0",font_size=28, stroke_width=1),
                Text("时，两个边界函数都趋近于 0，根据夹逼定理：",font=font_2,font_size=25),
            ).arrange(RIGHT),
            
        ).arrange(DOWN,aligned_edge=LEFT).next_to(
            step5_title,RIGHT,aligned_edge=UP).shift(UP*.3)

        resoult1=MathTex(
                r"\lim_{x \to 0} x^2 \cdot \sin\left(\frac{1}{x}\right) = 0",
                font_size=28, stroke_width=1,color=RED
        ).next_to(conclusion,DOWN)
        
        
        self.play(Write(conclusion))
        page_4Group.add(conclusion)
        self.play(Write(resoult1))
        page_4Group.add(resoult1)
        self.wait(1)

        self.play(LaggedStartMap(FadeOut, page_4Group, lag_ratio=0.3), run_time=2)
   
 
        
        
        
        
        #=============Page 5================
        example4=VGroup(
            Text(
            "例题：",font_size=30,font=font_2,
            ),
            MathTex(
                r"\lim_{n \to \infty} \frac{1^2 + 2^2 + \cdots + n^2}{n^3}",
                font_size=30, stroke_width=1, 
            )
        ).arrange(RIGHT).next_to(title_2,DOWN).shift(LEFT*.3)

        page5Group=VGroup()
        self.play(Write(example4))
        page5Group.add(example4)

        exam_rec1=self.EmphasizeText(example4[1][0][6:18])
        self.wait(1)
        self.play(Uncreate(exam_rec1))

        # 第二步：寻找上下界
        step2_title = Text(
            "寻找上下界", font_size=30, color=YELLOW,font=font_2,
            ).next_to(example4, DOWN,buff=.3, aligned_edge=LEFT)
        
        self.play(Write(step2_title))
        page5Group.add(step2_title)

        recs=[]
        for index in [6,9,15]:
            recs.append(Circumscribe(example4[1][0][index:index+2]))
        self.play(LaggedStart(*recs,lag_ratio=.4))

        lower_bound_text =VGroup( 
            Text(
            "每一项k²都≥1，"
            "所以总和:",
            font_size=23,
            font=font_2,
            color=_color_8
            ),
            MathTex(               
                r"1^2 + 2^2 + \cdots + n^2",
                r" \ge 1+1+1+ \cdots +1",
                r" = n \cdot 1 = n",
                font_size=28,
                stroke_width=1,
                color=RED
            )
        ).arrange(RIGHT).next_to(step2_title,RIGHT)

        self.play(Write(lower_bound_text))
        page5Group.add(lower_bound_text)

        lower_brace=Brace(lower_bound_text[1][1][1:],UP,color=_color_8)
        lower_brace_text=Text("n 个 1 相加",font_size=23,font=font_2,color=_color_8).next_to(lower_brace,UP)
        self.play(FadeIn(lower_brace),Write(lower_brace_text))
        self.wait(1)
        self.play(FadeOut(lower_brace),FadeOut(lower_brace_text))


        upper_bound_text =VGroup(
            Text(
            "每一项k²都≤n²，"
            "所以总和:",
            font_size=23,
            font=font_2,
            color=_color_8
            ),
            MathTex(
                r"1^2 + 2^2 + \cdots + n^2 \le " ,
                r"n^2 + n^2 + \cdots + n^2",
                r"= n \cdot n^2 = n^3",
                font_size=28,
                stroke_width=1,
                color=RED
            )
        ).arrange(RIGHT).next_to(lower_bound_text, DOWN, aligned_edge=LEFT)        
        
        self.play(Write(upper_bound_text))
        page5Group.add(upper_bound_text)

        upper_brace=Brace(upper_bound_text[1][1],DOWN,color=_color_8)
        upper_brace_text=Text("n 个 n² 相加",font_size=23,font=font_2,color=_color_8).next_to(upper_brace,DOWN)
        self.play(FadeIn(upper_brace),Write(upper_brace_text))

        self.wait(1.3)
        self.play(FadeOut(upper_brace),FadeOut(upper_brace_text))

        # 第三步：构造不等式
        step3_title = Text(
            "构造不等式", font_size=30,font=font_2, 
            color=YELLOW).next_to(
                step2_title, DOWN,buff=1.5, aligned_edge=LEFT)
        
        step3_ineq = MathTex(
            "\\frac{n}{n^3} \\leq \\frac{1^2 + 2^2 + \\cdots + n^2}{n^3} \\leq \\frac{n^3}{n^3}",
            "\\; \\Longrightarrow",
            stroke_width=1,
            font_size=25,
            color=_color_8,
        ).next_to(step3_title, RIGHT)
        
        step3_simplify = MathTex(
            "\\frac{1}{n^2} \\leq \\frac{1^2 + 2^2 + \\cdots + n^2}{n^3} \\leq 1",
            stroke_width=1,
            font_size=25,
            color=RED,
        ).next_to(step3_ineq, RIGHT)
        
        self.play(Write(step3_title))
        page5Group.add(step3_title)
        self.wait(.7)
        self.play(Write(step3_ineq))     
        page5Group.add(step3_ineq)
        self.play(Write(step3_simplify))
        page5Group.add(step3_simplify)
        self.wait(1)

        eph_rec1=self.EmphasizeText(step3_simplify[0][0:4])
        eph_rec2=self.EmphasizeText(step3_simplify[0][21:22])
        page5Group.add(eph_rec1,eph_rec2)
        lable1=Text(
            "极限为 0",
            font_size=25,
            font=font_2,
        ).next_to(step3_simplify[0][0:4],DOWN)
        lable2=Text(
            "极限为 1",
            font_size=25,
            font=font_2,
        ).next_to(step3_simplify[0][21:22],DOWN)
        self.play(Write(lable1),Write(lable2))
        page5Group.add(lable1,lable2,title_2,title_3)
        self.wait(2)
        
        self.play(LaggedStartMap(FadeOut, page5Group,lag_ratio=.3))



        #=============page 6 =============
        title_4=Text(
            "两个重要极限",font_size=29,font=font_2,
        ).to_corner(UL).shift(RIGHT*2.1+DOWN*.4)
        title_4.add_background_rectangle(color=_color_4)
        page6Group=VGroup()
        self.play(Write(title_4))
        page6Group.add(title_4)
        self.wait(.7)

        title3 = Text(
            "第一个重要极限: ", font_size=30,font=font_2, color=BLUE,weight=BOLD
            ).to_corner(UL).shift(DOWN*1.3+RIGHT*.2)
        
        self.play(Write(title3))
        page6Group.add(title3)
        self.wait(.5)

        step1 = MathTex(
            "\\lim_{n \\rightarrow \\infty} \\frac{1}{n} = 0",
            font_size=30,
            stroke_width=1,
            color=_color_4,
        ).next_to(title3, RIGHT)

        self.play(Write(step1))
       
        self.wait(1.5)

        title4 = Text(
            "第二个重要极限: ", font_size=30,font=font_2, color=BLUE,weight=BOLD
            ).next_to(title3, DOWN, buff=.5, aligned_edge=LEFT)
        self.play(Write(title4))
        page6Group.add(title4)
        self.wait(.5)

        step2 = MathTex(
            "\\lim_{n \\rightarrow \\infty} (1 + \\frac{1}{n})^n = e",
            font_size=30,
            stroke_width=1,
            color=_color_4,
        ).next_to(title4, RIGHT)
        self.play(Write(step2))
        
        self.wait(1.5)

        title5 = Text(
            "第一个重要极限的证明", font_size=28,font=font_2,color=_color_10,weight=BOLD
            ).next_to(title_4,RIGHT)
        
        self.play(LaggedStart(
            ReplacementTransform(title3,title5),
            FadeOut(title4),FadeOut(step1),FadeOut(step2),
            lag_ratio=.3
        ))
        
        self.wait(.7)




        
        





    def AddTitle(self,title="temp",font=font_2 ,color:str=_color_1,font_size=35,stroke_width=1.8):
        title=Text(
            title,  # 标题文本内容    
            font=font,  
            font_size=font_size, 
            stroke_width=stroke_width     
            
        ).to_corner(UL)
        
        title_back=Rectangle(
            width=title.width,
            height=title.height,
            fill_opacity=1,
            color=color
        ).move_to(title.get_center()+LEFT*3+DOWN*.2)


        title_back_pos=title_back.animate.move_to(title.get_center()+DOWN*.2+RIGHT*.2)
        
        
        self.add(title_back)  

        return LaggedStart(
            Write(title),
            title_back_pos,
            lag_ratio=0.3,
        )    

    def EmphasizeText(self,target,color:str=YELLOW,stroke_width=4):
        rec_target=Circumscribe(target,color=color,stroke_width=stroke_width)
        rec2_target=SurroundingRectangle(target,color=color,stroke_width=stroke_width)
        self.play(LaggedStart(rec_target,Create(rec2_target),lag_ratio=.5))
        return rec2_target

