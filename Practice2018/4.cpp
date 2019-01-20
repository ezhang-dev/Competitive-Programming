#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <numeric>
using namespace std;
template<typename T> priority_queue<int> print_queue(T& q) {
    std::priority_queue<int> z;
    while(!q.empty()) {
        std::cout << q.top() << " ";
        z.push(q.top());
        q.pop();
    }
    std::cout << '\n';
    return z;
}
string solve( uint64_t a, uint64_t b){
    std::priority_queue< uint64_t> q;
    q.push(a);
    uint64_t n;
    for(uint64_t _=0;_<b;_++){
        n=q.top();
        q.pop();
        q.push((n-1)/2);
        q.push(n/2);
        //q=print_queue(q);
    }
    return std::to_string(n/2)+" "+std::to_string((n-1)/2);

}


int main() {
    int test_cases;
	cin >> test_cases;
	for (int test_case = 1; test_case <= test_cases; test_case++) {
		uint64_t a;
		cin >> a;
        uint64_t b;
		cin >> b;
		cout << "Case #" << test_case << ": " << solve(a,b) << endl;
		cout.flush();
		cerr<<test_case<< endl;
	}
	return 0;
}
