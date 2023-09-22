/*
ID: bwliang1
TASK: ariprog
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define maxN 25
#define maxM 250
#define maxB (2 * maxM * maxM)

int n, m;
bool is_bisquare[maxB + 1];

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

bool ok(int s, int d) {
    for (int i = 0; i < n; i++) {
        int term = s + d * i;
        if (term > maxB || !is_bisquare[term]) {
            return false;
        }
    }
    return true;
}

int main() {
    setIO("ariprog");
    cin >> n >> m;
    
    // O(M^2)
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= m; j++) {
            is_bisquare[i * i + j * j] = true;
        }
    }

    // O(M^2)
    vector<int> bisquares;
    for (int i = 0; i <= maxB; i++) {
        if (is_bisquare[i]) {
            bisquares.push_back(i);
        }
    }
    
    // O(M^4 / big constant?)
    vector<pair<int, int>> sequences;
    for (int start : bisquares) {
        for (int d = 1; d <= (bisquares.back() - start) / (n - 1); d++) {
            if (ok(start, d)) {
                sequences.push_back(make_pair(d, start));
            }
        }
    }

    if (sequences.empty()) {
        cout << "NONE\n";
    }
    else {
        sort(sequences.begin(), sequences.end());
        for (auto [d, s] : sequences) {
            cout << s << " " << d << '\n';
        }
    }
}