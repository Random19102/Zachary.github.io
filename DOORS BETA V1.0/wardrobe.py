class wardrobe(Entity):
    global incloset,timer
    incloset=False
    timer=0
    def __init__(self,**kwargs):
        super().__init__(parent=scene, collider='box', x=10, origin_y=0.75, model='wardrobe_simple', texture='wood.jpg', **kwargs)
    def input(self, key):
        global incloset,timer
        if self.hovered==True:
            if key=='e' and not incloset and timer==0:
                player.y=3
                player.x=self.x
                player.z=self.z
                incloset=True
                def Timer():
                    global timer
                    timer+=1
                invoke(Timer, delay=0.5)
            if key=='e' and incloset and timer==1:
                incloset=False
                player.y=3
                player.x=self.x-5
                player.z=self.z
                def Timer1():
                    global timer
                    timer-=1
                invoke(Timer1, delay=0.5)