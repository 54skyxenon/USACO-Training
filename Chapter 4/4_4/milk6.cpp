/*
ID: bwliang1
TASK: milk6
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define tiii tuple<int, int, int>
#define mt make_tuple

int n, m;

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

// Ford Fulkerson was adapted from GeeksForGeeks
// https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem
bool BFS(vector<vector<int>>& rGraph, int s, int t, vector<int>& parent) {
    vector<bool> visited(n, false);
    queue<int> q({s});
    visited[s] = true;
    parent[s] = -1;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < n; v++) {
            if (!visited[v] && rGraph[u][v] > 0) {
                if (v == t) {
                    parent[v] = u;
                    return true;
                }
                q.push(v);
                parent[v] = u;
                visited[v] = true;
            }
        }
    }

    return false;
}

int ford_fulkerson(vector<vector<int>> graph, int s, int t) {
    int u, v;

    vector<vector<int>> rGraph = graph;
    vector<int> parent(n); 
    int max_flow = 0;

    // Augment the flow while there is path from source to sink
    while (BFS(rGraph, s, t, parent)) {
        int path_flow = INT_MAX;

        for (v = t; v != s; v = parent[v]) {
            u = parent[v];
            path_flow = min(path_flow, rGraph[u][v]);
        }

        for (v = t; v != s; v = parent[v]) {
            u = parent[v];
            rGraph[u][v] -= path_flow;
            rGraph[v][u] += path_flow;
        }

        max_flow += path_flow;
    }

    return max_flow;
}

int main() {
    setIO("milk6");
    cin >> n >> m;

    vector<vector<int>> graph(n, vector<int>(n));
    vector<tiii> edges;

    for (int i = 0; i < m; i++) {
        int s, e, c;
        cin >> s >> e >> c;
        graph[s - 1][e - 1] += c;
        edges.push_back(mt(s - 1, e - 1, i));
    }

    sort(edges.begin(), edges.end(), [&](const tiii& lhs, const tiii& rhs) {
        return graph[get<0>(lhs)][get<1>(lhs)] > graph[get<0>(rhs)][get<1>(rhs)];
    });

    int min_cut = 0;
    vector<int> cut;

    for (auto [s, e, i] : edges) {
        int flow_now = ford_fulkerson(graph, 0, n - 1);
        int capacity = graph[s][e];
        graph[s][e] -= capacity;
        int flow_after = ford_fulkerson(graph, 0, n - 1);
        if (flow_after + capacity == flow_now) {
            min_cut += capacity;
            cut.push_back(i + 1);
        }
        else {
            graph[s][e] += capacity;
        }
    }

    cout << min_cut << " " << cut.size() << '\n';
    sort(cut.begin(), cut.end());
    for (auto truck : cut) {
        cout << truck << '\n';
    }
}