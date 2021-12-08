#you have 4 miles from university. the bus drives at 25mph but  spends 2 minutes at each 
#of the 10 stops on the way .How long will the bus journey take?Alternatively ,you could 
#run to university .you jog the first mile at 7mph; then run the next twp at 15mph; before
#jogging the last at 7mph again.will this be quicker or slower than the bus?
stoppedtime=2*10
distance=4
speedmph=25/60
drivingTime=distance/speedmph
totalTimeByBus=drivingTime+stoppedtime
runningtime=((1/7)+(2/15)+(1/7))*60
print(f"the total time taken by the bus is {totalTimeByBus}")
print(f"the total time while jogging in {runningtime}")
if totalTimeByBus>runningtime:
    print("Bus takes more than the jog")
else:
    print("bus takes less than time than the jog")