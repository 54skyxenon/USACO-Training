/*
ID: bwliang1
TASK: betsy
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

// Function prototypes needed for mutual recursion!
int dfs_helper(int, int, int);
int dfs(int, int, int);

int n;
bool visited[7][7];

bool within_bounds(int r, int c) {
    return r >= 0 && r < n && c >= 0 && c < n;
}

bool visitable(int r, int c) {
    return within_bounds(r, c) && !visited[r][c];
}

bool surrounded(int r, int c) {
    int touched = 0;

    for (auto& [nr, nc] : vector<pair<int, int>>{{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}}) {
        if (!within_bounds(nr, nc) || visited[nr][nc]) {
            touched += 1;
        }
    }
    
    return touched == 3;
}

int is_dead_end(int r, int c) {
    return visitable(r, c) && !(r == n - 1 && c == 0) && surrounded(r, c);
}

int dfs_helper(int nr, int nc, int new_visited_count) {
    visited[nr][nc] = true;
    int ans = dfs(nr, nc, new_visited_count);
    visited[nr][nc] = false;
    return ans;
}

int dfs(int r, int c, int visited_count) {
    // Noble Mushtak has an alternate solution: use broken profile DP
    // My idea: if we've reached the end, we need to visit all squares
    if (visited[n - 1][0]) {
        return (visited_count == n * n);
    }

    // My idea: there must be exactly one connected component of unvisited squares
    // Benjamin Qi's idea: you just check if opposite sides are blocked to do this
    bool left_visitable = visitable(r, c - 1);
    bool right_visitable = visitable(r, c + 1);
    bool top_visitable = visitable(r - 1, c);
    bool bottom_visitable = visitable(r + 1, c);

    if (left_visitable && right_visitable && !top_visitable && !bottom_visitable) {
        return 0;
    }

    if (!left_visitable && !right_visitable && top_visitable && bottom_visitable) {
        return 0;
    }

    int ans = 0;

    // Adam D'Angelo's idea: if there is only one dead end, then you must go into it
    bool left_dead_end = is_dead_end(r, c - 1);
    bool right_dead_end = is_dead_end(r, c + 1);
    bool top_dead_end = is_dead_end(r - 1, c);
    bool bottom_dead_end = is_dead_end(r + 1, c);

    int dead_ends = left_dead_end + right_dead_end + top_dead_end + bottom_dead_end;
    
    if (dead_ends == 1) {
        if (bottom_dead_end) {
            ans += dfs_helper(r + 1, c, visited_count + 1);
        }
        if (right_dead_end) {
            ans += dfs_helper(r, c + 1, visited_count + 1);
        }
        if (top_dead_end) {
            ans += dfs_helper(r - 1, c, visited_count + 1);
        }
        if (left_dead_end) {
            ans += dfs_helper(r, c - 1, visited_count + 1);
        }
    }
    else if (dead_ends == 0)  {
        if (left_visitable) {
            ans += dfs_helper(r, c - 1, visited_count + 1);
        }
        if (right_visitable) {
            ans += dfs_helper(r, c + 1, visited_count + 1);
        }
        if (top_visitable) {
            ans += dfs_helper(r - 1, c, visited_count + 1);
        }
        if (bottom_visitable) {
            ans += dfs_helper(r + 1, c, visited_count + 1);
        }
    }

    return ans;
}

int32_t main() {
    setIO("betsy");
    cin >> n;
    
    visited[0][0] = true;
    cout << dfs(0, 0, 1) << '\n';
}