#include <iostream>
#include <cstdio>

using namespace std;

int A = 0;
int B = 0;
int C = 100;

int main(){
    int x;
    
    for (A = 0; A < 10; A++){
        cin >> x;
        if (x > B) B = x;
        else if (x < C) C = x;
    }
    cout << B << ", " << C << endl;
}
