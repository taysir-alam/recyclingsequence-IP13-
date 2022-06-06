ID = ''
#main function
# Written by Taysir Alam
def main():
    # calls all other functions
    # count to repeat cycle infenitely 
    global count
    count = 0
    while True:
        count == 0
    
        dispense_container()
        time.sleep(1)
        load_container()
        time.sleep(1)
        transfer_container()
        return_home()
        count = count+1


#function to dispense container
# Written by Qaosain Ahmad
def dispense_container():
    #define variables for new dispensed containers 
    global new
    global new1
    global new2
    #dispesne container and store properties on first run
    if count == 0:
        num = table.dispense_container(random.randint(1,6),True)
        global mass
        global ID
        mass = num[1]
        ID = num[2]
        print(ID)
        print(mass)
        time.sleep(1)

    # assign appropiate properties if it is not the first cycle
    else:
        if con == 1:
            ID = new[2]
        elif con == 2:
            ID = new1[2]
        elif con == 3:
            ID = new2[2] 
        
        exit

#function to load the container
#Written By Taysir Alam
def load_container():
    # assign variables for dispensing new containers after drop off
    global new
    global new1
    global new2
    # variable to know which bin was last dispensed 
    global con
    con = 0
    global ID
    global mass
    #dropoff and pickup locations
    dropoff = [(-0.099,-0.531,0.508),(-0.02,-0.54,0.508),(0.061,-0.537,0.508)]
    pickup = (0.615,0.0,0.28)
    mid = (-0.0,-0.246,0.825)

    # picking up first container
    bot.rotate(45)
    time.sleep(0.4)
    bot.rotate(45)
    time.sleep(0.4)
    bot.rotate(5)
    time.sleep(0.4)
    bot.rotate(5)
    arm.move_arm(0.615,0.0,0.28)
    time.sleep(2)
    arm.control_gripper(45)
    time.sleep(2)
    arm.move_arm(-0.0,-0.246,0.825)
    time.sleep(2)
    arm.move_arm(-0.09,-0.54,0.508)
    arm.control_gripper(-15)
    time.sleep(2)
    arm.rotate_shoulder(-50)
    arm.move_arm(-0.0,-0.246,0.825)
    arm.home()
    time.sleep(1)
    new = table.dispense_container(random.randint(1,6),True)
    print(new[2])
    Tmass = mass + new[1]
    print('Total Mass:' + Tmass)
    con = 1


    #pickup second container if ID mathces
    if str(new[2]) == str(ID) and Tmass < 90 :
        con = 2
        arm.move_arm(0.615,0.0,0.28)
        time.sleep(2)
        arm.control_gripper(45)
        time.sleep(2)
        arm.move_arm(-0.0,-0.246,0.825)
        time.sleep(2)
        arm.move_arm(-0.02,-0.54,0.508)
        arm.control_gripper(-15)
        time.sleep(2)
        arm.rotate_shoulder(-50)
        arm.move_arm(-0.0,-0.246,0.825)
        arm.home()
        time.sleep(1)
        new1 = table.dispense_container(random.randint(1,6),True)
        print(new1[2])
        #check if mass limit it met
        Tmass = Tmass + new1[1]
        print('Total Mass:' + Tmass)
        if Tmass > 90:
            
            exit
        #pickup third container if ID mathces
        if str(new1[2]) == str(new[2]) and Tmass < 90:
            con = 3
            arm.move_arm(0.615,0.0,0.28)
            time.sleep(2)
            arm.control_gripper(45)
            time.sleep(2)
            arm.move_arm(-0.0,-0.246,0.825)
            time.sleep(2)
            arm.move_arm(0.043, -0.545, 0.508)
            arm.control_gripper(-15)
            time.sleep(2)
            arm.rotate_shoulder(-50)
            arm.move_arm(-0.0,-0.246,0.825)
            arm.home()
            time.sleep(1)
            new2 = table.dispense_container(random.randint(1,6),True)
            print(new2[2])
            #make sure mass limit is met
            Tmass = Tmass + new2[1]
            print('Total Mass:' + Tmass)
            if Tmass > 90:
                
                
                exit
            
            exit
        else:
            
            exit
    else:
        
        exit
   
    #adjustments for bot to leave            
    bot.rotate(-45)
    time.sleep(0.5)
    bot.rotate(-45)
    bot.rotate(-5)
    bot.rotate(-5)



    
