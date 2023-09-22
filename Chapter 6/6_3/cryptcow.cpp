/*
ID: bwliang1
TASK: cryptcow
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

string plaintext = "Begin the Escape execution at the Break of Dawn";
set<string> substrings;
int encryption_count;

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int letter_count(string& encrypted, char letter) {
    return count_if(
        encrypted.begin(),
        encrypted.end(),
        [&](char c){
            return c == letter;
        }
    );
}

// Lesson learned -- DON'T USE REGEX IT'S SLOW
// Ripped off pruning function from here:
// https://github.com/NerdMomentwDavid/USACOTrainingSolutions/blob/main/Section%206.3%20-%20Cryptcowgraphy.cpp
bool all_in_plaintext(string& s) {
    // Checking prefix
    int l = min(s.size(), plaintext.size());
    for (int i = 0; i < l; i++) {
        if (s[i] == 'C') {
            break;
        }
        if (s[i] != plaintext[i]) {
            return false;
        }
    }
    
    // Checking suffix
    l = s.size();
    int t = plaintext.size() - 1;
    for (int i = l - 1; i >= 0; i--) {
        if (s[i] == 'W') {
            break;
        }

        if (s[i] != plaintext[t--]) {
            return false;
        }
    }
    
    // Checking middle
    t = 0;
    for (int i = 0; i < l; i++) {
        if (s[i] == 'C' || s[i] == 'O' || s[i] == 'W') {
            string tmp = s.substr(t, i - t);
            if (i > t && !substrings.count(tmp)) {
                return false;
            }
            t = i + 1;
        }
    }
    
    return true;
}

pair<int, int> dfs(const string& chars, set<string>& seen, int depth) {
    if (chars == plaintext) {
        return {1, encryption_count};
    }
    
    if (depth == encryption_count) {
        return {0, 0};
    }

    for (int c_idx = 0; c_idx < chars.length(); ++c_idx) {
        if (chars[c_idx] == 'C') {
            for (int o_idx = c_idx + 1; o_idx < chars.length(); ++o_idx) {
                if (chars[o_idx] == 'O') {
                    for (int w_idx = o_idx + 1; w_idx < chars.length(); ++w_idx) {
                        if (chars[w_idx] == 'W') {
                            string before_c = chars.substr(0, c_idx);
                            string between_co = chars.substr(c_idx + 1, o_idx - c_idx - 1);
                            string between_ow = chars.substr(o_idx + 1, w_idx - o_idx - 1);
                            string after_w = chars.substr(w_idx + 1, chars.size() - w_idx - 1);
                            string together = before_c + between_ow + between_co + after_w;

                            if (all_in_plaintext(together) && !seen.count(together)) {
                                seen.insert(together);
                                if (dfs(together, seen, depth + 1).first == 1) {
                                    return {1, encryption_count};
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    return {0, 0};
}

int main() {
    setIO("cryptcow");

    string encrypted;
    getline(cin, encrypted);
    encryption_count = letter_count(encrypted, 'C');

    if (!(encryption_count == letter_count(encrypted, 'O') && encryption_count == letter_count(encrypted, 'W'))) {
        cout << "0 0\n";
        return 0;
    }

    // Generate substrings
    for (int i = 0; i < plaintext.size(); ++i) {
        for (int j = 1; j <= plaintext.size() - i + 1; ++j) {
            substrings.insert(plaintext.substr(i, j));
        }
    }

    set<string> seen({encrypted});
    pair<int, int> result = dfs(encrypted, seen, 0);
    cout << result.first << " " << result.second << '\n';
}
