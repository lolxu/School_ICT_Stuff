#IGCSE Computer Science 2018 pre-release Group KOO solution.
#Altered version - input are randomly generated.
#Crucial Variables

import random;

weekDays = ["Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."];
print("Please input the number of cows in the herd: ");
cowNum = random.randint(0, 1000);
print(cowNum);

cowID = [];
badCowNum = 0;
badCowID = [];
totalYield = 0.0;
maxYield = 0.0;
maxYieldID = "";
al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

if (cowNum > 0):
    for i in range(0, cowNum):
        tmpID = "";         #Use this because the ID has to be checked first!
        print("Enter COW %d's ID (3-digit): " % (i+1));
        tmpID = ''.join(random.sample(al, random.randint(1,4)));
        print(tmpID);
        #-------------------#Correct Input Value if it is wrong in the beginning
        while (len(tmpID) != 3):
            print("You have entered a %d-digit ID, the program only accept 3-digit ID. Please enter again!" % (len(tmpID)));
            print("-> Enter COW %d's ID (AGAIN): " % (i+1));
            tmpID = ''.join(random.sample(al, 3));
            print(tmpID);
        
        cowID.append(tmpID);

        #-------------------#temporary variables used in the DAY LOOP
        badYieldCnt = 0;    #Store the times of bad yield (<12 L)
        yieldPerCow = 0.0;
        morningYield = 0.0; 
        eveningYield = 0.0;
        
        for day in range(0, 7):
            morningYield = round(random.uniform(0,30),2);
            print("Enter the %s MORNING_YIELD for this cow: " % (weekDays[day]));
            print(morningYield);
            eveningYield = round(random.uniform(0,30),2);
            print("Enter the %s EVENING_YIELD for this cow: " % (weekDays[day]));
            print(eveningYield);
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
    print("Y'all don't have any cows. Y'all poor!");

