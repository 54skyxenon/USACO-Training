/*
ID: bwliang1
TASK: problemname
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

void setIO(string s, int argc, char** argv) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    if (argc > 1 && !strcmp(argv[1], "--use-console")) {
        return;
    }

    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int main(int argc, char** argv) {
    setIO("problemname", argc, argv);
    // Write code here...
}
