/*
ID: bwliang1
TASK: stamps
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define maxK 200
#define maxS 10000

bool seen[maxK * maxS + 1];

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
    setIO("stamps");

    int k, n;
    cin >> k >> n;
    
    vector<int> stamps(n);
    for (int& s : stamps) {
        cin >> s;
    }

    seen[0] = true;
    queue<pair<int, int>> Q({make_pair(0, 0)});

    while (!Q.empty()) {
        auto [curr, depth] = Q.front();
        Q.pop();

        if (depth + 1 <= k) {
            for (int s : stamps) {
                if (!seen[curr + s]) {
                    seen[curr + s] = true;
                    Q.push(make_pair(curr + s, depth + 1));
                }
            }
        }

    }

    int i = 0;
    while (seen[i]) {
        i++;
    }

    cout << (i - 1) << '\n';
}