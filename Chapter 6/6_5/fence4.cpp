/*
ID: bwliang1
TASK: fence4
LANG: C++17
*/

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>
using namespace std;

#define RAY_SLOPE_THRESHOLD 1000000

void setIO(string s) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen((s + ".in").c_str(), "r", stdin);
    freopen((s + ".out").c_str(), "w", stdout);
}

struct Point {
    double x, y;
    Point(double x=0, double y=0) : x(x), y(y) {}

    double dist(Point& other) {
        return pow(this->x - other.x, 2) + pow(this->y - other.y, 2);
    }

    // less than operator for sorting
    bool operator<(const Point& other) const {
        if (this->x != other.x) {
            return this->x < other.x;
        }
        return this->y < other.y;
    }
};

int n;
Point observer;
vector<Point> points;
map<double, set<double>> points_search;
map<Point, int> point_index;

class LineSegment {
public:
    Point p1, p2;

    LineSegment(Point& p1, Point& p2) {
        this->p1 = p1;
        this->p2 = p2;
    }

    int orientation(Point& p, Point& q, Point& r) {
        // to find the orientation of an ordered triplet (p, q, r) function returns the following values:
        // 0: Collinear points
        // 1: Clockwise points
        // 2: Counterclockwise
        double val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
        if (val > 0) {
            return 1;
        }
        else if (val < 0) {
            return 2;
        }
        else {
            return 0;
        }
    }

    bool on_segment(Point& p, Point& q, Point& r) {
        return q.x <= max(p.x, r.x) && q.x >= min(p.x, r.x) && q.y <= max(p.y, r.y) && q.y >= min(p.y, r.y);
    }

    bool intersects(LineSegment& other) {
        Point p1 = this->p1;
        Point q1 = this->p2;
        Point p2 = other.p1;
        Point q2 = other.p2;

        // Find the 4 orientations required for the general and special cases
        int o1 = this->orientation(p1, q1, p2);
        int o2 = this->orientation(p1, q1, q2);
        int o3 = this->orientation(p2, q2, p1);
        int o4 = this->orientation(p2, q2, q1);
    
        // General case
        if (o1 != o2 && o3 != o4)
            return true;
    
        // Special Cases
        // p1, q1 and p2 are collinear and p2 lies on segment p1q1
        if (o1 == 0 && this->on_segment(p1, p2, q1))
            return true;
    
        // p1, q1 and q2 are collinear and q2 lies on segment p1q1
        if (o2 == 0 && this->on_segment(p1, q2, q1))
            return true;
    
        // p2, q2 and p1 are collinear and p1 lies on segment p2q2
        if (o3 == 0 && this->on_segment(p2, p1, q2))
            return true;
    
        // p2, q2 and q1 are collinear and q1 lies on segment p2q2
        if (o4 == 0 && this->on_segment(p2, q1, q2))
            return true;
    
        // If none of the cases
        return false;
    }

    Point find_intersection(LineSegment& other) {
        double x1 = this->p1.x;
        double y1 = this->p1.y;
        double x2 = this->p2.x;
        double y2 = this->p2.y;
        double x3 = other.p1.x;
        double y3 = other.p1.y;
        double x4 = other.p2.x;
        double y4 = other.p2.y;
        double px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4));
        double py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4));
        return Point(px, py);
    }

    friend ostream& operator<<(ostream& stream, const LineSegment& ls) {
        Point p1, p2;

        if (point_index[ls.p1] <= point_index[ls.p2]) {
            p1 = ls.p1;
            p2 = ls.p2;
        }
        else {
            p1 = ls.p2;
            p2 = ls.p1;
        }
        
        stream << p1.x << ' ' << p1.y << ' ' << p2.x << ' ' << p2.y;
        return stream;
    }

    // Sort the segments for output by examining the last point and showing first those points that are earlier in the input. 
    bool operator<(const LineSegment& other) const {
        Point self_last_point = point_index[this->p1] <= point_index[this->p2] ? this->p2 : this->p1;
        Point other_last_point = point_index[other.p1] <= point_index[other.p2] ? other.p2 : other.p1;
        return point_index[self_last_point] < point_index[other_last_point];
    }
};

int main() {
    setIO("fence4");
    cin >> n;

    int ox, oy;
    cin >> ox >> oy;
    observer.x = double(ox);
    observer.y = double(oy);

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        points.push_back(Point(double(x), double(y)));
        points_search[x].insert(y);
        point_index[points.back()] = i;
    }

    // Test an ordered list of vertices (x_i, y_i) to see if the array is a valid fence
    vector<LineSegment> added_lines;

    for (int i = 0; i < n; i++) {
        LineSegment ls(points[(i - 1 + n) % n], points[i]);

        vector<LineSegment> can_touch;
        if (!added_lines.empty()) {
            if (i == n - 1) {
                move(added_lines.begin() + 1, added_lines.end() - 1, back_inserter(can_touch));
            }
            else {
                move(added_lines.begin(), added_lines.end() - 1, back_inserter(can_touch));
            }
        }

        if (any_of(can_touch.begin(), can_touch.end(), [&](LineSegment prev_line) {
            return ls.intersects(prev_line);
        })) {
            cout << "NOFENCE\n";
            return 0;
        }

        added_lines.push_back(ls);
    }

    set<int> visible;

    int elapsed = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            Point& l1 = points[i];
            Point& l2 = points[j];
            Point midpoint = Point((l1.x + l2.x) / 2, (l1.y + l2.y) / 2);

            // extend to a point so far that we can test for intersections
            double dx = midpoint.x - observer.x;
            double dy = midpoint.y - observer.y;
            Point ray_end = Point(midpoint.x + dx * RAY_SLOPE_THRESHOLD, midpoint.y + dy * RAY_SLOPE_THRESHOLD);
            LineSegment ray(observer, ray_end);

            double best_dist = 2e14;
            tuple<Point, int, int> best_hit = make_tuple(Point(RAY_SLOPE_THRESHOLD, RAY_SLOPE_THRESHOLD), 0, -1);
            vector<tuple<Point, int, int>> hits;

            for (int line_num = 0; line_num < added_lines.size(); line_num++) {
                LineSegment& line = added_lines[line_num];
                if (ray.intersects(line)) {
                    Point intersection_point = ray.find_intersection(line);
                    int is_point = points_search[intersection_point.x].count(intersection_point.y);

                    double this_dist = intersection_point.dist(observer);
                    if (this_dist < best_dist || this_dist == best_dist && is_point < get<1>(best_hit)) {
                        best_hit = make_tuple(intersection_point, -is_point, line_num);
                        best_dist = this_dist;
                    }
                }
            }

            if (get<2>(best_hit) > -1) {
                auto& [_, in_points_search, hit_line] = best_hit;
                
                if (in_points_search == 0) {
                    visible.insert(hit_line);
                }
            }
        }
    }

    vector<LineSegment> visible_segments;
    for (int line_num : visible) {
        visible_segments.push_back(added_lines[line_num]);
    }
    
    cout << visible_segments.size() << '\n';
    sort(visible_segments.begin(), visible_segments.end());
    for (LineSegment& segment : visible_segments) {
        cout << segment << '\n';
    }
}