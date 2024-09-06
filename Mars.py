def launch_sequence():
    print("Initiating countdown...")
    print("3... 2... 1... Lift-off!")
launch_sequence()
def travel_time_to_mars(distance, speed):
    time = distance / speed
    print("Travel time to Mars is:", time, "hours")
    if speed < 20000:
        print("Warning: Speed is too slow for a timely arrival!")
    elif speed > 50000:
        print("Warning: Speed is too fast, risk of overshooting Mars!")
    else:
        print("Speed is optimal for Mars mission.")
travel_time_to_mars(225000000, 250000000000)
def mars_mission(distance, speed, fuel, crew_ready):
    time = distance / speed
    print("Travel time to Mars is:", time, "hours")
    if speed < 20000:
        print("Warning: Speed is too slow for a timely arrival!")
    elif speed > 50000:
        print("Warning: Speed is too fast, risk of overshooting Mars!")
    else:
         print("Speed is optimal for Mars mission.")
    if fuel < 500000:
        print("Warning: Not enough fuel for the journey!")
    else:
        print("Fuel levels are sufficient.")

    if crew_ready:
        print("Crew is ready for the mission")
    else:
        print("Crew is not ready. Mission delayed")            
    print ("Estimated travel time to Mars:", time, "hours")    
mars_mission(225000000, 40000, 700000, True)