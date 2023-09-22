/*
ID: bwliang1
TASK: rectbarn
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

// https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/732697/44ms-easy-solution-c/
int largest_rectangle_area(vector<int>& heights) {
    stack<int> st;
    int ans = 0;
    
    heights.push_back(0);
    for (int i = 0; i < heights.size(); i++) {
        while (!st.empty() && heights[st.top()] > heights[i]){
            int top = heights[st.top()];
            st.pop();
            int ran = st.empty() ? -1 : st.top();
            ans = max(ans, top * (i - ran - 1));
        }
        st.push(i);
    }
    heights.pop_back();

    return ans;
}

int main() {
    setIO("rectbarn");

    int r, c, p;
    cin >> r >> c >> p;

    vector<set<int>> banned(r);
    while (p--) {
        int br, bc;
        cin >> br >> bc;
        banned[br - 1].insert(bc - 1);
    }

    int ans = 0;
    vector<int> prefix(r);

    for (int col = 0; col < c; col++) {
        for (int row = 0; row < r; row++) {
            if (banned[row].count(col)) {
                prefix[row] = 0;
            }
            else {
                prefix[row]++;
            }
        }
        ans = max(ans, largest_rectangle_area(prefix));
    }

    cout << ans << '\n';
}