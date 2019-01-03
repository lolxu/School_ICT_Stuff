#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int Counter = 0, Number;


int main(){
    cin >> Number;
    int Highest = Number;
    int Lowest  = Number;
    
    while (Counter < 9){
        cin >> Number;
        if (Number > Highest) Highest = Number;
        else if (Number < Lowest) Lowest = Number;
        Counter++;
    }
    cout << Highest << ", " << Lowest << endl;
    return 0;
}
