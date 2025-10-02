from manim import *
import numpy as np
from typing import Callable, Optional, Union, List, Tuple

# --------------------- 常量区 ---------------------
TITLE_TEXT = "数列极限的动态演示"
TITLE_SIZE = 36
TICK_FONT_SIZE = 29
SUB_TICK_FS = 25
LABEL_FS = 29
DOT_COLOR = RED
TICK_COLOR = WHITE
SUB_TICK_COLOR = YELLOW
LABEL_COLOR = BLUE
ANIM_TIME = 0.5
ZOOM_TIME = 1

# --------------------- 可复用组件 ---------------------
class EnhancedNumberAxis(VGroup):
    """增强型水平数轴，支持灵活刻度、子刻度、函数点添加和缩放动画"""
    
    def __init__(
        self,
        x_range: Tuple[float, float, float] = (-15, 15, 1),  # (min, max, step)
        sub_tick_step: Optional[float] = 0.1,
        sub_tick_range: Optional[Tuple[float, float]] = None,
        initial_scale: float = 1.0,
        center: np.ndarray = ORIGIN,
        tick_length: float = 0.2,
        sub_tick_length: float = 0.1,
        include_numbers: bool = True,
        numbers_to_include: Optional[List[float]] = None,
        decimal_places: int = 0,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        # 参数设置
        self.x_min, self.x_max, self.step = x_range
        self.sub_tick_step = sub_tick_step
        self.sub_tick_range = sub_tick_range if sub_tick_range is not None else (self.x_min, self.x_max)
        self.scale_factor = initial_scale
        self.center_offset = center
        self.tick_length = tick_length
        self.sub_tick_length = sub_tick_length
        self.include_numbers = include_numbers
        self.numbers_to_include = numbers_to_include
        self.decimal_places = decimal_places
        
        # 存储组件
        self.seq_dots = VGroup()
        self.seq_labels = VGroup()
        self.seq_n_values = []
        self.function_dots = VGroup()
        self.function_labels = VGroup()
        
        # 创建数轴
        self.line = Line(
            self._x2pos(self.x_min), 
            self._x2pos(self.x_max), 
            color=TICK_COLOR
        )
        
        # 主刻度
        self.ticks = VGroup()
        self.labels = VGroup()
        
        # 确定要显示的数字
        if self.numbers_to_include is not None:
            numbers = self.numbers_to_include
        else:
            numbers = np.arange(self.x_min, self.x_max + self.step, self.step)
        
        for x in numbers:
            if self.x_min <= x <= self.x_max:
                tick = Line(UP * self.tick_length/2, DOWN * self.tick_length/3, color=TICK_COLOR)
                tick.move_to(self._x2pos(x))
                self.ticks.add(tick)
                
                if self.include_numbers:
                    label = Text(
                        f"{x:.{self.decimal_places}f}", 
                        font_size=TICK_FONT_SIZE, 
                        color=TICK_COLOR
                    )
                    label.next_to(tick, DOWN, buff=0.15)
                    self.labels.add(label)
        
        # 子刻度
        self.sub_ticks = VGroup()
        self.sub_labels = VGroup()
        
        if sub_tick_range is not None:           
            self.add_sub_ticks(
                self.sub_tick_range[0], 
                self.sub_tick_range[1], 
                sub_tick_step,
                animate=True
            )
        
        # 添加所有组件
        self.add(
            self.line, 
            self.ticks, 
            self.labels,
            self.sub_ticks, 
            self.sub_labels,
            self.seq_dots, 
            self.seq_labels,
            self.function_dots,
            self.function_labels
        )
    
    def _x2pos(self, x: float) -> np.ndarray:
        """将数学坐标 x 转换为 Manim 坐标"""
        return self.center_offset + RIGHT * x * self.scale_factor
    
    def add_sub_ticks(
        self, 
        start: float,   # 子刻度起始位置
        end: float,     # 子刻度结束位置
        step: float = 0.1,   # 子刻度间隔，默认为0.1
        animate: bool = False,  # 是否启用动画效果，默认为False
        scene: Optional[Scene] = None,  # 传入Scene以执行动画
        font_size =SUB_TICK_FS,
        include_numbers:bool = True
    ):
        """在指定区间添加子刻度"""
        if step <= 0:
            return
        
        # # 移除现有子刻度（如果需要重新创建）
        # if animate and scene is not None:
        #     scene.play(FadeOut(self.sub_ticks), FadeOut(self.sub_labels), run_time=ANIM_TIME/2)
        #     print("===========>>Removed existing sub ticks with animation.")
        #     self.sub_ticks = VGroup()
        #     self.sub_labels = VGroup()
        
        # 添加新的子刻度
        x_values = np.arange(start, end + step, step)

        for x in x_values:
            if abs(x - round(x)) < 1e-5: continue # 避免浮点精度问题                

            if self.x_min <= x <= self.x_max:
                tick = Line(
                    UP * self.sub_tick_length/2, 
                    DOWN * self.sub_tick_length/2, 
                    color=SUB_TICK_COLOR
                )
                tick.move_to(self._x2pos(x))
                self.sub_ticks.add(tick)
                             
                if include_numbers:
                    label = Text(
                        f"{x:.1f}", 
                        font_size=font_size, 
                        color=SUB_TICK_COLOR
                    )
                    label.next_to(tick, DOWN, buff=0.1)
                    self.sub_labels.add(label)
        
        # 更新组件
        # self.remove(self.sub_ticks, self.sub_labels)
        # self.add(self.sub_ticks, self.sub_labels)
        
        if animate and scene is not None:
            scene.play(
                FadeIn(self.sub_ticks), 
                FadeIn(self.sub_labels), 
                run_time=ANIM_TIME/2
            )

    def add_sub_ticks_2(self,
                        startPos:int = 0,
                        new_sub_ticks_range:tuple[int, int] = (0,1)):
        for i in range(new_sub_ticks_range[0], new_sub_ticks_range[1] + 1):
            pos =startPos + i * 0.1
            if abs(pos - round(pos)) < 1e-9:
                continue  # 跳过整数刻度

            t = Line(UP*0.1, DOWN*0.1, color=SUB_TICK_COLOR)
            lab = Text(f"{pos:.1f}", font_size=SUB_TICK_FS, color=SUB_TICK_COLOR)
            self.sub_ticks.add(t)
            self.sub_labels.add(lab)
            x = startPos + (i + 1) * 0.1
            t.move_to(self._x2pos(x))
            lab.next_to(t, DOWN, buff=0.15)
       
    

    def add_sequence_points(
        self, 
        n_start: int, 
        n_end: int, 
        scene: Scene, 
        func: Callable[[int], float] = lambda n: 1/n,
        label_func: Optional[Callable[[int], str]] = None,
        run_time: float = ANIM_TIME,
        lable_size:int = LABEL_FS,
        isPlay:bool = True
    ):
        """添加数列点，支持自定义函数"""
        for n in range(n_start, n_end + 1):
            a_n = func(n)
            dot = Dot(color=DOT_COLOR).move_to(self._x2pos(a_n))
            
            # 创建标签
            if label_func is not None:
                label_text = label_func(n)
            else:
                if n <= 2:
                    label_text = f"a_{{{n}}} = {a_n:.2f}"
                else:
                    label_text = f"a_{{{n}}}"
            
            # 使用MathTex或Text取决于内容
            if any(c in label_text for c in ['_', '^', '\\']):
                label = MathTex(f"\\boldsymbol{{{label_text}}}", font_size=lable_size, color=LABEL_COLOR)
            else:
                label = Text(label_text, font_size=lable_size, color=LABEL_COLOR)#, weight=BOLD)

            # 交替显示标签位置
            direction = DOWN if n % 2 == 0 else UP
            label.next_to(dot, direction, buff=0.2).align_to(dot, LEFT)
            
            self.seq_dots.add(dot)
            self.seq_labels.add(label)
            self.seq_n_values.append(n)           
            if isPlay:
                scene.play(FadeIn(dot), Write(label), run_time=run_time)
                scene.wait(run_time/2)
        
        if not isPlay:
            scene.play(FadeIn(self.seq_dots[n_start-1:n_end]), Write(self.seq_labels[n_start-1:n_end]), run_time=run_time)
    def add_function_points(
        self,
        func: Callable[[float], float],
        x_values: List[float],
        scene: Scene,
        dot_color: str = RED,
        label_func: Optional[Callable[[float], str]] = None,
        run_time: float = ANIM_TIME
    ):
        """为任意函数添加点"""
        for x in x_values:
            y = func(x)
            dot = Dot(color=dot_color).move_to(self._x2pos(y))
            
            # 创建标签
            if label_func is not None:
                label_text = label_func(x)
            else:
                label_text = f"f({x:.1f}) = {y:.2f}"
            
            if any(c in label_text for c in ['_', '^', '\\']):
                label = MathTex(label_text, font_size=LABEL_FS, color=LABEL_COLOR)
            else:
                label = Text(label_text, font_size=LABEL_FS, color=LABEL_COLOR)
            
            label.next_to(dot, UP, buff=0.2)
            
            self.function_dots.add(dot)
            self.function_labels.add(label)
            
            scene.play(FadeIn(dot), Write(label), run_time=run_time)
            scene.wait(run_time/2)
    
    def zoom_to(
        self, 
        new_scale: float, 
        new_center: Optional[np.ndarray] = None,
        new_points: Optional[Tuple[int, int]] = None,
        scene: Optional[Scene] = None, 
        run_time: float = ZOOM_TIME,
        pointLablesize:int = LABEL_FS,
        isPlayPoint:bool = True,
        sequence_func: Optional[Callable[[int], float]] = None,       
        sub_tick_range: Optional[Tuple[float, float]] = None,
        sub_tick_step: Optional[float] = None,
        otherAnimationsTicks: Optional[List[Animation]] = None,
    ):
        """缩放动画，支持中心点移动和子刻度更新"""
        if new_center is not None:
            self.center_offset = new_center
       
        # 创建动画列表
        anims = []
        old_scale = self.scale_factor
        self.scale_factor = new_scale
        
        # 更新数轴线条
        new_line = Line(
            self._x2pos(self.x_min), 
            self._x2pos(self.x_max), 
            color=TICK_COLOR
        )
        anims.append(Transform(self.line, new_line))
        
        # 更新主刻度及其标签
        
        for x, tick, lab in zip(range(self.x_min, self.x_max + 1),
                                self.ticks, self.labels):            
            anims += [
                tick.animate.move_to(self._x2pos(x)),
                lab.animate.next_to(self._x2pos(x), DOWN, buff=0.3)
            ]
        
        
        # 更新子刻度及其标签
        for (tick, lab) in zip(self.sub_ticks, self.sub_labels):
            x =float(lab.text)
            anims += [
                tick.animate.move_to(self._x2pos(x)),
                lab.animate.next_to(self._x2pos(x), DOWN, buff=0.15)
            ]
        
        
        # # 更新子刻度标签
        # for label in self.sub_labels:
        #     try:
        #         # 确保我们处理的是单个标签而不是数组
        #         x_text = label.text if hasattr(label, 'text') else ""
        #         x = float(x_text)
        #         new_label = Text(
        #             f"{x:.1f}", 
        #             font_size=SUB_TICK_FS, 
        #             color=SUB_TICK_COLOR
        #         ).next_to(self._x2pos(x), DOWN, buff=0.1)
        #         anims.append(Transform(label, new_label))
        #     except (ValueError, AttributeError):
        #         pass
        
        # 更新数列点
        for dot, n in zip(self.seq_dots, self.seq_n_values):
            a_n = sequence_func(n) if sequence_func is not None else 1/n
            new_dot = Dot(color=dot.get_color()).move_to(self._x2pos(a_n))
            anims.append(Transform(dot, new_dot))
        
        # 更新数列标签
        for label, dot, n in zip(self.seq_labels, self.seq_dots, self.seq_n_values):
            a_n = sequence_func(n) if sequence_func is not None else 1/n
            direction = DOWN if n % 2 == 0 else UP
            if n <= 3 and sequence_func is None:
                label_text = f"a_{{{n}}} = {a_n:.2f}"
            else:
                label_text = f"a_{{{n}}}"
            
            if any(c in label_text for c in ['_', '^', '\\']):
                new_label = MathTex(label_text, font_size=pointLablesize, color=LABEL_COLOR)
            else:
                new_label = Text(label_text, font_size=pointLablesize, color=LABEL_COLOR)
            
            new_label.next_to(self._x2pos(a_n), direction, buff=0.2)
            anims.append(Transform(label, new_label))
        
        # 更新函数点
        for dot in self.function_dots:
            x = self._pos2x(dot.get_center())
            new_dot = Dot(color=dot.get_color()).move_to(self._x2pos(x))
            anims.append(Transform(dot, new_dot))
        
        # 更新函数标签
        for label, dot in zip(self.function_labels, self.function_dots):
            x = self._pos2x(dot.get_center())
            # 安全地获取标签文本
            if hasattr(label, 'tex_string'):
                label_text = label.tex_string
            elif hasattr(label, 'text'):
                label_text = label.text
            else:
                label_text = ""
                
            if any(c in label_text for c in ['_', '^', '\\']):
                new_label = MathTex(label_text, font_size=LABEL_FS, color=LABEL_COLOR)
            else:
                new_label = Text(label_text, font_size=LABEL_FS, color=LABEL_COLOR)
            
            new_label.next_to(self._x2pos(x), UP, buff=0.2)
            anims.append(Transform(label, new_label))
        
        if otherAnimationsTicks is not None:
            anims.append(otherAnimationsTicks)

        # 执行动画
        if scene is not None:
            scene.play(*anims, run_time=run_time)
            
            # 添加子刻度（如果需要）
            if sub_tick_range is not None and sub_tick_step is not None:
                self.add_sub_ticks(
                    sub_tick_range[0], 
                    sub_tick_range[1], 
                    sub_tick_step, 
                    animate=True, 
                    scene=scene
                )
            
            # 添加新点（如果需要）
            if new_points is not None:
                self.add_sequence_points(
                    new_points[0], 
                    new_points[1],
                    scene=scene,                     
                    func=sequence_func if sequence_func is not None else lambda n: 1/n,                   
                    run_time=run_time/2,
                    lable_size=pointLablesize,
                    isPlay=isPlayPoint
                )
    
    def _pos2x(self, pos: np.ndarray) -> float:
        """将 Manim 坐标转换为数学坐标 x"""
        # 确保我们处理的是单个坐标而不是数组
        if isinstance(pos, np.ndarray):
            return (pos[0] - self.center_offset[0]) / self.scale_factor
        else:
            # 如果 pos 不是数组，直接返回
            return pos

class DemoScene(Scene):
    def construct(self):
        title = Text(TITLE_TEXT, font_size=TITLE_SIZE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # 创建数轴
        axis = EnhancedNumberAxis(
            x_range=(-5, 10, 1),
            sub_tick_step=0.1,
            sub_tick_range=None,
            initial_scale=1.5,
            center=LEFT * 2 + DOWN
        )
        self.play(Create(axis))
        # self.wait(1)
        
        # 添加数列点
        # axis.add_sequence_points(1, 5, self)
        # self.wait(1)
        axis.add_sub_ticks(-1,1,animate=True,scene=self)
        # axis.add_sub_ticks(0,1,animate=True,scene=self)
        # axis.add_sub_ticks(1,2,animate=True,scene=self)
        # self.play(FadeIn(axis.sub_ticks), FadeIn(axis.sub_labels))
        # 第一次缩放
        axis.zoom_to(
            new_scale=7.0,
            new_center=LEFT * .7 + UP,
            new_points=(1,7),
            scene=self,           
            sub_tick_range=None,
            sub_tick_step=.1,
            sequence_func=lambda n: np.sin(n)/n
        )
        # axis.add_function_points(
        #     func=lambda x: np.sin(x),
        #     x_values=[0.1, 0.2, 0.3, 0.4, 0.5],
        #     scene=self,
        #     dot_color=GREEN,
        #     label_func=lambda x: f"\\sin({x:.1f}) = {np.sin(x):.2f}"
        # )
         # 第二次缩放
        axis.zoom_to(new_scale=21,scene=self,new_points=(8,13))
        axis.zoom_to(new_scale=11,scene=self)
        axis.zoom_to(new_scale=5,scene=self)
        axis.zoom_to(new_scale=5,new_center=DOWN+LEFT,scene=self)
        # self.wait(1)
        
        # # 添加函数点
        # axis.add_function_points(
        #     func=lambda x: np.sin(x),
        #     x_values=[0.1, 0.2, 0.3, 0.4, 0.5],
        #     scene=self,
        #     dot_color=GREEN,
        #     label_func=lambda x: f"\\sin({x:.1f}) = {np.sin(x):.2f}"
        # )
        # self.wait(1)
        
        # # 第二次缩放
        # axis.zoom_to(
        #     new_scale=8.0,
        #     new_center=DOWN * 0.5 + RIGHT * 0.2,
        #     scene=self,
        #     add_sub_ticks=True,
        #     sub_tick_range=(0, 0.2),
        #     sub_tick_step=0.05
        # )
        # self.wait(2)