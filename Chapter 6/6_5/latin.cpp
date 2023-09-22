/*
ID: bwliang1
TASK: latin
LANG: C++17
*/

// Adapted from: cloudzf2

#include <bits/stdc++.h>
using namespace std;

#define int long long

int N;
int fact[7] = {0, 1, 2, 6, 24, 120, 720};
int at_top_column[7];
int dp[8];

bool row_taken[7][7];
bool col_taken[7][7];

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int dfs(int row, int col, int state) {
    if (row == N - 1) {
        dp[state]++;
        return 1;
    }

    int ans = 0;

    for (int i = 0; i < N; i++) {
        if (!row_taken[row][i] && !col_taken[col][i]) {
            // for just the second row, memoize
            if (row == 1) {
                // mark what's put in each column
                at_top_column[col] = i;

                // if we're on the last column, construct a state characterized by the longest permutation cycle
                if (col == N - 1) {
                    state = 2;

                    vector<bool> visited(N, false);
                    for (int i = 0; i < N; i++) {
                        if (!visited[i]) {
                            int count = 0;
                            int ptr = i;

                            do {
                                visited[ptr] = true;
                                ptr = at_top_column[ptr];
                                count++;
                            }
                            while (!visited[ptr]);
                            
                            state = max(state, count);
                        }
                    }

                    // if this state was memoized for the first row, then take advantage of symmetry
                    if (dp[state] > 0) {
                        return dp[state];
                    }
                }
            }

            row_taken[row][i] = true;
            col_taken[col][i] = true;

            if (col < N - 1) {
                ans += dfs(row, col + 1, state);
            }
            else {
                ans += dfs(row + 1, 1, state);
            }

            row_taken[row][i] = false;
            col_taken[col][i] = false;
        }
    }

    return ans;
}

int32_t main() {
    setIO("latin");

    cin >> N;
    for (int i = 0; i < N; i++) {
        col_taken[i][i] = true;
        row_taken[i][i] = true;
    }

    at_top_column[0] = 1;
    cout << dfs(1, 1, 0) * fact[N - 1] << '\n';
}
