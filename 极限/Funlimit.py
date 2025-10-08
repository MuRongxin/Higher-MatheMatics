from manim import *
import numpy as np

from manim.utils.rate_functions import (ease_in_out_cubic )

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
font_2="FZZhengHeiS-EB-GB"
font_3="H.H. Samuel"
font_4="Harlow Solid"
font_5="Kristen ITC"
font_6="Playbill"
font_7="STCaiyun"
font_8="WenYue XinQingNianTi J"
font_9="FZZongYi-M05S"
font_foreign="Forte"


#SmileySans-Oblique_6.ttf

class Infinitesimal(MovingCameraScene):
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
            "假设这是一块足球场",font=font_2,
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
            "这个不断分割的过程中产生的每一块“蛋糕”，",          
            font_size=30,
            color=_color_6,
            font=font_2
        )
        summary_text_2=Text(
            "  相对于足球场来说都越来越微不足道，",
             font_size=30,
             color=_color_6,
             font=font_2
        )
        summary_text_3=Text(
            "   但它们本身都大于零",
             font_size=30,
             color=_color_6,
             font=font_2
             )
        summary_text=VGroup(
            summary_text_1,summary_text_2,summary_text_3
        ).arrange(DOWN,aligned_edge=LEFT).move_to(
            rec_playground.get_center()+RIGHT*.3).set_stroke(width=1.5,color=_color_8)
        self.play(Write(summary_text))


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
            "这里有一块蛋糕", font_size=1,color=_color_4,font=font_8).next_to(rects,UP)
        
        self.play(Write(cakeTex))


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
        # self.play(Write(cakeTex))
        # self.wait(1)

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

        self.wait(2)

        self.play(
            self.camera.frame.animate.move_to(rects[100].get_center()).set_width(0.01),
            run_time=2.5,rate_functions=smooth)


