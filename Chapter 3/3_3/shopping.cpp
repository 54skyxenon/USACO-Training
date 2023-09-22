/*
ID: bwliang1
TASK: shopping
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define INF 2e9
#define MAX_QUANTITY 6
#define MAX_PRODUCTS 5

int s, b;
int dp[MAX_QUANTITY][MAX_QUANTITY][MAX_QUANTITY][MAX_QUANTITY][MAX_QUANTITY];

vector<pair<int, map<int, int>>> offers;
vector<int> product, needed;
map<int, int> price;

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main() {
    setIO("shopping");
    
    cin >> s;
    for (int i = 0; i < s; i++) {
        int num_packages;
        cin >> num_packages;

        map<int, int> package;
        while (num_packages--) {
            int c, k;
            cin >> c >> k;
            package[c] = k;
        }

        int deal;
        cin >> deal;
        offers.push_back(make_pair(deal, package));
    }

    cin >> b;
    for (int i = 0; i < b; i++) {
        int c, k, p;
        cin >> c >> k >> p;
        price[c] = p;
        product.push_back(c);
        needed.push_back(k);
    }

    for (int i = 0; i < MAX_PRODUCTS - b; i++) {
        product.push_back(0);
        needed.push_back(0);
    }

    for (int i = 0; i < MAX_QUANTITY; i++) {
        for (int j = 0; j < MAX_QUANTITY; j++) {
            for (int k = 0; k < MAX_QUANTITY; k++) {
                for (int l = 0; l < MAX_QUANTITY; l++) {
                    for (int m = 0; m < MAX_QUANTITY; m++) {
                        if (i + j + k + l + m == 0) {
                            dp[i][j][k][l][m] = 0;
                            continue;
                        }

                        vector<int> have({i, j, k, l, m});

                        int ans = INF;
                        for (auto [deal, package] : offers) {
                            vector<int> bought;
                            for (int n = 0; n < MAX_PRODUCTS; n++) {
                                bought.push_back(have[n] - package[product[n]]);
                            }

                            if (all_of(bought.begin(), bought.end(), [](int remaining) { return remaining >= 0; })) {
                                ans = min(ans, deal + dp[bought[0]][bought[1]][bought[2]][bought[3]][bought[4]]);
                            }
                        }
                        
                        for (int n = 0; n < MAX_PRODUCTS; n++) {
                            vector<int> bought = have;
                            if (have[n] > 0) {
                                bought[n]--;
                                ans = min(ans, price[product[n]] + dp[bought[0]][bought[1]][bought[2]][bought[3]][bought[4]]);
                            }
                        }

                        dp[i][j][k][l][m] = ans;
                    }
                }
            }
        }
    }

    cout << dp[needed[0]][needed[1]][needed[2]][needed[3]][needed[4]] << '\n';
}