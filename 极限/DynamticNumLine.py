from manim import *
import numpy as np
from typing import Optional

# --------------------- 常量区 ---------------------
TITLE_TEXT       = "数列极限的动态演示"
TITLE_SIZE       = 41
TICK_FONT_SIZE   = 29
SUB_TICK_FS      = 25
LABEL_FS         = 29
DOT_COLOR        = RED
TICK_COLOR       = WHITE
SUB_TICK_COLOR   = YELLOW
LABEL_COLOR      = BLUE
ANIM_TIME        = 0.5
ZOOM_TIME        = 1

# --------------------- 可复用组件 ---------------------
class NumberAxis(VGroup):
    """一条水平数轴，支持整数刻度、0.1 子刻度、数列点及缩放动画。"""
    def __init__(self,
                 x_min: int = -15,
                 x_max: int = 15,
                 initial_scale: float = 1,
                 center: np.ndarray = ORIGIN,
                 **kwargs):
        super().__init__(**kwargs)
        self.x_min         = x_min
        self.x_max         = x_max
        self.scale_factor  = initial_scale
        self.center_offset = center   # 数轴中心相对 Scene 中心的偏移
        self.seq_dots      = VGroup() # 已经创建的数列点
        self.seq_labels    = VGroup()
        self.seq_n_values  = []      # 每个点对应的n值
        # --- 主刻度 ---
        self.line   = Line(LEFT*10, RIGHT*10, color=TICK_COLOR)
        self.ticks  = VGroup()
        self.labels = VGroup()
        for x in range(self.x_min, self.x_max + 1):
            t = Line(UP*0.2, DOWN*0.1)
            lab = Text(str(x), font_size=TICK_FONT_SIZE)
            self.ticks.add(t)
            self.labels.add(lab)
        self._layout_main_ticks()
        # --- 0.1 子刻度 ---
        self.sub_ticks  = VGroup()
        self.sub_labels = VGroup()
        # for i in range(1, 10):
        #     pos = i * 0.1
        #     t = Line(UP*0.1, DOWN*0.1, color=SUB_TICK_COLOR)
        #     lab = Text(f"{pos:.1f}", font_size=SUB_TICK_FS, color=SUB_TICK_COLOR)
        #     self.sub_ticks.add(t)
        #     self.sub_labels.add(lab)
        # self._layout_sub_ticks()
        self.add(self.line, self.ticks, self.labels,
                 self.sub_ticks, self.sub_labels,
                 self.seq_dots, self.seq_labels)
    # ------------- 私有布局方法 -------------
    def _x2pos(self, x: float) -> np.ndarray:
        """把数学坐标 x 转换成 Manim 坐标"""
        return self.center_offset + RIGHT * x * self.scale_factor
    
    def _pos2x(self, pos: np.ndarray) -> float:
        """将 Manim 坐标转换为数学坐标 x"""
        # 确保我们处理的是单个坐标而不是数组
        if isinstance(pos, np.ndarray):
            return (pos[0] - self.center_offset[0]) / self.scale_factor
        else:
            # 如果 pos 不是数组，直接返回
            return pos

    def _layout_main_ticks(self):
        for x, tick, lab in zip(range(self.x_min, self.x_max + 1),
                                self.ticks, self.labels):
            tick.move_to(self._x2pos(x))
            lab.next_to(tick, DOWN, buff=0.1)
    def _layout_sub_ticks(self,startPos = 0):
        for i, (tick, lab) in enumerate(zip(self.sub_ticks, self.sub_labels)):
            x = startPos + (i + 1) * 0.1
            tick.move_to(self._x2pos(x))
            lab.next_to(tick, DOWN, buff=0.15)
    # ------------- 公开接口 -------------
    def add_sequence_points(self, n_start: int, n_end: int, scene: Scene, runTime=ANIM_TIME):
        """把 a_n = 1/n (n_start..n_end) 逐个出现"""
        insert_dot_animes=[]
        for n in range(n_start, n_end + 1):
            a_n = 1 / n
            dot = Dot(color=DOT_COLOR).move_to(self._x2pos(a_n))
            # 偶数 label 在上方，奇数在下方，避免重叠
            direction = DOWN if n % 2 == 0 else UP
            if n<=9:
                label = MathTex(f"\\mathbf{{a_{{{n}}} = \\frac{{1}}{{{n}}}}}",
                                font_size=LABEL_FS,
                                color=LABEL_COLOR)
            else:
                label = MathTex(f"\\mathbf{{a_{{{n}}}}}",
                                font_size=LABEL_FS,
                                color=LABEL_COLOR)            
            label.next_to(dot, direction, buff=0.2)
            self.seq_dots.add(dot)
            self.seq_labels.add(label)
            self.seq_n_values.append(n)  # 存储n值
            # scene.play(FadeIn(dot), Write(label), run_time=runTime)
            insert_dot_animes+=[FadeIn(dot), Write(label)]
            # scene.wait(runTime/2)
        
        return insert_dot_animes

    def add_sub_ticks(self,startPos:int = 0,new_sub_ticks_range:tuple[int, int] = (0,1)):
        for i in range(new_sub_ticks_range[0], new_sub_ticks_range[1] + 1):
            pos =startPos + i * 0.1
            if abs(pos - round(pos)) < 1e-9:
                continue  # 跳过整数刻度

            t = Line(UP*0.1, DOWN*0.1, color=SUB_TICK_COLOR)
            lab = Text(f"{pos:.1f}", font_size=SUB_TICK_FS, color=SUB_TICK_COLOR)
            self.sub_ticks.add(t)
            self.sub_labels.add(lab)
        self._layout_sub_ticks(startPos)
        # self.add(self.sub_ticks, self.sub_labels)
       
    def zoom_to(self, new_scale: float, new_points: tuple[int, int] = None, scene: Scene = None,new_center: Optional[np.ndarray] = None, runTime=ZOOM_TIME):
        """一次性完成：
        1) 所有主刻度、子刻度、已有点的缩放与移动
        2) 新增 new_points 区间的数列点
        """
        anims = []
        self.center_offset = new_center if new_center is not None else self.center_offset
        # 保存旧的缩放因子
        old_scale = self.scale_factor
        # 更新内部状态
        self.scale_factor = new_scale
        # 主刻度
        for x, tick, lab in zip(range(self.x_min, self.x_max + 1),
                                self.ticks, self.labels):
            anims += [
                tick.animate.move_to(self._x2pos(x)),
                lab.animate.next_to(self._x2pos(x), DOWN, buff=0.3)
            ]
        # 子刻度
        for i, (tick, lab) in enumerate(zip(self.sub_ticks, self.sub_labels)):
            x = (float(lab.text))
            anims += [
                tick.animate.move_to(self._x2pos(x)),
                lab.animate.next_to(self._x2pos(x), DOWN, buff=0.15)
            ]
     

        # 已有点
        for n, dot, lab in zip(self.seq_n_values, self.seq_dots, self.seq_labels):
            a_n = 1 / n
            direction = UP if n % 2 == 0 else DOWN
            anims += [
                dot.animate.move_to(self._x2pos(a_n)),
                lab.animate.next_to(self._x2pos(a_n), direction, buff=0.2)
            ]
        # 数轴本身
        line_center = self._x2pos(0)  # 计算数轴线中心应该移动到的位置       

        anims.append(self.line.animate.move_to(line_center).stretch_to_fit_width(
            self.line.get_width() * new_scale / old_scale))
        # if scene:
        #     scene.play(*anims, run_time=runTime)
        # 新增点（如果有）
        dotAnims = []
        if new_points and scene:
            dotAnims = self.add_sequence_points(new_points[0], new_points[1], scene, runTime/2)

        if scene:
           scene.play(*anims,run_time=runTime)
           scene.play(AnimationGroup(*dotAnims,lag_ratio=.5),run_time=runTime)
