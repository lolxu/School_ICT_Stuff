#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

string weekDays[7] = {"Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."};

const int MAXN = 10000007;

string cow[MAXN];
float morningYield[MAXN], eveningYield[MAXN];
float totalYield;

int flag = 0;
int schk = 0;
int scnt = 0;


vector<string> badCow;


int main(){
    int N;
    printf("Please enter the number of cows in the herd\n");
    scanf("%d", &N);
    printf("There are %d cows in the herd.\n", N);
    
    int i = 1;
    int badCowNum = 0;
    float maxYield = 0;
    string bestCow;
    string tmpID;
    
    //MAIN LOOP
    while (i <= N){
        
        //input
        printf("Please input COW %d's ID (3-digit)\n",i);
        scanf("%s",&tmpID);
        
        /*
        if (chksame(tmpID, N)){
            while (1){
                printf("The ID already exists! ENTER ANOTHER VALID ID!\n");
                scanf("%s",&tmpID);
                if (!chksame(tmpID)) {
                    if (tmpID.length() == 3){flag = 1;break;}
                    else printf("Please enter a valid 3-digit ID!\n");
                }
            }
        }
        */
         
        int j = 1;
        int badYield = 0;
        
        //checking digit
        if (tmpID.length() == 3){
            cow[i] = tmpID;
            int day = 0;

            //The day loop
            while (j <= 14){
                float tmpY, tmpX;
                //AM yield input
                cout << "COW " << i << "'s yield: Please input the MORNING yield for " << weekDays[day] << " (enter -1 to exit)" << endl;
                cin >> tmpX;
                if (tmpX == -1) break;
                
                if (tmpX > maxYield){
                    maxYield = tmpX;
                    bestCow = cow[i];
                }
                
                morningYield[j] = tmpX;
                totalYield += tmpX;
                
                //PM yield input
                cout << "COW " << i << "'s yield: Please input the EVENING yield for " << weekDays[day] << " (enter -1 to exit)" << endl;
                cin >> tmpY;
                if (tmpY == -1) break;
                
                if (tmpY > maxYield){
                    maxYield = tmpY;
                    bestCow = cow[i];
                }
                
                eveningYield[j] = tmpY;
                totalYield += tmpY;
                
                //increment of the "day loop"
                j++;
                day++;
                
                //recording number of bad yield (less than 12 litres)
                if (tmpX + tmpY < 12) badYield++;
                
            }
            //check the badYield times and store the bad cow ID
            if (badYield >= 4){
                badCowNum++;
                badCow.push_back(cow[i]);
            }
            
            i++;
        }
        
        else {
            cout << "INVALID INPUT (wrong number of digit)" << endl;
            while (1){
                printf("ENTER ANOTHER VALID ID! (3-digit)\n");
                cin >> tmpID;
                if (tmpID.length() == 3) {flag = 1; cow[i] = tmpID; break;}
            }
        }
        
    }
    cout << endl;
    cout << "Total yield this week is (rounded to whole litre): " << round(totalYield) << endl;
    cout << endl;
    cout << "The average yield per cow is (rounded to whole litre): " << round(totalYield / MAXN) << endl;
    cout << endl;
    cout << "The most productive cow is: " << bestCow << endl;
    cout << endl;
    
    if (badCowNum > 0){
        cout << "The cows that have less than 12 litres of milk on 4 or more days are (output ID): " << endl;
        for (int i = 0; i < badCowNum; i++){
            cout << badCow[i] << endl;
        }
    }
    return 0;
}
