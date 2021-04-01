#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

long long sum(vector<int> &a);

int main() {
	int N = 0;

	cin >> N;




	return 0;
}

long long sum(vector<int> &a) {

	return 0.0;
}
/* 4344 평균은 맞겠지 */
/*
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


int main() {
	int N = 0;

	cin >> N;


	for (int i = 0; i < N; i++) {

		int sum = 0;
		double avg = 0;

		int n = 0;

		cin >> n;

		vector<int> v(n, 0);
		for (int j = 0; j < n; j++) {
			cin >> v[j];
			sum += v[j];
		}

		avg = (double)sum / (double)n;
		// cnt/N * 100
		int cnt = 0;

		for (int j = 0; j < n; j++) {
			if (avg < v[j]) cnt++;
		}

		double per = round((double)cnt / (double)n * 100000) / 1000;

		cout << fixed;
		cout.precision(3);
		cout << per << "%" << endl;
	}

	return 0;
}
*/