class DemoScene(Scene):
    def construct(self):
        # 标题
        title = Text(TITLE_TEXT, font_size=TITLE_SIZE, color=BLUE)
        title.to_edge(UP)

        
        axis = NumberAxis(initial_scale=1, center=np.array([-4, 0, 0]))
       

        self.play(Create(axis.line), Create(axis.ticks), Write(axis.labels))
       
       
        
        # 第一轮 放大
        # axis.zoom_to(5, None,  self)
       
        axis.add_sub_ticks(-1,(1,20))
        # self.play(Create(axis.sub_ticks), Write(axis.sub_labels))
        self.play(FadeIn(axis.sub_ticks), FadeIn(axis.sub_labels))

        # axis.add_sub_ticks(1,(1,9))
        axis.zoom_to(5, (1,4),  self)
        axis.zoom_to(10, (5,11),  self,new_center=np.array([1,0,0]))
        axis.zoom_to(25, (12,17),  self)
        axis.zoom_to(50, (18,23),  self)
        self.wait(1)
        # axis.zoom_to(17, (9,19),  self)
        # self.play(Create(axis.sub_ticks), Write(axis.sub_labels))



class NbConceptDemo(Scene):
    def construct(self):
         # ---------------- 1. 开头 ----------------
        title = Text("简单认识邻域的概念:", font_size=TITLE_SIZE-5, color=BLUE)
        title.move_to(UP*3.5+LEFT*4.4)

        text_before = Text("对实数轴上的点 a 和任意数 ε>0，a 的邻域就是", 
                          font_size=24, color=BLUE_C)
        text_highlight = Text("开区间", font_size=24, color=BLUE_C)
        text_after = Text("(a−ε, a+ε)", font_size=24, color=BLUE_C)

        def_group = VGroup(text_before, text_highlight, text_after).arrange(
            RIGHT
        )

        
        definition_Group = VGroup(
            def_group,
            MathTex(r"\text{可以简单记为：} N(a,\epsilon ) = ( a+\epsilon  ,a+\epsilon )", font_size=TITLE_SIZE-9, color=BLUE),
            MathTex(r"\mathbf{\text{标准记法 } U_\varepsilon(a) = \{x \in \mathbb{R} : |x - a| < \varepsilon\}}", font_size=TITLE_SIZE-5, color=BLUE_A)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(np.array([-1, 2.2, 0]))

        red_box = SurroundingRectangle(
            text_highlight,
            color=RED_E,
            fill_opacity=0,
            stroke_width=3,
            buff=0.1  # 框框和文字的间距
        )

        self.play(Write(title))
        self.play(Write(definition_Group),Create(red_box))
        self.wait(1)
        # ---------------- 2. 数轴与方框邻域 ----------------
        axis = NumberLine(
            x_range=[-7, 7, 1], length=14,
            include_tip=True, include_numbers=True
        ).shift(DOWN * 0.8)

        x0 = ValueTracker(1.0)
        dot =always_redraw(lambda: Dot(axis.number_to_point(x0.get_value()), color=YELLOW, radius=0.1))
        dot_label = always_redraw(lambda: MathTex("a").next_to(dot, UP, buff=0.15))

        eps = ValueTracker(1.0)
        
        box = always_redraw(lambda: Rectangle(
            width=axis.number_to_point(x0.get_value() + eps.get_value())[0]
                  - axis.number_to_point(x0.get_value() - eps.get_value())[0],
            height=1.4,
            stroke_color=GREEN_B, stroke_width=2,
            fill_color=GREEN, fill_opacity=0.35
        ).move_to(axis.number_to_point(x0.get_value()), aligned_edge=ORIGIN))

        self.play(Create(axis), FadeIn(dot), Write(dot_label))
        self.play(Create(box))

        # ---------------- 3. 字幕同步强调 ----------------  
        
        epsilone=always_redraw(
            lambda: MathTex(r"\mathbf{\varepsilon = }", f"{eps.get_value():.1f}",color=RED_D)
            .move_to(axis.number_to_point(x0.get_value())+UP)
        )
        # 端点红线
        left_line = always_redraw(lambda: DashedLine(
            axis.number_to_point(x0.get_value() - eps.get_value()) + UP * 0.7,
            axis.number_to_point(x0.get_value() - eps.get_value()) + DOWN * 0.7,
            stroke_color=RED, 
            stroke_width=7
        ))
        right_line = always_redraw(lambda: DashedLine(
            axis.number_to_point(x0.get_value() + eps.get_value()) + UP * 0.7,
            axis.number_to_point(x0.get_value() + eps.get_value()) + DOWN * 0.7,
            stroke_color=RED, 
            stroke_width=7
        ))
        self.play(Create(left_line), Create(right_line), Create(epsilone))

        # 闪烁强调“不算”
        for _ in range(3):
            self.play(left_line.animate.set_opacity(0.2),
                      right_line.animate.set_opacity(.2),
                      red_box.animate.set_opacity(0.2),
                      rate_func=there_and_back, run_time=0.5)

        # ---------------- 4. 缩放展示“可大可小” ----------------
        self.play(eps.animate.set_value(3), run_time=3, rate_func=there_and_back)
        self.wait()
        
        self.play(x0.animate.set_value(-3), run_time=3, rate_func=there_and_back)

        # ---------------- 5. 多邻域叠放 ----------------
        self.play(eps.animate.set_value(0.5))
        more_eps = [1.0, 1.5, 2.0]
        colors   = [BLUE, ORANGE, PURPLE]
        more_box = VGroup()
        for e, c in zip(more_eps, colors):
            more_box.add(Rectangle(
                width=axis.number_to_point(x0.get_value() + e)[0] - axis.number_to_point(x0.get_value() - e)[0],
                height=1.4, stroke_color=c, stroke_width=2.5,
                fill_color=c, fill_opacity=0.25
            ).move_to(axis.number_to_point(x0.get_value()), aligned_edge=ORIGIN))
        self.play(*[FadeIn(m, scale=1.3) for m in more_box], lag_ratio=0.5)
        
        text=Text("同一个点的邻域不是唯一的, ε 任意，具体选取视情况而定.",font_size=28).next_to(more_box,DOWN,buff=.5)
        self.play(Write(text))
        self.play(Indicate(text))
        
       
        
        self.wait(3)

        # 一键淡出
        self.play(*[FadeOut(m) for m in self.mobjects])







# 配置LaTeX支持中文
config.tex_template = TexTemplate(
    preamble=r"""
\usepackage{ctex}
\usepackage{amsmath,amssymb}
"""
)





import math

class SequenceLimitWithZoom(ZoomedScene,MovingCameraScene):
    def __init__(self,renderer=None, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            renderer=renderer,
            zoomed_display_height=4,
            zoomed_display_width=8,
            image_frame_stroke_width=1,
            zoomed_camera_config={
                "default_frame_stroke_width": 1,
            },
            **kwargs
        )
    
    def construct(self):
        # 创建坐标系
        
        x_amx_length=77
        axes = Axes(
            x_range=[0, x_amx_length, 5],
            y_range=[-1, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
            tips=False,
        ).scale(1)
        
        # 添加坐标轴标签
        x_label = axes.get_x_axis_label("n", edge=RIGHT, direction=UP, buff=0.5)
        y_label = axes.get_y_axis_label("x_n", edge=UP, direction=RIGHT, buff=0.7)
        
        axes_Anime=[]
        axes_Anime+=[Create(axes), Write(x_label), Write(y_label)]

        title=MathTex(
            r"\text{数列}x_n = \frac{\sin(n)}{n}\text{的收敛演示}",
            font_size=30).move_to(np.array([5, 3.3, 0]))
        
        title_1=MathTex(
            r"\text{数列}x_n = \frac{\sin(n)}{n}\text{的收敛演示}",
            font_size=40).move_to(ORIGIN)

        # 极限值 L = 0
        L = 0
        limit_line = Line(axes.c2p(0, L), axes.c2p(x_amx_length, L), color=YELLOW, stroke_width=2)

        self.play(Create(title_1))
        self.wait(1)
        self.play(Transform(title_1,title))
        
        self.play(*axes_Anime)
        
        
        # 添加极限标签
        limit_label = MathTex(r"\text{数列} \frac{sin(n)}{n}\text{的极限数值为： }L = 0",font_size=27).next_to(limit_line, UP, buff=0.8)
        self.play(Write(limit_label))
        self.play(Create(limit_line))

        # 定义 epsilon 邻域
        epsilon = ValueTracker(0.1)
        epsilon_band_upper = always_redraw(lambda: DashedLine(
            axes.c2p(0, L + epsilon.get_value()), 
            axes.c2p(x_amx_length, L + epsilon.get_value()), 
            color=GREEN_B, 
            stroke_width=4
        ))
        epsilon_band_lower = always_redraw(lambda: DashedLine(
            axes.c2p(0, L - epsilon.get_value()), 
            axes.c2p(x_amx_length, L - epsilon.get_value()), 
            color=GREEN_B, 
            stroke_width=4            
        ))
       
        # 创建邻域区域
        epsilon_region = always_redraw(lambda: Rectangle(
            width=axes.c2p(x_amx_length, 0)[0] - axes.c2p(0, 0)[0],            
            height=2*epsilon.get_value()*axes.y_length/(axes.y_range[1]-axes.y_range[0]), 
            fill_color=RED,
            fill_opacity=0.2,
            stroke_width=0
        ).move_to(axes.c2p(x_amx_length/2, L)))
        # 添加 epsilon 标签
        epsilon_label = always_redraw(lambda: 
                                      MathTex(r"\varepsilon \text{取值为：} "+
                                              f"{epsilon.get_value():.2f}",
                                              font_size=27)
                                              .next_to(limit_label, RIGHT, buff=0.3))

        epsilon_label_upper = always_redraw(lambda: MathTex(r"L + \varepsilon ",font_size=27).next_to(epsilon_band_upper, LEFT, buff=0.1))
        epsilon_label_lower = always_redraw(lambda: MathTex(r"L - \varepsilon ",font_size=27).next_to(epsilon_band_lower, LEFT, buff=0.1))
        
        # 显示极限定义
        text_1=Text("由数列极限的定义：",font_size=25)
        definition_1 = MathTex(
            r"\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall n > N, |x_n - L| < \varepsilon"
        ).scale(0.5)
        text_2=Text("我们可得：",font_size=25)
        definition_2 = MathTex(
            r"\text{极限 L 的} \varepsilon \text{领域:}(L- \varepsilon,L+\varepsilon)"
            ).scale(0.5)

        defi=VGroup(text_1,definition_1,text_2).arrange(RIGHT)

        definition=VGroup(defi,
                          definition_2
                          ).arrange(DOWN,aligned_edge=RIGHT).move_to(axes.c2p(44,1))
       

        self.play(Write(definition))
        self.play(Create(epsilon_band_upper), 
                  Create(epsilon_band_lower),
                  Create(epsilon_region),
                  Write(epsilon_label))

        self.wait(.5)
        indicate_region=SurroundingRectangle(epsilon_region, color=RED, buff=0.1)
        self.play(Create(indicate_region))
        self.wait(.5)
        self.play(Uncreate(indicate_region))

        self.play(Write(epsilon_label_upper),
                  Write(epsilon_label_lower))
       
        
        # 生成数列点
        x_values = list(range(1, 77))
        y_values = [np.sin(n)/n for n in x_values]
       
        # 创建数列点
        dots = []
        for n, y in zip(x_values, y_values):
            point = axes.c2p(n, y)           
            dot = Dot(point, color=RED, radius=0.05)
            dots.append(dot)
        
        self.wait(.5)
#=========================================================
# 定义相机移动策略

        dot_group = VGroup()            # 【新增】
        self.add(dot_group)             # 挂到场景里，后续由 updater 往里填点
        
        def spawn_dot_on_tick(mob, dt):                       # 【新增】
            if not hasattr(spawn_dot_on_tick, "idx"):         # 静态计数器
                spawn_dot_on_tick.idx = 0
                spawn_dot_on_tick.accum=0.0
            
            INTERVAL=0.07
            spawn_dot_on_tick.accum+=dt
            # print("============================.dot_group count: "+str(len(dot_group)))
            idx = spawn_dot_on_tick.idx
            
            if spawn_dot_on_tick.accum<INTERVAL:
                return
            if idx < len(x_values):                           # 还有没描的点
                dot = Dot(axes.c2p(x_values[idx], y_values[idx]), radius=0.04,color=RED)
                mob.add(dot)                                  # 填到容器里
                spawn_dot_on_tick.idx += 1                    # 计数器 +1
                spawn_dot_on_tick.accum=0.0

        
        dot_group.add_updater(spawn_dot_on_tick)              # 【新增】正式交给引擎

        camera_moves = {                                      # 【新增】把要移动的关键帧先列出来
              # n==30 时，run_time=1 s
            40: 1.5,
            44: 1.5,
            50: 1.5,
            58: 2,           
        }

        
        def get_camera_target(n):
            """根据当前点的位置计算相机应该移动到的目标位置和缩放级别"""
            # 目标位置：当前点的x坐标稍微靠右，y坐标保持在极限线附近
            target_x = n + 4  # 让相机稍微超前一些
            target_point = axes.c2p(target_x, L+0.25)
            width=self.camera.frame.width
            # 动态调整缩放级别：随着n增大，视野变窄以看清细节
            # 当n较小时，保持较宽的视野；当n较大时，缩小视野以聚焦
            if 30 < n < 40:
                width = 15  # 初始较宽的视野
            if 40 <n < 70:
                width = 10   # 中等视野
            # else:
            #     width = 8   # 后期聚焦的窄视野
                
            return target_point, width        

        self.wait(1.5)  # 等待数轴和极限线等元素稳定下来

        for _, (dot, n, y) in enumerate(zip(dots, x_values, y_values)):
    # ---------- 触发相机移动 ----------
            # self.wait(0.02  )
            if n in camera_moves:                               # 【改动】只留关键帧
                target_point, new_width = get_camera_target(n)
                # 并行播放，不影响描点
                self.play(
                    self.camera.frame.animate.move_to(target_point).set(width=new_width),
                    run_time=camera_moves[n],
                    rate_func=smooth
               )
    # ---------- 其他一次性小动画 ----------
            if n == 50:
                self.play(axes.x_axis.animate.set_font_size(5), run_time=0.3)
            
           

            
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).set(width=15),
            run_time=2
        )
        
