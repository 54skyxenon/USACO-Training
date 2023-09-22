/*
ID: bwliang1
LANG: C++17
TASK: charrec
*/

#include <bits/stdc++.h>
using namespace std;

#define NUM_CHARS 27
#define CHAR_ROWS 20
#define THRESHOLD 120
#define INF 1e9
#define State pair<string, int>

vector<vector<int>> ideal;
vector<string> CHARS = {
    " ", "a", "b", "c", "d", "e", "f", "g", "h",
    "i", "j", "k", "l", "m", "n", "o", "p", "q", 
    "r", "s", "t", "u", "v", "w", "x", "y", "z"
};

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int bitmask(string& line) {
    int mask = 0;
    int power = 1;

    for (int col = 0; col < CHAR_ROWS; col++) {
        if (line[col] == '1') {
            mask += power;
        }
        power *= 2;
    }

    return mask;
}

void read_font_file() {
    ifstream font_file("font.in");
    string line;
    getline(font_file, line);

    for (int c_idx = 0; c_idx < CHARS.size(); c_idx++) {
        vector<int> char_lines;
        for (int i = 0; i < CHAR_ROWS; ++i) {
            getline(font_file, line);
            char_lines.push_back(bitmask(line));
        }
        ideal.push_back(char_lines);
    }

    font_file.close();
}

int corruption(int n1, int n2) {
    // AKA the hamming distance
    int x = n1 ^ n2;
    int set_bits = 0;
 
    while (x > 0) {
        set_bits += x & 1;
        x >>= 1;
    }
 
    return set_bits;
}

int main() {
    setIO("charrec");
    read_font_file();

    int n;
    cin >> n;

    vector<int> all_input(n);
    for (int i = 0; i < n; i++) {
        string line;
        cin >> line;
        all_input[i] = bitmask(line);
    }

    vector<State> dp(n + 1, make_pair("", INF));
    dp[n] = make_pair("", 0);

    for (int i = n - 19; i >= 0; i--) {
        string best_char = "";
        int best_cost = INF;

        // take the next 19 rows
        {
            string best19_char = "";
            int best19_cost = INF;

            for (int j = 0; j < NUM_CHARS; j++) {
                // which row in the IDEAL image to skip
                for (int skip = 0; skip < CHAR_ROWS; skip++) {
                    int cost = 0;
                    int other_row = 0;

                    for (int row = 0; row < 19; row++) {
                        if (other_row == skip) {
                            other_row++;
                        }
                        cost += corruption(ideal[j][other_row], all_input[i + row]);
                        other_row++;
                    }

                    if (cost < best19_cost) {
                        best19_char = CHARS[j];
                        best19_cost = cost;
                    }
                }
            }

            best19_char = ((best19_cost > THRESHOLD) ? "?" : best19_char) + dp[i + 19].first;
            best19_cost = best19_cost + dp[i + 19].second;

            if (best19_cost < best_cost) {
                best_char = best19_char;
                best_cost = best19_cost;
            }
        }

        // take the next 20 rows
        if (i < n - 19) {
            string best20_char = "";
            int best20_cost = INF;

            for (int j = 0; j < NUM_CHARS; j++) {
                int cost = 0;

                for (int row = 0; row < CHAR_ROWS; row++) {
                    cost += corruption(ideal[j][row], all_input[i + row]);
                }

                if (cost < best20_cost) {
                    best20_char = CHARS[j];
                    best20_cost = cost;
                }
            }

            best20_char = ((best20_cost > THRESHOLD) ? "?" : best20_char) + dp[i + 20].first;
            best20_cost = best20_cost + dp[i + 20].second;

            if (best20_cost < best_cost) {
                best_char = best20_char;
                best_cost = best20_cost;
            }
        }

        // take the next 21 rows
        if (i < n - 20) {
            string best21_char = "";
            int best21_cost = INF;

            for (int j = 0; j < NUM_CHARS; j++) {
                // which row in the EVALUATION image to skip
                for (int skip = 0; skip < CHAR_ROWS; skip++) {
                    int cost = 0;
                    int other_row = 0;

                    for (int row = 0; row < 21; row++) {
                        if (row == skip) {
                            continue;
                        }
                        
                        cost += corruption(ideal[j][other_row], all_input[i + row]);
                        other_row++;
                    }

                    if (cost < best21_cost) {
                        best21_char = CHARS[j];
                        best21_cost = cost;
                    }
                }
            }

            best21_char = ((best21_cost > THRESHOLD) ? "?" : best21_char) + dp[i + 21].first;
            best21_cost = best21_cost + dp[i + 21].second;

            if (best21_cost < best_cost) {
                best_char = best21_char;
                best_cost = best21_cost;
            }
        }

        dp[i] = make_pair(best_char, best_cost);
    }

    cout << dp[0].first << '\n';
}