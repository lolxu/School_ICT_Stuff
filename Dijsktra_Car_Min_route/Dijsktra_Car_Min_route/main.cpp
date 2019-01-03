#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

const int maxn = 100050;

int T, n, m, point[maxn];
int inp[maxn], tmp;
queue<int> q;

struct node{
    int r, nxt;
}e[maxn];

void bind(int ind, int ed){
    e[tmp].r = ed;
    e[tmp].nxt = point[ind];
    point[ind] = tmp++;
}

int main(){
    int a, b, ans;
    cin >> T;
    while (T--){
        cin >> n >> m;
        tmp = 1;
        ans = 0;
        memset(inp, 0, sizeof(inp));
        memset(point, -1, sizeof(point));
        for (int i = 0; i < m; i++){
            cin >> a >> b;
            bind(a, b);
            inp[b]++;
        }
        for (int i = 1; i <= n; i++){
            if (!inp[i]){
                q.push(i);
                ans++;
            }
        }
        
        while (!q.empty()){
            int x = q.front();
            q.pop();
            for (int i = point[x]; i > 0; i = e[i].nxt){
                int v = e[i].r;
                inp[v]--;
                if (!inp[v]){
                    q.push(v);
                    ans++;
                }
            }
        }
        
        if (ans == n) cout << "Correct" << endl;
        else cout << "Wrong" << endl;
    }
    return 0;
}
