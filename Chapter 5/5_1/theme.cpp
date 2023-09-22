/*
ID: bwliang1
TASK: theme
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int n;
vector<int> differences;
vector<int> suffixes;

int lcp(vector<int>& A, vector<int>& B) {
    int lcp_length = 0;

    for (int i = 0; i < min(A.size(), B.size()); i++) {
        if (A[i] != B[i]) {
            break;
        }
        lcp_length++;
    }

    return lcp_length;
}

int main() {
    setIO("theme");
    cin >> n;

    vector<int> notes(n);

    for (int i = 0; i < n; i++) {
        cin >> notes[i];
        suffixes.push_back(i);
    }
    
    for (int i = 1; i < n; i++) {
        differences.push_back(notes[i] - notes[i - 1]);
    }

    sort(suffixes.begin(), suffixes.end(), [](const int& lhs, const int& rhs) {
        vector<int> v_lhs(differences.begin() + lhs, differences.end());
        vector<int> v_rhs(differences.begin() + rhs, differences.end());
        return v_lhs < v_rhs;
    });

    vector<int> lcp_sa(suffixes.size());
    for (int i = 1; i < suffixes.size(); i++) {
        vector<int> v_prev(differences.begin() + suffixes[i - 1], differences.end());
        vector<int> v_curr(differences.begin() + suffixes[i], differences.end());
        lcp_sa[i] = lcp(v_prev, v_curr);
    }

    int ans = 0;
    for (int i = 0; i < suffixes.size() - 1; i++) {
        int suffix_i = suffixes[i];
        int curr_lcp_length = differences.size() - suffix_i;

        for (int j = i + 1; j < suffixes.size(); j++) {
            curr_lcp_length = min(curr_lcp_length, lcp_sa[j]);
            int suffix_j = suffixes[j];
            int dist = abs(suffix_i - suffix_j) - 1;
            ans = max(ans, min(dist, curr_lcp_length) + 1);
        }
    }

    cout << ((ans < 5) ? 0 : ans) << '\n';
}