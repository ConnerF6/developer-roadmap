import time
disapointment = False
in_bathroom = False

def Takea_Shit():
    print("I'M GONNA BROWN!")
    print("Objective: get to the bathroom within 5 minutes or shit yourself")
    time.sleep(10)
    if in_bathroom == True:
        print("Ahhh sweet releaf")
    else:
        print("I'M SHITZING!!!")
        disapointment = True
    time.sleep(1 * 8)
    Takea_Shit()
Takea_Shit()