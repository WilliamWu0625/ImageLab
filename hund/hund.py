a=Animation()

yellow=(225,225,102)
brown=(139,69,19)
gray=(128,128,128)

def ears(color):
    m[0][1]=color
    m[0][2]=color
    m[0][6]=color
    m[0][7]=color

def face(color):
    m[1][3]=color
    m[1][4]=color
    m[1][5]=color
    m[2][2]=color
    m[2][6]=color
    m[3][1]=color
    m[3][1]=color
    m[3][7]=color
    m[4][1]=color
    m[4][7]=color
    m[5][1]=color
    m[5][7]=color
    m[6][0]=color
    m[6][7]=color
    m[7][6]=color

def eyes(color):
    m[3][3]=color
    m[3][5]=color

def nose_mouth(color):
    m[4][4]=color
    m[5][4]=color

def move_ears(color):
    m[1][0]=color
    m[0][7]=off
    m[1][7]=color

def move_face(color):
    m[6][0]=off
    m[7][6]=off
    m[7][7]=color
    m[6][2]=color

def move_mouth(color):
    m[5][3]=color
    m[5][5]=color

ears(brown)
face(yellow)
eyes(gray)
nose_mouth(brown)

a.add_frame(m)

move_ears(brown)
move_face(yellow)
move_mouth(brown)
    
a.add_frame(m)
