class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions={'up':[0,1,'left','right']
                    ,'left':[-1,0,'down','up']
                    ,'down':[0,-1,'right','left']
                    ,'right':[1,0,'up','down']
        }
        dire='up'
        from collections import namedtuple
        obstacles=set(map(tuple,obstacles))
        x=0
        y=0
        res=0
        for command in commands:
            if(command>0):
                for step in range(command):
                    if((x+directions[dire][0],y+directions[dire][1]) not in obstacles):
                        x+=directions[dire][0]
                        y+=directions[dire][1]
                        res=max(res,x**2+y**2)
                    else:
                        break
            elif(command==-1):
                dire=directions[dire][3]
            else:
                dire=directions[dire][2]
        return res