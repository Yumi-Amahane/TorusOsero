import string
import numpy as np

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
    
def PutStone(Square,x,y,color):
    if len(Square)<=y or len(Square[0])<=x or Square[y][x]!=" ":
        return [Square,-1]
    
    return [Square,0]

def checkCanPut(square,Turn):
    H=len(square)
    W=len(square[0])
    if Turn%2==0:
        color="B"
    else:
        color="W"

    Res=[[[]for i in range(W)]for j in range(H)]

    for cy in range(H):
        for cx in range(W):
            if square[cy][cx]==".":
                #右
                #print(cx,cy,"isdot")
                ResRev=[]#リバースのリザーブ
                for ix in range(cx+1,W):
                    #print(cx,cy,square[cy][ix])
                    if square[cy][ix]==".":
                        break
                        #空欄有ったらひっくり返らないものね
                    if square[cy][ix]==color:
                        for rev in ResRev:
                            Res[cy][cx].append(rev)
                        break
                    else:
                        ResRev.append([ix,cy])

                #左
                ResRev=[]#リバースのリザーブ
                for ix in range(cx-1,-1,-1):
                    #print(cx,cy,square[cy][ix])
                    if square[cy][ix]==".":
                        break
                        #空欄有ったらひっくり返らないものね
                    if square[cy][ix]==color:
                        for rev in ResRev:
                            Res[cy][cx].append(rev)
                        break
                    else:
                        ResRev.append([ix,cy])



                #下
                ResRev=[]#リバースのリザーブ
                for iy in range(cy+1,H):
                    #print(cx,cy,square[cy][ix])
                    if square[iy][cx]==".":
                        break
                        #空欄有ったらひっくり返らないものね
                    if square[iy][cx]==color:
                        for rev in ResRev:
                            Res[cy][cx].append(rev)
                        break
                    else:
                        ResRev.append([cx,iy])

                #左
                ResRev=[]#リバースのリザーブ
                for iy in range(cy-1,-1,-1):
                    #print(cx,cy,square[cy][ix])
                    if square[iy][cx]==".":
                        break
                        #空欄有ったらひっくり返らないものね
                    if square[iy][cx]==color:
                        for rev in ResRev:
                            Res[cy][cx].append(rev)
                        break
                    else:
                        ResRev.append([cx,iy])


                #右下
                #print(cx,cy,"isdot")
                ResRev=[]#リバースのリザーブ
                c=1
                while(cx+c<W and cy+c<H):
                    #print("みぎした",c)
                    #print(cx,cy,square[cy][ix])
                    if square[cy+c][cx+c]==".":
                        break
                        #空欄有ったらひっくり返らないものね
                    if square[cy+c][cx+c]==color:
                        for rev in ResRev:
                            Res[cy][cx].append(rev)
                        break
                    else:
                        ResRev.append([cx+c,cy+c])
                    c+=1

                #左下
                #print(cx,cy,"isdot")
                ResRev=[]#リバースのリザーブ
                c=1
                while(0<cx-c and cy+c<H):
                    #print(cx,cy,square[cy][ix])
                    if square[cy+c][cx-c]==".":
                        break
                        #空欄有ったらひっくり返らないものね
                    if square[cy+c][cx-c]==color:
                        for rev in ResRev:
                            Res[cy][cx].append(rev)
                        break
                    else:
                        ResRev.append([cx-c,cy+c])

                    c+=1

                #左上
                #print(cx,cy,"isdot")
                ResRev=[]#リバースのリザーブ
                c=1
                while(0<cx-c and 0<cy-c):
                    #print(cx,cy,square[cy][ix])
                    if square[cy-c][cx-c]==".":
                        break
                        #空欄有ったらひっくり返らないものね
                    if square[cy-c][cx-c]==color:
                        for rev in ResRev:
                            Res[cy][cx].append(rev)
                        break
                    else:
                        ResRev.append([cx-c,cy-c])

                    c+=1

                #右上
                #print(cx,cy,"isdot")
                ResRev=[]#リバースのリザーブ
                c=1
                while(cx+c<W and 0<cy-c):
                    #print(cx,cy,square[cy][ix])
                    if square[cy-c][cx+c]==".":
                        break
                        #空欄有ったらひっくり返らないものね
                    if square[cy-c][cx+c]==color:
                        for rev in ResRev:
                            Res[cy][cx].append(rev)
                        break
                    else:
                        ResRev.append([cx+c,cy-c])

                    c+=1


            if len(Res[cy][cx])!=0:
                print(cx,cy,Res[cy][cx])
    return Res

Square=Reset(3,2)
#draw(Square)
Turn=0
Color=["B","W"]
while(True):#Turn==0):
    Turn+=1
    print()
    draw(Square)


    Revlist=checkCanPut(Square,Turn)
    S=0
    for y in (Revlist):
        for x in (y):
            S+=len(x)
    if S==0:
        Revlist=checkCanPut(Square,Turn+1)
        for y in (Revlist):
            for x in (y):
                S+=len(x)
        if S==0:
            break
        else:
            print("Cannot put "+Color[Turn%2]+" Stone")
            print("Press any key to continue")
            input()
            continue
    #print(S)
    print("put a "+Color[Turn%2]+" Stone")

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