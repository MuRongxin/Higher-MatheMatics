from manim import *
import numpy as np

# --------------------- 常量区 ---------------------
TITLE_TEXT       = "数列极限的动态演示"
TITLE_SIZE       = 36
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
        for i in range(1, 10):
            pos = i * 0.1
            t = Line(UP*0.1, DOWN*0.1, color=SUB_TICK_COLOR)
            lab = Text(f"{pos:.1f}", font_size=SUB_TICK_FS, color=SUB_TICK_COLOR)
            self.sub_ticks.add(t)
            self.sub_labels.add(lab)
        self._layout_sub_ticks()
        self.add(self.line, self.ticks, self.labels,
                 self.sub_ticks, self.sub_labels,
                 self.seq_dots, self.seq_labels)
    # ------------- 私有布局方法 -------------
    def _x2pos(self, x: float) -> np.ndarray:
        """把数学坐标 x 转换成 Manim 坐标"""
        return self.center_offset + RIGHT * x * self.scale_factor
    def _layout_main_ticks(self):
        for x, tick, lab in zip(range(self.x_min, self.x_max + 1),
                                self.ticks, self.labels):
            tick.move_to(self._x2pos(x))
            lab.next_to(tick, DOWN, buff=0.1)
    def _layout_sub_ticks(self):
        for i, (tick, lab) in enumerate(zip(self.sub_ticks, self.sub_labels)):
            x = (i + 1) * 0.1
            tick.move_to(self._x2pos(x))
            lab.next_to(tick, DOWN, buff=0.15)
    # ------------- 公开接口 -------------
    def add_sequence_points(self, n_start: int, n_end: int, scene: Scene, runTime=ANIM_TIME):
        """把 a_n = 1/n (n_start..n_end) 逐个出现"""
        for n in range(n_start, n_end + 1):
            a_n = 1 / n
            dot = Dot(color=DOT_COLOR).move_to(self._x2pos(a_n))
            # 偶数 label 在上方，奇数在下方，避免重叠
            direction = DOWN if n % 2 == 0 else UP
            if n<=9:
                label = MathTex(f"a_{{{n}}} = \\frac{{1}}{{{n}}}",
                                font_size=LABEL_FS,
                                color=LABEL_COLOR)
            else:
                label = MathTex(f"a_{{{n}}}",
                                font_size=LABEL_FS,
                                color=LABEL_COLOR)
            label.next_to(dot, direction, buff=0.2)
            self.seq_dots.add(dot)
            self.seq_labels.add(label)
            self.seq_n_values.append(n)  # 存储n值
            scene.play(FadeIn(dot), Write(label), run_time=runTime)
            scene.wait(runTime/2)
    def zoom_to(self, new_scale: float, new_points: tuple[int, int] = None, scene: Scene = None, runTime=ZOOM_TIME):
        """一次性完成：
        1) 所有主刻度、子刻度、已有点的缩放与移动
        2) 新增 new_points 区间的数列点
        """
        anims = []
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
            x = (i + 1) * 0.1
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
        anims.append(self.line.animate.stretch_to_fit_width(
            self.line.get_width() * new_scale / old_scale))
        if scene:
            scene.play(*anims, run_time=runTime)
        # 新增点（如果有）
        if new_points and scene:
            self.add_sequence_points(new_points[0], new_points[1], scene, runTime/2)

# 配置LaTeX支持中文
config.tex_template = TexTemplate(
    preamble=r"""
\usepackage{ctex}
\usepackage{amsmath,amssymb}
"""
)
# --------------------- 场景剧本 ---------------------
class ImprovedNumberLine(Scene):
    def construct(self):
        # 标题
        title = Text(TITLE_TEXT, font_size=TITLE_SIZE, color=BLUE)
        title.to_edge(UP)

        # 第一部分：例：数列 a_n = 1/n
        part1 = MathTex(r"\text{例：数列 } a_{n} = \frac{1}{n}", font_size=30, color=WHITE)

        # 第二部分：或表示为：lim(n→∞) a_n
        part2 = MathTex(r"\text{或表示为：} \lim_{n \to \infty} a_{n}", font_size=30, color=WHITE)
        part2.next_to(part1, RIGHT, aligned_edge=LEFT, buff=0.2)
        # 第三部分：当 n 不断增大时的取值情况
        part3 = Text("当 n 不断增大时的取值情况", font_size=25, color=WHITE)

        # 第四部分：n=1,2,3,4,5,6,7,8,9...
        part4 = MathTex(r"n=1,2,3,4,5,6,7,8,9 \ldots", font_size=30, color=RED_A )

        # 将所有部分垂直排列
        exampleInfo=VGroup(part1,part2).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
        example = VGroup(exampleInfo ,part3, part4).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # 结论
        conclusion=Tex("结论：数列 $a_n = \\frac{1}{n}$ 的极限是 0，也可以说数列 $a_n = \\frac{1}{n}$ 收敛于 0",font_size=40, color=BLUE_B)

        example.next_to(title, DOWN).shift(LEFT*4)

        self.play(Write(title), Write(example))

       

        # 初始数轴
        axis = NumberAxis(initial_scale=1, center=np.array([-3, 0, 0]))
        self.play(Create(axis.line), Create(axis.ticks), Write(axis.labels))
        
        # 第一轮 放大
        axis.zoom_to(7, None,  self)
        

        # 第一轮点
        axis.add_sequence_points(1, 4, self)

        # 三次放大
        axis.zoom_to(15, (6, 9),  self)
        axis.zoom_to(30, (10, 17), self, 0.7)
        axis.zoom_to(50, (18, 25), self, 0.7)
        axis.zoom_to(100, (26,50), self, 0.5)
        axis.zoom_to(200, (50,77), self, 0.4)
        self.wait(1)

        self.play(Write(conclusion), conclusion.animate.to_edge(DOWN).shift(LEFT*0.5), buff=0.4)
        
        self.wait(2)