/*
ID: bwliang1
LANG: C++17
TASK: contact
*/

#include <bits/stdc++.h>
using namespace std;

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
    setIO("contact");

    int a, b, n;
    cin >> a >> b >> n;

    string text, line;
    while (getline(cin, line)) {
        text.append(line);
    }

    map<string, int> frequency;
    for (int l = a; l <= b; ++l) {
        if (l > text.length()) {
            break;
        }

        for (int i = 0; i <= text.length() - l; i++) {
            frequency[text.substr(i, l)]++;
        }
    }

    map<int, vector<string>> items;
    for (auto [bit_string, cnt] : frequency) {
        items[cnt].push_back(bit_string);
    }

    int printed = 0;
    for (auto iter = items.rbegin(); iter != items.rend(); iter++) {
        cout << iter->first << endl;

        sort(iter->second.begin(), iter->second.end(), [](const string& lhs, const string& rhs) {
            return lhs.length() < rhs.length() || lhs < rhs;
        });

        for (int i = 0; i < iter->second.size(); i++) {
            cout << iter->second[i] << ((i % 6 == 5 || i == iter->second.size() - 1) ? "\n" : " ");
        }

        if (++printed == n) {
            break;
        }
    }
}