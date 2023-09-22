/*
ID: bwliang1
TASK: checker
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int n, ans_count, rows_taken_order[13];
bool rows_taken[13], diag_down[25], diag_up[25];

// Basically N-Queens but we only need to print the first 3 solutions
void dfs(int col) {
    if (col == n) {
        if (ans_count < 3) {
            for (int i = 0; i < n; i++) {
                cout << rows_taken_order[i] << " \n"[i == n - 1];
            }
        }
        ans_count++;
        return;
    }
    
    for (int row = 0; row < n; row++) {
        // DFS'ing this way prevents us from putting our next queen in the same column as another
        // Be we also cannot be in the same row nor diagonal
        int diag_down_index = row - col + 12;
        int diag_up_index = row + col;

        if (rows_taken[row] || diag_down[diag_down_index] || diag_up[diag_up_index]) {
            continue;
        }

        rows_taken_order[col] = row + 1;
        rows_taken[row] = true;
        diag_down[diag_down_index] = true;
        diag_up[diag_up_index] = true;

        dfs(col + 1);

        rows_taken_order[col] = 0;
        rows_taken[row] = false;
        diag_down[diag_down_index] = false;
        diag_up[diag_up_index] = false;
    }
}

int main() {
    setIO("checker");
    cin >> n;

    dfs(0);
    cout << ans_count << '\n';
}