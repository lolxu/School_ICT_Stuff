#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

char GC[10000];
double weight = 0;
int NumOfSacks[4];

int main(){
    
    printf("Please input the number of sacks [input content first(C - cement, G - gravel, S - sand), Then the number of sacks] [You need to input three times]\n");
    int k = 0;
    for (int i = 1; i <= 3; i++){
        cin >> GC[i] >> k;
        
        if (GC[i] == 'C') NumOfSacks[1] = k;
        if (GC[i] == 'S') NumOfSacks[2] = k;
        if (GC[i] == 'G') NumOfSacks[3] = k;
        
        //cout << GC[i] << NumOfSacks[i] << endl;
    }
    
    int reject = 0;
    double TotWeight = 0;
    
    for (int i = 1; i <= 3; i++)
    
    for (int j = 1; j <= NumOfSacks[i]; j++){
    
    char content = GC[i];
    bool flag = 1;
        
        //while (flag){
        if ((content == 'S') || (content == 'G')){
            
            cout << "Please input the weight of this sack " << content << " " << j << endl;
            
            scanf("%lf", &weight);
            //cout << endl;
            
            if (weight <= 49.9) {reject++;}
                else if (weight >= 50.1) {reject++;}
                else {flag = 0; TotWeight += weight;}
        }
        else if (content == 'C'){
            
            cout << "Please input the weight of this sack " << content << " " << j << endl;
            scanf("%lf", &weight);
            //cout << endl;
            
            if (weight <= 24.9) {reject++;}
            else if (weight >= 25.10) {reject++;}
            else {flag = 0; TotWeight += weight;}
            
        }
        //}
        
    }
    
    cout << "Total weight of accepted sacks " << TotWeight << endl;
    cout << "Total rejected number of sacks " << reject << endl;
    
    return 0;
    
}
