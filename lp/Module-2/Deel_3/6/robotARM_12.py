from RobotArm import RobotArm  
robotArm = RobotArm('exercise 12')
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for _ in range(9 - i):
            robotArm.moveRight()
        robotArm.drop()
        for _ in range(8- i):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()
