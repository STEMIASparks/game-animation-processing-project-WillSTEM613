def setup():
    size(1000,1000)
    background(255)

#variables
ypos= 500
xpos= 500
resi=50
cur=10
sp=0
i = 0
vel = 10
s=1
sec = 0
pf = 0
x = 10
y = 10
sz = 10
gravDir = 0
gravSp = 0.0913

#centering
xpos -= resi/2
ypos -= resi/2

#play area box
def border():
    fill(0)
    rect(225,225,550,550,10)
    fill(255)
    rect(250,250,500,500,10)

#pixelfinder(pF)
def pixelFinder():
    fill(132)
    rect(x,y,10,10)

#draw
def draw():
    global  ypos,xpos,resi,cur,sp,s,sec,pf,gravDir,gravSp,vel
    background(255)
    border()
    fill(0)
    rect(xpos,ypos,resi,resi,cur)
    
    #if gravDir goes over or under 
    if gravDir == -1:
        gravDir = 3
    if gravDir == 4:
        gravDir = 0
    
    if pf == 1:
        pixelFinder()
    
    #gravity
    if gravDir == 0:
        sp += gravSp
        ypos += sp
    if gravDir == 1:
        sp += gravSp
        ypos -= sp
    if gravDir == 2:
        sp += gravSp
        xpos += sp
    if gravDir == 3:
        sp += gravSp
        xpos -= sp
        
        
    #if touching walls
    if ypos >= 700 and gravDir == 0:
        sp=0
    if xpos >= 700 and gravDir == 2:
        sp=0
    if ypos <= 250 and gravDir == 1:
        sp=0
    if xpos <= 250 and gravDir == 3:
        sp=0
  
            
    #stopping touching walls
    if xpos <= 250 and s == 1:
        xpos = 250
    if xpos >= 700 and s == 1:
        xpos = 700
    if ypos >= 700 and s == 1:
        ypos = 700
    if ypos <= 250 and s == 1:
        ypos = 250
    
    #text
    textSize(25)
    text("gimme good mark",500,90)
    
    print(x,y,pf,gravDir,sp,xpos,ypos)
    
#keystrokes 
def keyPressed():
    global ypos,sp,xpos,vel,s,pf,x,y,gravDir
    if key == 'r':
        gravDir -= 1
    if key == 't':
        gravDir += 1
    if key == 'v':
        if pf == 1:
            pf = 0
        elif pf == 0:
            pf = 1
    #player
    if pf == 0:
        if key == 's':
            ypos += vel
            s=1
        if key == 'a':
            xpos -= vel
            s=1
        if key == 'w':
            ypos -= vel
            s=1
        if key == 'd':
            xpos += vel
            s=1
        if key == 'e':
            xpos += vel
            ypos -= vel
            s=1
        if key == 'q':
            xpos -= vel
            ypos -= vel
            s=1
    #pixelFinder
    if pf == 1:
        if key == 'w':
            y -= 10
        if key == 's':
            y += 10
        if key == 'a':
            x -= 10
        if key == 'd':
            x += 10
