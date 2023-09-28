#Part 1
print("Welcome to Bretts Restaurant Calculator. This calculator will calculate an 18% tip and 7% sales tax.")
print("To begin, Please enter the charge for the food: ")
OriginalValue = float(input())
AdditionalCharges = [OriginalValue * 0.18, OriginalValue * 0.07]
print("~~~~~")
print("Tip: {:0.2f}".format(AdditionalCharges[0]))
print("Sales Tax: {:0.2f}".format(AdditionalCharges[1]))
print("Total cost: {:0.2f}".format(OriginalValue + sum(AdditionalCharges)))
print("~~~~~")
print("Press enter to close...") 
input()



#################################################################################################################################################

# Part 2
print("Welcome to Bretts Clock Calculator. This calculator will calculate the time given a start point and a duration (in hours) on a 24 hour scale.")
print("To begin, Please enter the current time (in 24 hour, integer format ONLY. Ex: 13 = 1PM): ")
StartTime = int(input())
print("Now enter a duration (in hours) that you would like to calculate: ")
Duration = int(input())
DurationChangeLog = [Duration]
# Using iteration method (demonstrating looping and arrays)
while(Duration >= 24):
    Duration -= 24;
    DurationChangeLog.append(Duration)
print(">> DebugInfo:DurationChangeLog: ", DurationChangeLog)
# Using MODULUS to calculate the remainder instead (Remove the While statement)
if (Duration > 24):
    ModdedDuration = Duration % 24
else:
    ModdedDuration = Duration
    
EndTime = StartTime + ModdedDuration
if(EndTime >= 24):
    EndTime -= 24
print("The ending time is: ", EndTime)


