from manim import*
_color_1="#39c5bb"  
_color_2="#C1003C"  
_color_3="#11999e"
_color_4=ManimColor("#ff2e63")
_color_5="#79D87E"
_color_6="#fff4e1"
_color_7="#ffaaa5"
_color_8="#b9d7ea"
_color_9="#7dace4"

font_2="得意黑"
# font_2="文悦新青年体 (须授权)"

class AnimeTools(Scene):
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
        ) , title_back

    def EmphasizeTexts(self,targets,color:str=YELLOW,stroke_width=4,buff=0):
        animes=[]
        recs=VGroup()
        for target in targets:        
            rec_target=Circumscribe(target,color=color,stroke_width=stroke_width,buff=buff)
            animes.append(rec_target)
            rec2_target=SurroundingRectangle(target,color=color,
                                             stroke_width=stroke_width,
                                             buff=buff)
            animes.append(Create(rec2_target))
            recs.add(rec2_target)
        
        self.play(LaggedStart(*animes,lag_ratio=.3))
        return recs

def TempfunCtion(self):
    pass