/*
ID: bwliang1
TASK: camelot
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define INF 1e9
#define maxC 26
#define maxR 30
#define pii pair<int, int>
#define mp make_pair

int rows, columns;

pii king;
vector<pii> knights;
vector<pii> king_adj({mp(-1, -1), mp(-1, 0), mp(-1, 1), mp(0, -1), mp(0, 1), mp(1, -1), mp(1, 0), mp(1, 1)});
vector<pii> knights_adj({mp(-2, 1), mp(-2, -1), mp(2, 1), mp(2, -1), mp(-1, 2), mp(-1, -2), mp(1, -2), mp(1, 2)});

int dist_knights[maxR][maxC][maxR][maxC];
bool visited_knights[maxR][maxC][maxR][maxC];
vector<vector<vector<vector<int>>>> dist_pickup(maxR, vector<vector<vector<int>>>(maxC, vector<vector<int>>(maxR, vector<int>(maxC, INF))));

int dist_king[maxR][maxC];
bool visited_king[maxR][maxC];

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
    setIO("camelot");
    cin >> rows >> columns;

    char king_c;
    int king_r;
    cin >> king_c >> king_r;
    king = mp(king_r - 1, king_c - 'A');

    char c;
    while (cin >> c) {
        int r;
        cin >> r;
        knights.push_back(mp(r - 1, c - 'A'));
    }

    // BFS to find king's distance to every reachable cell
    {
        queue<pii> Q({king});
        visited_king[king.first][king.second] = true;
        dist_king[king.first][king.second] = 0;

        while (!Q.empty()) {
            auto [r, c] = Q.front();
            Q.pop();

            for (auto [dr, dc] : king_adj) {
                int nr = r + dr;
                int nc = c + dc;

                if (0 <= nr && nr < rows && 0 <= nc && nc < columns && !visited_king[nr][nc]) {
                    visited_king[nr][nc] = true;
                    dist_king[nr][nc] = dist_king[r][c] + 1;
                    Q.push(mp(nr, nc));
                }
            }
        }
    }

    // BFS from each knight to record it's distance to each cell
    // Also record shortest distance king must travel to get picked up by each knight
    for (auto [sr, sc] : knights) {
        queue<pii> Q({mp(sr, sc)});
        dist_knights[sr][sc][sc][sc] = 0;
        visited_knights[sr][sc][sr][sc] = true;
        dist_pickup[sr][sc][sr][sc] = dist_king[sr][sc];

        while (!Q.empty()) {
            auto [r, c] = Q.front();
            Q.pop();

            vector<pii> to_visit;
            for (auto [dr, dc] : knights_adj) {
                int nr = r + dr;
                int nc = c + dc;
                if (0 <= nr && nr < rows && 0 <= nc && nc < columns && !visited_knights[sr][sc][nr][nc]) {
                    to_visit.push_back(mp(nr, nc));
                }
            }

            // prioritize being closer to the king if you have a choice of ordering the next BFS layer!
            sort(to_visit.begin(), to_visit.end(), [](const pii& lhs, const pii& rhs) {
                return dist_king[lhs.first][lhs.second] < dist_king[rhs.first][rhs.second];
            });

            for (auto [nr, nc] : to_visit) {
                visited_knights[sr][sc][nr][nc] = true;
                dist_knights[sr][sc][nr][nc] = dist_knights[sr][sc][r][c] + 1;
                dist_pickup[sr][sc][nr][nc] = min(dist_pickup[sr][sc][r][c], dist_king[nr][nc]);
                Q.push(mp(nr, nc));
            }
        }
    }

    int ans = INF;

    // Test which of the cells is cheapest for everyone to get to and report that distance
    for (int target_row = 0; target_row < rows; target_row++) {
        for (int target_col = 0; target_col < columns; target_col++) {
            int knight_sum = 0;
            int king_sum = dist_king[target_row][target_col];

            for (auto [r, c] : knights) {
                if (visited_knights[r][c][target_row][target_col]) {
                    knight_sum += dist_knights[r][c][target_row][target_col];
                    king_sum = min(king_sum, dist_pickup[r][c][target_row][target_col]);
                }
                else {
                    knight_sum = INF;
                    king_sum = INF;
                    break;
                }
            }

            ans = min(ans, knight_sum + king_sum);
        }
    }

    cout << ans << "\n";
}