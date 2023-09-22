/*
ID: bwliang1
TASK: cowxor
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define pii pair<int, int>
#define mp make_pair
#define mt make_tuple

vector<pii> cows;

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

bool bs_0_ok(int mid, int shift) {
    return (cows[mid].first & (1 << shift)) == 0;
}

// Find the highest bound for the last 0.
int bs_0(int lo, int hi, int shift) {
    if (!bs_0_ok(lo, shift)) {
        return -1;
    }

    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        if (!bs_0_ok(mid, shift)) {
            hi = mid - 1;
        }
        else {
            lo = mid;
        }
    }
        
    return lo;
}

bool bs_1_ok(int mid, int shift) {
    return (cows[mid].first & (1 << shift)) > 0;
}

// Find the lowest bound for the first 1.
int bs_1(int lo, int hi, int shift) {
    if (!bs_1_ok(hi, shift)) {
        return -1;
    }

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (!bs_1_ok(mid, shift)) {
            lo = mid + 1;
        }
        else {
            hi = mid;
        }
    }
    
    return lo;
}

pii walk(bitset<21>& complement, int idx, int lo, int hi) {
    if (lo == hi || idx == complement.size()) {
        return cows[lo];
    }

    if (complement[20 - idx]) {
        int lower_bound = bs_1(lo, hi, 20 - idx);
        if (lower_bound != -1) {
            return walk(complement, idx + 1, lower_bound, hi);
        }
    }
    else { // bit is a 0
        int upper_bound = bs_0(lo, hi, 20 - idx);
        if (upper_bound != -1) {
            return walk(complement, idx + 1, lo, upper_bound);
        }
    }

    return walk(complement, idx + 1, lo, hi);
}

int main() {
    setIO("cowxor");

    int n;
    cin >> n;

    cows.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> cows[i].first;
        cows[i].second = i;
        cows[i].first ^= cows[i - 1].first;
    }
    sort(cows.begin(), cows.end());

    pii best_bounds = mp(0, 0);
    int best_xor = INT_MIN;
    int best_length = 0;

    for (int k = 1; k <= n; k++) {
        auto [curr_xor, i] = cows[k];
        bitset<21> bitmask(curr_xor);
        auto [target_xor, j] = walk(bitmask.flip(), 0, 0, n);

        // If XOR tied, choose the sequence for which its last cow has the highest rank.
        // If there still is a tie, choose the shortest sequence.
        pii curr_bounds = mp(min(i, j), max(i, j));
        curr_xor = target_xor ^ curr_xor;
        int curr_length = curr_bounds.second - curr_bounds.first;
        
        if (mt(curr_xor, -curr_bounds.second, -curr_length) > mt(best_xor, -best_bounds.second, -best_length)) {
            best_bounds = curr_bounds;
            best_xor = curr_xor;
            best_length = curr_length;
        }
    }

    cout << best_xor << " " << (best_bounds.first + 1) << " " << best_bounds.second << '\n';
}