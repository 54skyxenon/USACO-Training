/*
ID: bwliang1
LANG: C++17
TASK: butter
*/

#include <bits/stdc++.h>
using namespace std;

#define INF 1e9
#define pii pair<int, int>
#define mp make_pair

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
    setIO("butter");
    int n, p, c;
    cin >> n >> p >> c;

    vector<int> pasture(n);
    for (int i = 0; i < n; i++) {
        cin >> pasture[i];
        pasture[i]--;
    }

    vector<vector<pii>> graph(p);
    for (int i = 0; i < c; i++) {
        int src, dest, cost;
        cin >> src >> dest >> cost;
        src--;
        dest--;
        graph[src].push_back(mp(dest, cost));
        graph[dest].push_back(mp(src, cost));
    }

    // Prefer running N Dijkstra's to Floyd-Warshall as N < P
    vector<vector<int>> dist(p, vector<int>(p, INF));
    for (int start_pasture : pasture) {
        dist[start_pasture][start_pasture] = 0;

        priority_queue<pii> Q;
        Q.push(mp(0, start_pasture));

        while (!Q.empty()) {
            auto [d, src] = Q.top(); Q.pop();
            d = -d;

            if (d > dist[start_pasture][src]) {
                continue;
            }

            for (auto [nei, cost] : graph[src]) {
                if (dist[start_pasture][nei] > cost + d) {
                    dist[start_pasture][nei] = cost + d;
                    Q.push(mp(-dist[start_pasture][nei], nei));
                }
            }
        }
    }

    int ans = INF;
    for (int i = 0; i < p; i++) {
        int candidate = 0;
        for (int start_pasture : pasture) {
            candidate += dist[start_pasture][i];
        }
        ans = min(ans, candidate);
    }
    cout << ans << '\n';
}