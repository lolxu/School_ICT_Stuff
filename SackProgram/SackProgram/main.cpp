#include <iostream>
#include <cstdio>
#include <cstring>
//#include <algorithm>

using namespace std;

char content;
double weight = 0;

int main(){
    
    bool flag = 1;
    
    printf("Please input the content for this sack ( C - cement, G - gravel, S - sand)\n");
    
    scanf("%c", &content);
    printf("\n");
    
    if (content == 'S' || content == 'G' || content == 'C'){
    
        //while (flag){
        if ((content == 'S') || (content == 'G')){
            
            printf("Please input the weight of this sack\n");
            scanf("%lf", &weight);
            //cout << endl;
            
            if (weight <= 49.9) cout << content << " sack is underweight! Rejected!" << endl << endl;
            else if (weight >= 50.1) cout << content << " sack is overweight! Rejected!" << endl << endl;
            else {cout << "Thank you for your submission. The " << content << " sack has the weight of " << weight << endl; flag = 0;}
        }
        else if (content == 'C'){
            
            printf("Please input the weight of this sack\n");
            scanf("%lf", &weight);
            //cout << endl;
            
            if (weight <= 24.9) cout << content << " sack is underweight! Rejected!" << endl << endl;
            else if (weight >= 25.10) cout << content << " sack is overweight! Rejected!" << endl << endl;
            else {cout << "Thank you for your submission. The " << content << " sack has the weight of " << weight << endl; flag = 0;}
            
        }
        //}
    
    }
    else cout << "INVALID INPUT" << endl;
    
    return 0;
    
}
