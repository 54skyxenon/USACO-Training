/*
ID: bwliang1
TASK: calfflac
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define pii pair<int, int>
#define mp make_pair

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
    setIO("calfflac");
    
    string s;
    char c;
    while (cin.get(c)) {
        s += c;
    }

    vector<pair<char, int>> data;
    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i])) {
            data.push_back(mp(tolower(s[i]), i));
        }
    }

    int ans_len = 0;
    pii ans = mp(-1, -1);

    for (int i = 0; i < data.size(); i++) {
        // test odd-length centered here
        int l = i;
        int r = i;
        int run = 0;
        while (l >= 0 && r < data.size() && data[l].first == data[r].first) {
            run += 1 + (l != r);
            if (run > ans_len) {
                ans_len = run;
                ans = mp(l, r);
            }
            l--;
            r++;
        }

        // test even-length starting before
        if (i > 0) {
            l = i - 1;
            r = i;
            run = 0;
            while (l >= 0 && r < data.size() && data[l].first == data[r].first) {
                run += 2;
                if (run > ans_len) {
                    ans_len = run;
                    ans = make_pair(l, r);
                }
                l--;
                r++;
            }
        }
    }

    int ans_start = ans.first;
    int ans_end = ans.second;

    cout << ans_len << endl;
    int true_first = data[ans_start].second;
    int true_last = data[ans_end].second + 1;

    for (int ptr = true_first; ptr < true_last; ptr += 80) {
        cout << s.substr(ptr, min(true_last - ptr, 80));
    }
    cout << '\n';
}