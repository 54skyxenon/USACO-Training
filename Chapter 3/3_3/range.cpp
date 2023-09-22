/*
ID: bwliang1
LANG: C++17
TASK: range
*/

#include <bits/stdc++.h>
using namespace std;

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
    setIO("range");
    int n;
    cin >> n;
    
    vector<string> field(n);
    for (string& row : field) {
        cin >> row;
    }

    vector<vector<int>> prefix(n + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= n; i++) {
        vector<int> prefix_row(n + 1);
        for (int j = 1; j <= n; j++) {
            prefix_row[j] = prefix_row[j - 1] + (field[i - 1][j - 1] == '1');
            prefix[i][j] = prefix_row[j] + prefix[i - 1][j];
        }
    }

    vector<int> grazable(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int dim = 2; dim <= min(i, j); dim++) {
                int square_count = prefix[i][j] - prefix[i - dim][j] - prefix[i][j - dim] + prefix[i - dim][j - dim];
                if (square_count == dim * dim) {
                    grazable[dim]++;
                }
            }
        }
    }
    
    for (int i = 2; i <= n; i++) {
        if (grazable[i]) {
            cout << i << " " << grazable[i] << '\n';
        }
        else {
            break;
        }
    }
}