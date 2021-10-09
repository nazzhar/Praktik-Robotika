from controller import Robot
 
tembok = 2

def maju():
    rightmotor.setVelocity(4.5)
    leftmotor.setVelocity(4.5)
def hari():
    rightmotor.setVelocity(4)
    leftmotor.setVelocity(-4)
def hanan():
    rightmotor.setVelocity(-4)
    leftmotor.setVelocity(4)
def diam():
    rightmotor.setVelocity(0)
    leftmotor.setVelocity(0)
def sebelum_tembok():
    if garis_kanan > 1400 and garis_kiri < 1400:
        hari()
    elif garis < 1200:
        maju()
    elif garis_kanan < 1400 and garis_kiri > 1400:
        hanan()
    elif garis_kirii < 500:
        diam()
        hari()
def setelah_tembok():
    if garis_kanan > 1400 and garis_kiri < 1400:
        hari()
    elif garis_kanan < 1400 and garis_kiri > 1400:
        hanan()
    elif garis_kanann < 500 :
        hanan()
    elif ping_depan > 200:
        maju()
    elif ping_depan < 200:
        diam()
    else :
        maju()
def ditembok():
    if (garis > 3600 and ping_kanan < 1000) or (garis > 3600 and ping_kiri < 1000):
        maju()
def palang():
    if garis_kanann < 500 and garis_kirii > 600:
        hanan()
    elif garis_kanann < 500 and garis_kanann > 350 and garis_kirii < 600 and garis_kirii > 350 and ping_depan > 200:
        maju()   
    elif ping_depan < 200:
        diam()
    elif garis_kanann < 350 and garis_kirii < 350:
        diam()     
         
robot = Robot()

timestep = int(robot.getBasicTimeStep())

leftmotor = robot.getDevice('motor_1')
rightmotor = robot.getDevice('motor_2')
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))

pingkiri = robot.getDevice('ds_left')
pingkanan = robot.getDevice('ds_right')
pingdepan = robot.getDevice('ds_front')


irl2 = robot.getDevice('IRL2')
irl1 = robot.getDevice('IRL1')
ircl = robot.getDevice('IRCL')
ircr = robot.getDevice('IRCR')
irr1 = robot.getDevice('IRR1')
irr2 = robot.getDevice('IRR2')

irl2.enable(timestep)
irl1.enable(timestep)
ircl.enable(timestep)
ircr.enable(timestep)
irr1.enable(timestep)
irr2.enable(timestep)
pingkiri.enable(timestep)
pingkanan.enable(timestep)
pingdepan.enable(timestep)

while robot.step(timestep) != -1:  
    rightmotor.setVelocity(10)
    leftmotor.setVelocity(10)
    
     
    irl2_val = irl2.getValue()
    irl1_val = irl1.getValue()
    ircl_val = ircl.getValue()
    ircr_val = ircr.getValue()
    irr1_val = irr1.getValue()
    irr2_val = irr2.getValue()
    ping_kanan = pingkanan.getValue()
    ping_kiri = pingkiri.getValue()
    ping_depan = pingdepan.getValue()

    garis_kanann = irr1_val + irr2_val
    garis_kirii = irl1_val + irl2_val
    garis_kanan = ircr_val + irr1_val + irr2_val
    garis_kiri = ircl_val + irl1_val + irl2_val
    garis_tengah = ircr_val + ircl_val
    garis = garis_kanan + garis_kiri
    
    
    print ('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format (garis_kirii, garis_tengah, garis_kanann, garis_kiri, garis_kanan, tembok))
   

    if tembok == 2:
        sebelum_tembok()
        ditembok()
        if garis < 3000 and ping_kiri < 1000:
            tembok = 3 
    elif tembok == 3:
        setelah_tembok()
        if ping_kanan < 900:
            tembok = 4
    elif tembok == 4:
        palang()

       
       
        
        
        

   
            
         