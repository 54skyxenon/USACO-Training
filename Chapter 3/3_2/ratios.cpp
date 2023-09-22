/*
ID: bwliang1
LANG: C++17
TASK: ratios
*/

#include <bits/stdc++.h>
using namespace std;

#define tiiii tuple<int, int, int, int>
#define mt make_tuple
#define INF 2e9

int goal[3];
int mixtures[3][3];

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

void solve() {
    vector<tiiii> solutions;

    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            for (int k = 0; k < 100; k++) {
                int entries[3] = {i, j, k};
                vector<int> sums;
                for (int c = 0; c < 3; c++) {
                    int sum = 0;
                    for (int r = 0; r < 3; r++) {
                        sum += entries[r] * mixtures[r][c];
                    }
                    sums.push_back(sum);
                }

                int ratio = 0;
                bool bad = false;
                for (int l = 0; l < 3; l++) {
                    if (goal[l] > 0) {
                        bad = bad || (sums[l] % goal[l] != 0);
                        ratio = max(ratio, sums[l] / goal[l]);
                    }
                    else {
                        bad = bad || (sums[l] > 0);
                    }
                }
                for (int l = 0; l < 3; l++) {
                    bad = bad || (goal[l] > 0 && (sums[l] / goal[l] != ratio));
                }

                if (ratio > 0 && !bad) {
                    solutions.push_back(mt(i, j, k, ratio));
                }
            }
        }
    }

    if (solutions.empty()) {
        cout << "NONE\n";
    }
    else {
        int ans[4] = {0, 0, 0, 0};
        int ans_sum = INF;

        for (auto [a, b, c, d] : solutions) {
            if (a + b + c + d < ans_sum) {
                ans_sum = a + b + c + d;
                ans[0] = a;
                ans[1] = b;
                ans[2] = c;
                ans[3] = d;
            }
        }

        cout << ans[0] << " " << ans[1] << " " << ans[2] << " " << ans[3] << '\n';
    }
}

int main() {
    setIO("ratios");

    cin >> goal[0] >> goal[1] >> goal[2];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> mixtures[i][j];
        }
    }

    solve();
}