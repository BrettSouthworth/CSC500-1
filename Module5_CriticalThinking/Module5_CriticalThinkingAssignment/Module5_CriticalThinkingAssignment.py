
#Part 1

print("Welcome to Bretts average rainfall calculator. Please enter the number of years (whole numbers only): ")
years = int(input())
i = 0

totalRainFall = 0.0
totalMonths = years * 12
avgRainFallPerMonth = 0.0

# Outer loop for number of years
for i in range(years): 

    # Inner loop for each month
    for j in range (12):
        print("Please enter the rainfall in inches for year " + str(i+1) + " month " + str(j+1) + ": ")
        rainfall_in = float(input())
        totalRainFall += rainfall_in
        avgRainFallPerMonth += rainfall_in
    
print("Total Rainfall: " + str(totalRainFall))
print("Number of Months: " + str(totalMonths))
print("Average Rainfall: " + str(avgRainFallPerMonth/totalMonths))


#Part 2
print("Welcome to Bretts CSU Global Bookstore book club rewards calculator. To begin, please enter the total number of books you have purchased this month: ")
RewardsConfiguration = [[0,0], [2,5], [4,15], [6,30], [8,60]]
totalBooksPurchased = int(input())
maxIndex = len(RewardsConfiguration)

if maxIndex < 1:
    raise Exception("Invalid RewardsConfiguration inputted.")

rewardPoints = RewardsConfiguration[0][1]

for i in range(maxIndex):
    if totalBooksPurchased >= RewardsConfiguration[i][0]:
        rewardPoints = RewardsConfiguration[i][1]
    else:
        break    

print("Your rewards points have totalled to: " + str(rewardPoints))
