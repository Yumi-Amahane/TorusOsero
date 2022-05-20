from msilib.schema import Directory
from msvcrt import kbhit


def Reset(W,H):
    halfW=int(W/2)
    halfH=int(H/2)
    Square=[["." for i in range(W)] for j in range(H)]
    Square[halfH][halfW]="W"
    Square[halfH-1][halfW-1]="W"
    Square[halfH-1][halfW]="B"
    Square[halfH][halfW-1]="B"

    return (Square)

def draw(square):
    Horizon=" "
    for i in range(len(square[0])):
        Horizon+=str(i)+" "
    print(Horizon)

    for c,i in enumerate(square):
        Horizon=str(c)
        for j in i:
            Horizon+=j+" "
        print(Horizon)


def checkCanPut(square,Turn):
    H=len(square)
    W=len(square[0])
    Color=["B","W"]

    Res=[[[]for i in range(W)]for j in range(H)]

    for cy in range(H):
        for cx in range(W):
            if square[cy][cx]==".":
                c=0
                #direction=[True,True,True,True,True,True,True,True]

                direction=[True for i in range(8)]
                RevReses=[[] for i in range (8)]
                #8方向に判定を伸ばせるかの判定上から時計回りで
                while (sum(direction)!=0):
                    c+=1

                    for D in range(8):
                        if direction[D]==True:

                            if D==0:#上
                                Checkx=cx
                                Checky=cy-c
                                while Checky<0:
                                    Checky+=H
                                    #print("TorusCheck",Checkx," ",Checky)

                            if D==1:#右上
                                Checkx=cx+c
                                Checky=cy-c
                                while W<=Checkx:
                                    Checkx-=(W)
                                while Checky<0:
                                    Checky+=H

                            if D==2:#右
                                Checkx=cx+c
                                Checky=cy
                                while W<=Checkx:
                                    Checkx-=(W)

                            if D==3:#右下
                                Checkx=cx+c
                                Checky=cy+c
                                while W<=Checkx:
                                    Checkx-=(W)
                                while H<=Checky:
                                    Checky-=H

                            if D==4:#下
                                Checkx=cx
                                Checky=cy+c
                                while H<=Checky:
                                    Checky-=H

                            if D==5:#左下
                                Checkx=cx-c
                                Checky=cy+c
                                while Checkx<0:
                                    Checkx+=(W)
                                while H<=Checky:
                                    Checky-=H

                            if D==6:#左
                                Checkx=cx-c
                                Checky=cy
                                while Checkx<0:
                                    Checkx+=(W)

                            if D==7:#左上
                                Checkx=cx-c
                                Checky=cy-c
                                while Checkx<0:
                                    Checkx+=(W)
                                while Checky<0:
                                    Checky+=H
                                
                                
                            if square[Checky][Checkx]==".":
                                direction[D]=False
                            if square[Checky][Checkx]==Color[Turn%2] or (Checky==cy and Checkx==cx):
                                for Rev in (RevReses[D]):
                                    if (Rev in Res[cy][cx])==False:
                                        Res[cy][cx].append(Rev)
                                direction[D]=False
                            if square[Checky][Checkx]==Color[Turn%2-1]:
                                RevReses[D].append([Checkx,Checky])



            if len(Res[cy][cx])!=0:
                print(cx,cy,Res[cy][cx])
    return Res


Square=Reset(6,6)
#draw(Square)
Turn=0
Color=["B","W"]
while(True):#Turn==0):
    Turn+=1
    print()
    draw(Square)


    Revlist=checkCanPut(Square,Turn)
    S=0
    #print(len(Revlist))
    #print(len(Revlist[0]))

    for y in (Revlist):
        for x in (y):
            S+=len(x)
            #print((x),S)
    if S==0:
        print("Cannot put "+Color[Turn%2]+" Stone")
        print("Press Enter key to continue")
        input()
        
        Revlist=checkCanPut(Square,Turn+1)
        for y in (Revlist):
            for x in (y):
                S+=len(x)
        if S==0:
            print("Cannot put "+Color[Turn%2-1]+" Stone")
            break
        else:
            continue
    #print(S)
    print("put a "+Color[Turn%2]+" Stone")

    Count=[0,0]
    for y in (Square):
        for x in (y):
            if x=="W":
                Count[0]+=1
            if x=="B":
                Count[1]+=1

    print("W-B")
    print(str(Count[0])+"-"+str(Count[1]))

    Input=input()
    while ((" " in Input)==False):
        Input=input()
    
    x,y=[int(x) for x in Input.split()]
    #print(x,y)

    if len(Revlist[y][x])==0:
        print("Cannot put a stone")
        Turn-=1

    else:
        Square[y][x]=Color[Turn%2]
        for Rev in Revlist[y][x]:
            Square[Rev[1]][Rev[0]]=Color[Turn%2]

#draw(Square)

Count=[0,0]
for y in (Square):
    for x in (y):
        if x=="W":
            Count[0]+=1
        if x=="B":
            Count[1]+=1

print("W-B")
print(str(Count[0])+"-"+str(Count[1]))