#===================================================        
        
        # self.wait(2)
        
        


        # ===== 缩放功能 =====
        # 设置缩放区域（选择数列收敛的部分）
        zoom_area_1 = Rectangle(
            width=3,
            height=1.5,
            color=WHITE,
            stroke_width=2
        ).move_to(axes.c2p(70, L))
        
        zoom_area_2 = Rectangle(
            width=3,
            height=1.5,
            color=WHITE,
            stroke_width=2
        ).move_to(axes.c2p(15, L))

        self.play(Create(zoom_area_1),Create(zoom_area_2))

 

        # 激活缩放
        self.activate_zooming()        
        
        self.zoomed_camera.frame.match_width(zoom_area_1)
        self.zoomed_camera.frame.match_height(zoom_area_1)
        self.zoomed_camera.frame.move_to(zoom_area_1.get_center())
        self.zoomed_display.to_corner(UR)
        
       
        
        self.play(self.get_zoomed_display_pop_out_animation())

        discreption=Text(
            "随着n 取值的增大，数列的值会越来越接近极限值，收敛在极限值附近",
            font_size=29,color=BLUE).to_edge(DOWN,buff=.8).shift(RIGHT*.5)
        self.wait(1)
        


        surrendRect=SurroundingRectangle(discreption,color=RED_A,buff=.1)
       
        self.play(Write(discreption),Create(surrendRect))
        self.wait(1)          
        
        # 清理缩放
        self.play(self.get_zoomed_display_pop_out_animation(), reverse_rate_function=True)

        self.play(Uncreate(surrendRect), Uncreate(discreption), Uncreate(zoom_area_1))
        self.wait(1)
      
        
        confirm_N_value_1=MathTex(
            r"\text{由数列极限定义，}\text{对于}\forall \varepsilon > 0 ,\
            \exists N \in \mathbb{N},\
            \text{当}n>N\text{时，有}\left | x_n-L \right|<\varepsilon"
        ).scale(0.7)
        
        confirm_N_value_2=MathTex(
            r"\text{已知极限 L 为 0} ,\varepsilon \text{现在取的是0.1}\
            \text{，需要确定N值}").scale(0.7)
        
        confirm_N_value_3=MathTex(
            r"\text{则：}\left | n-0 \right|<0.1,").scale(0.7)

        confirm_N_value=VGroup(confirm_N_value_1,
                               confirm_N_value_2,
                               confirm_N_value_3
                               ).arrange(DOWN,aligned_edge=LEFT).to_edge(
                                   DOWN,buff=.7).shift(LEFT*.5)
        
        self.play(Write(confirm_N_value))

        self.play(self.camera.frame.animate.move_to(axes.c2p(13,0.1)).set(width=9),
            run_time=1.5
        )

        self.wait(1)
        
        
        # 计算并标记 N 值
        N_value = math.ceil(1 / epsilon.get_value())
        N_indicator =DashedLine(
            start=axes.c2p(N_value, 0), 
            end=axes.c2p(N_value, 0.5), 
            color=WHITE,
            stroke_width=3
        )
        
        self.play(Create(N_indicator))
        
        N_label = MathTex(r"N = \lceil \frac{1}{\varepsilon} \rceil").scale(0.7).next_to(N_indicator, RIGHT, buff=0.2)
        self.play(Write(N_label))
        # self.wait(2)
        
        
        
        self.play(epsilon.animate.set_value(0.05), run_time=.8)
        # self.play(self.camera.frame.animate.set(width=9))
        
        N_value = math.ceil(1 / epsilon.get_value())
        N_indicator_2 =DashedLine(
            start=axes.c2p(N_value, 0), 
            end=axes.c2p(N_value, 1), 
            color=WHITE,
            stroke_width=2
        )
        N_label_2 = MathTex(r"N = \lceil \frac{1}{\varepsilon} \rceil").scale(0.7).next_to(N_indicator, RIGHT, buff=0.2)

        self.play(Transform(N_indicator, N_indicator_2),
                  Transform(N_label, N_label_2),run_time=1)

        self.wait(1)
        # 最终动画：移除邻域，保留极限线
        # self.play(
        #     Uncreate(epsilon_band_upper),
        #     Uncreate(epsilon_band_lower),
        #     FadeOut(epsilon_region),
        #     Uncreate(N_indicator),
        #     Uncreate(N_label),
        #     Uncreate(zoom_area_1)
        # )
        
        self.wait(2)
        
        # 重新强调极限
        self.play(limit_line.animate.set_stroke_width(4))
        self.wait(1)
        
        # 清理
        # self.play(
        #     *[Uncreate(dot) for dot in dots],
        #     Uncreate(limit_line),
        #     Uncreate(limit_label),
        #     Uncreate(definition),
        #     Uncreate(epsilon_label)
        # )
        
        

        # self.wait(1) 







