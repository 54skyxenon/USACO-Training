/*
ID: bwliang1
TASK: humble
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define int long long

int k, n;

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int solve() {
    cin >> k >> n;
    
    set<int> Q;

    vector<int> primes(k);
    for (int i = 0; i < k; i++) {
        cin >> primes[i];
        Q.insert(primes[i]);
    }
    sort(primes.begin(), primes.end());

    int step = 0;
    for (auto it = Q.begin(); it != Q.end(); it++) {
        int curr = *it;
        if (++step == n) {
            return curr;
        }

        for (int p : primes) {
            if (Q.size() >= n && curr * p >= *Q.rbegin()) {
                break;
            }
            
            Q.insert(curr * p);
            if (Q.size() > n) {
                Q.erase(prev(Q.end()));
            }
        }
    }

    throw invalid_argument("No solution!");
}

int32_t main() {
    setIO("humble");
    cout << solve() << '\n';
}