#IGCSE Computer Science 2018 pre-release Group KOO solution.

#Crucial Variables
weekDays = ["Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."];
cowNum = int(input("Please input the number of cows in the herd: "));

cowID = [];
badCowNum = 0;
badCowID = [];
totalYield = 0.0;
maxYield = 0.0;
maxYieldID = "";

if (cowNum > 0):
    for i in range(0, cowNum):
        tmpID = "";         #Use this because the ID has to be checked first!
        tmpID = input("Enter COW %d's ID (3-digit): " % (i+1));
        #-------------------#Correct Input Value if it is wrong in the beginning
        while (len(tmpID) != 3):
            print("You have entered a %d-digit ID, the program only accept 3-digit ID. Please enter again!" % (len(tmpID)));
            tmpID = input("-> Enter COW %d's ID (AGAIN): " % (i+1));
        
        cowID.append(tmpID);

        #-------------------#temporary variables used in the DAY LOOP
        badYieldCnt = 0;    #Store the times of bad yield (<12 L)
        yieldPerCow = 0.0;
        morningYield = 0.0; 
        eveningYield = 0.0;
        
        for day in range(0, 7):
            morningYield = float(input("Enter the %s MORNING_YIELD for this cow: " % (weekDays[day])));
            eveningYield = float(input("Enter the %s EVENING_YIELD for this cow: " % (weekDays[day])));
            if (morningYield + eveningYield < 12):
                badYieldCnt += 1;
            yieldPerCow += morningYield + eveningYield;
            
        #-------------------#END of DAY LOOP
            
        totalYield += yieldPerCow;
        
        if (yieldPerCow > maxYield):
            maxYield = yieldPerCow;
            maxYieldID = cowID[i];
            
        #Processing the number of cows that have bad yield
        if (badYieldCnt >= 4):
            badCowNum += 1;
            badCowID.append(cowID[i]); #Record ID

    ################# END of COW LOOP ######################
    print("################################### RESULTS ###################################");
    print("The TOTAL YIELD of the herd (rounded to the nearest whole litre): %d" % (round(totalYield)));
    print("")
    print("The AVERAGE YIELD of the herd (rounded to the nearest whole litre): %d" % (round(totalYield / cowNum)));
    print("")
    print("The COW with most yield is COW %s. It produced %d L (rounded to the nearest whole litre) of milk " % (maxYieldID, round(maxYield)));
    print("")
    #Check cows that produced less than 12L of milk for 4 or more days.
    if (len(badCowID) > 0):
        print("-> Here are the cows that produced less than 12 L of milk for four or more days in a week:");
        for i in range(0, len(badCowID)):
            print("cow",badCowID[i]);
else:
    print("Y'all don't have any cows. Y'all poor!")