class specificExample_1(MovingCameraScene):
    def construct(self):
        # 题目
        example=MathTex(
            r"\text{例：用定义证明数列}x_n = \frac{1}{n}\text{的极限是0 。}",
            font_size=40
        ).to_corner(UL)
        
        define=MathTex(
            r"\text{数列极限定义，}\text{对于}\forall \varepsilon > 0 ,\
            \exists N \in \mathbb{N},\
            \text{当}n>N\text{时，有}\left | x_n-L \right|<\varepsilon"
        ,color=BLUE_D).scale(0.7).next_to(example,DOWN,buff=.4).align_to(example,LEFT)
        
        description=Text(
            "该数列的极限值 L = 0 , 需要根据 ε 的取值，确定 N 的值，证明的关键点就是确定N值.",
            font_size=29).next_to(define,DOWN,buff=.3).align_to(define,LEFT)

        emphasizeRect=Rectangle(
            width=2,
            height=0.8,
            color=RED,
            stroke_width=3
        ).move_to(np.array([.5,1.8,0]))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#======动画播放区间=============================
        self.play(Write(example))
        self.wait(1)
        self.play(Write(define))
        self.wait(.8)
        print("================================>",str(description.get_bottom()))
        self.play(Write(description))
        self.play(Create(emphasizeRect))
