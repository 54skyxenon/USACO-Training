/*
ID: bwliang1
TASK: inflate
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define maxNM 10001
#define pii pair<int, int>
#define mp make_pair

int m, n;
vector<pair<int, int>> categories;
vector<int> memo(maxNM, -1);

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int dp(int rem) {
    if (memo[rem] != -1) {
        return memo[rem];
    }

    if (rem == 0) {
        return memo[rem] = 0;
    }
    
    int ans = 0;
    for (auto [points, minutes] : categories) {
        if (minutes > rem) {
            break;
        }
        ans = max(ans, points + dp(rem - minutes));
    }
    
    return memo[rem] = ans;
}

int main() {
    setIO("inflate");
    cin >> m >> n;

    for (int i = 0; i < n; i++) {
        int points, minutes;
        cin >> points >> minutes;
        if (minutes <= m) {
            categories.push_back(mp(points, minutes));
        }
    }

    sort(categories.begin(), categories.end(), [](const auto& lhs, const auto& rhs) {
        return lhs.second < rhs.second;
    });

    cout << dp(m) << '\n';
}