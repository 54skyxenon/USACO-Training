/*
ID: bwliang1
LANG: C++17
TASK: spin
*/

#include <bits/stdc++.h>
using namespace std;

#define MOD 360
#define pii pair<int, int>
#define mp make_pair

int speed[5];
vector<pii> wheels[5];

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

pii helper(pii& w1, pii& w2) {
    int new_posn = max(w1.first, w2.first);
    int new_extent = min(w1.first + w1.second, w2.first + w2.second) - new_posn;
    return mp(new_posn % MOD, new_extent);
}

pii merge(pii w1, pii w2) {
    if ((w1.first + w1.second >= MOD) == (w2.first + w2.second >= MOD)) {
        return helper(w1, w2);
    }
    else if (w1.first + w1.second >= MOD) {
        w2.first += MOD;
        return helper(w1, w2);
    }
    else { // w2.first + w2.second >= MOD
        w1.first += MOD;
        return helper(w1, w2);
    }
}

bool simulate() {
    for (pii& w1 : wheels[0]) {
        for (pii& w2 : wheels[1]) {
            for (pii& w3 : wheels[2]) {
                for (pii& w4 : wheels[3]) {
                    for (pii& w5 : wheels[4]) {
                        if (merge(w1, merge(w2, merge(w3, merge(w4, w5)))).second >= 0) {
                            return true;
                        }
                    }
                }
            }
        }
    }

    for (int i = 0; i < 5; i++) {
        for (pii& wedge : wheels[i]) {
            wedge.first = (wedge.first + speed[i]) % MOD; 
        }
    }
        
    return false;
}

int main() {
    setIO("spin");

    for (int i = 0; i < 5; i++) {
        cin >> speed[i];

        int wedges;
        cin >> wedges;

        wheels[i].resize(wedges);
        for (int j = 0; j < wedges; j++) {
            cin >> wheels[i][j].first >> wheels[i][j].second;
        }
    }

    int t = 0;
    while (!simulate()) {
        if (++t == 360) {
            cout << "none\n";
            return 0;
        }
    }
    cout << t << '\n';
}