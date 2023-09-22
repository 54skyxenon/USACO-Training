/*
ID: bwliang1
TASK: bigbrn
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define maxN 1001

int n, t;
int dp[maxN][maxN];
int blocked[maxN][maxN];

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
    setIO("bigbrn");

    cin >> n >> t;
    while (t--) {
        int r, c;
        cin >> r >> c;
        blocked[r][c] = 1;
    }

    int ans = 0;

    for (int r = 1; r <= n; r++) {
        for (int c = 1; c <= n; c++) {
            if (!blocked[r][c]) {
                int top = dp[r - 1][c];
                int left = dp[r][c - 1];
                if (top == left) {
                    dp[r][c] = top + (1 - blocked[r - top][c - top]);
                }
                else {
                    dp[r][c] = 1 + min(top, left);
                }
            }
            ans = max(ans, dp[r][c]);
        }
    }

    cout << ans << '\n';
}