#function to transfer container
# Written By Qaosain Ahmad
def transfer_container():
    #print bin destination 
    print('Destination:' + ID)
    time.sleep(2)
    bot.activate_ultrasonic_sensor()
    time.sleep(1)
    # instruction for bot to stop and deposit at bin 1
    if ID == 'Bin01':
        while True:
            # While bot is moving print sensor readings
            # stop when sensor reading is correct for appropiate bin
            reading = bot.read_ultrasonic_sensor()
            print(str(reading))
            if '0.37' >= str(reading) >= '0.35':
                bot.stop()
                bot.rotate(-45)
                time.sleep(0.5)
                bot.rotate(-40)
                bot.rotate(1)
                bot.travel_forward(0.13)
                bot.rotate(45)
                time.sleep(0.4)
                bot.rotate(50)
                time.sleep(1)
                deposit_container()
                bot.rotate(45)
                time.sleep(1)
                bot.rotate(45)
                time.sleep(1)
                bot.forward_time(2.9)
                bot.rotate(-45)
                bot.rotate(-45)
                bot.deactivate_ultrasonic_sensor()
                break
             # code for linefollowing during transfer
            left, right = bot.line_following_sensors()  
            if left == 1 and right == 1:
                bot.set_wheel_speed([0.1,0.1])
            elif left == 1 and right == 0:
                bot.set_wheel_speed([0,0.02])
                time.sleep(0.01)
            elif left == 0 and right == 1:
                bot.set_wheel_speed([0.02,0])
                time.sleep(0.1)
            elif left or right != 1:
                bot.set_wheel_speed([0.01,0.05])
    # instruction for bot to stop and deposit at bin 2  
    elif ID == 'Bin02':
        while True:
            # While bot is moving print sensor readings
            # stop when sensor reading is correct for appropiate bin
            reading1 = bot.read_ultrasonic_sensor()
            print(str(reading1))
            time.sleep(0.1)
            if '0.23' >= str(reading1) >= '0.21':
                bot.stop()
                bot.rotate(-45)
                time.sleep(0.5)
                bot.rotate(-45)
                bot.rotate(1)
                bot.travel_forward(0.13)
                bot.rotate(45)
                time.sleep(0.4)
                bot.rotate(45)
                time.sleep(1)
                bot.rotate(5)
                deposit_container()
                bot.rotate(45)
                time.sleep(1)
                bot.rotate(45)
                time.sleep(0.5)
                bot.rotate(5)
                time.sleep(1)
                bot.forward_time(1.5)
                bot.rotate(-45)
                bot.rotate(-45)
                bot.deactivate_ultrasonic_sensor()
                break
             # code for linefollowing during transfer
            left, right = bot.line_following_sensors()  
            if left == 1 and right == 1:
                bot.set_wheel_speed([0.1,0.1])
            elif left == 1 and right == 0:
                bot.set_wheel_speed([0,0.02])
                time.sleep(0.01)
            elif left == 0 and right == 1:
                bot.set_wheel_speed([0.02,0])
                time.sleep(0.1)
            else:
                bot.set_wheel_speed([0.01,0.05])
            
    # instructions for bot to stop and deposit at bin 3
    elif ID == 'Bin03':
        while True:
            # While bot is moving print sensor readings
            # stop when sensor reading is correct for appropiate bin
            reading2 = bot.read_ultrasonic_sensor()
            print(str(reading2))
            time.sleep(0.1)
            if '0.14' >= str(reading2) >= '0.12':
                bot.stop()
                bot.rotate(-45)
                time.sleep(0.5)
                bot.rotate(-40)
                bot.rotate(1)
                bot.travel_forward(0.13)
                bot.rotate(45)
                time.sleep(0.4)
                bot.rotate(55)
                time.sleep(1)
                deposit_container()
                bot.rotate(45)
                time.sleep(1)
                bot.rotate(45)
                time.sleep(0.5)
                bot.rotate(5)
                time.sleep(1)
                bot.forward_time(0.5)
                bot.rotate(-45)
                bot.rotate(-45)
                bot.deactivate_ultrasonic_sensor()
                break
             # code for linefollowing during transfer
            left, right = bot.line_following_sensors()  
            if left == 1 and right == 1:
                bot.set_wheel_speed([0.1,0.1])
            elif left == 1 and right == 0:
                bot.set_wheel_speed([0,0.02])
                time.sleep(0.01)
            elif left == 0 and right == 1:
                bot.set_wheel_speed([0.02,0])
                time.sleep(0.1)
            else:
                bot.set_wheel_speed([0.01,0.05])
                
    # instruction for bot to stop and deposit at bin 4
    elif ID == 'Bin04':
        while True:
            # While bot is moving print sensor readings
            # stop when sensor reading is correct for appropiate bin
            reading3 = bot.read_ultrasonic_sensor()
            print(str(reading3))
            time.sleep(0.1)
            if '0.04' >= str(reading3) >= '0.02':
                bot.stop()
                bot.rotate(6)
                bot.deactivate_ultrasonic_sensor()
                time.sleep(0.5)
                deposit_container()
                break
            # code for linefollowing during transfer
            left, right = bot.line_following_sensors()  
            if left == 1 and right == 1:
                bot.set_wheel_speed([0.1,0.1])
            elif left == 1 and right == 0:
                bot.set_wheel_speed([0,0.02])
                time.sleep(0.01)
            elif left == 0 and right == 1:
                bot.set_wheel_speed([0.02,0])
                time.sleep(0.1)
            else:
                bot.set_wheel_speed([0.01,0.05])
    exit  

    

#function to deposit container
#Written By Taysir Alam
def deposit_container():
    #activate actuator and dump
    bot.activate_linear_actuator()
    bot.dump()
    bot.deactivate_linear_actuator()

#function to return bot home
#Written By Qaosain Ahmad
def return_home():
    arm.home()
    bot.activate_ultrasonic_sensor()
    #while loop for bot to continue in line untill home position is reached
    while True:
        home = bot.position()
        print(home)
        if (1.462,0.055,0.00074) <= home <= (1.49,0.09,0.0007579):
            bot.stop()
            time.sleep(0.8)
            bot.rotate(-45)
            time.sleep(0.8)
            bot.rotate(-45)
            bot.forward_distance(0.05)
            time.sleep(0.8)
            bot.rotate(45)
            time.sleep(0.8)
            bot.rotate(45)
            bot.rotate(5)
            bot.deactivate_ultrasonic_sensor()
            break
        left, right = bot.line_following_sensors()  
        if left == 1 and right == 1:
            bot.set_wheel_speed([0.1,0.1])
        elif left == 1 and right == 0:
            bot.set_wheel_speed([0,0.02])
            time.sleep(0.01)
        elif left == 0 and right == 1:
            bot.set_wheel_speed([0.02,0])
            time.sleep(0.1)
        else: 
            bot.set_wheel_speed([0.01,0.05])


    exit
    
        
#main function 
main()