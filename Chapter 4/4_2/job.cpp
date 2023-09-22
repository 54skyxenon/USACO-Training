/*
ID: bwliang1
TASK: job
LANG: C++17
*/

#include <bits/stdc++.h>
using namespace std;

#define pii pair<int, int>
#define mp make_pair
#define INF 2e9

int n, m1, m2;
vector<int> a_machines, b_machines;

void setIO(string s) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

int score(vector<pii>& assigned) {
    return assigned.empty() ? 0 : assigned.back().second;
}

vector<pii> accommodate(int job_start, int worker_duration, vector<pii> worker_assigned) {
    worker_assigned.insert(worker_assigned.begin(), mp(job_start, job_start + worker_duration));

    for (int i = 1; i < worker_assigned.size(); i++) {
        if (worker_assigned[i].first < worker_assigned[i - 1].second) {
            int shift_up = worker_assigned[i - 1].second - worker_assigned[i].first;
            worker_assigned[i].first += shift_up;
            worker_assigned[i].second += shift_up;
        }
    }

    return worker_assigned;
}

vector<int> summarize(vector<vector<pii>>& assigned) {
    vector<int> taken;
    for (auto worker_assigned : assigned) {
        for (auto [start, end] : worker_assigned) {
            taken.push_back(end);
        }
    }
    sort(taken.begin(), taken.end());
    return taken;
}

vector<int> solve(vector<int>& workers, vector<int>& jobs, vector<vector<pii>>& assigned) {
    if (jobs.empty()) {
        return summarize(assigned);
    }
    
    int best_worker = -1;
    int best_score = INF;

    for (int i = 0; i < workers.size(); i++) {
        vector<pii> new_assigned = accommodate(jobs.back(), workers[i], assigned[i]);
        int new_score = score(new_assigned);
        if (new_score < best_score) {
            best_worker = i;
            best_score = new_score;
        }
    }

    assigned[best_worker] = accommodate(jobs.back(), workers[best_worker], assigned[best_worker]);
    jobs.pop_back();
    return solve(workers, jobs, assigned);
}

int main() {
    setIO("job");
    cin >> n >> m1 >> m2;

    a_machines.resize(m1);
    for (int& a : a_machines) {
        cin >> a;
    }

    b_machines.resize(m2);
    for (int& b : b_machines) {
        cin >> b;
    }

    sort(a_machines.begin(), a_machines.end());
    sort(b_machines.begin(), b_machines.end());

    vector<int> jobs_a(n);
    vector<vector<pii>> a_assigned(n), b_assigned(n);

    vector<int> a_finish_times = solve(a_machines, jobs_a, a_assigned);
    cout << a_finish_times.back() << " ";
    vector<int> b_finish_times = solve(b_machines, a_finish_times, b_assigned);
    cout << b_finish_times.back() << "\n";
}