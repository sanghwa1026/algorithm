#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N = 0;

	cin >> N;



	for (int i = 0; i < N; i++) {
		int n = 0;

		cin >> n;
		vector<int> score(n, 0);

		int sum = 0;

		for (int j = 0; j < n; j++) {
			cin >> score[j];
			sum += score[j];

		}
	}

	return 0;
}

/* 10996 º° Âï±â - 21 */

/*
#include <iostream>

using namespace std;

int main() {
	int N = 0;
	cin >> N;

	// 2 * N
	if (N == 1) cout << "*";
	else {
		int first = N - N / 2;
		int second = N / 2;

		for (int i = 0; i < N; i++) {

			int cnt = 0;
			int idx = 0;

			while (cnt != first) {
				if (idx % 2 == 0) {
					cout << "*";
					cnt++;
				}
				else {
					cout << " ";
				}
				idx++;
			}
			cnt = 0;
			idx = 0;
			cout << endl;

			while (cnt != second) {
				if (idx % 2 == 1) {
					cout << "*";
					cnt++;
				}
				else {
					cout << " ";
				}
				idx++;
			}

			cout << endl;
		}


	}


	return 0;
}
*/


/* 10818 ÃÖ¼Ò, ÃÖ´ë */

/*
#include <iostream>
#include <limits.h>

using namespace std;

int main() {
	int N = 0;

	cin >> N;

	int min = INT_MAX;
	int max = INT_MIN;

	for (int i = 0; i < N; i++) {
		int n = 0;

		cin >> n;

		if (n < min) min = n;

		if (n > max) max = n;
	}

	cout << min << " " << max;


	return 0;
}

*/

/* 2562 ÃÖ´ñ°ª */

/*
#include <iostream>
#include <limits.h>

using namespace std;

int main() {
	int N = 9;

	int idx = 0;
	int max = INT_MIN;

	for (int i = 0; i < N; i++) {
		int n = 0;

		cin >> n;

		if (max < n) {
			idx = i+1;
			max = n;
		}
	}

	cout << max << endl;
	cout << idx;

	return 0;
}
*/

/* 1546 Æò±Õ */

/*
#include <iostream>
#include <limits.h>
#include <vector>

using namespace std;

int main() {
	int N = 0;

	cin >> N;
	int max = INT_MIN;

	vector<double> score(N, 0);

	double sum = 0;

	for (int i = 0; i < N; i++) {

		cin >> score[i];

		if (score[i] > max) max = score[i];
	}

	for (int i = 0; i < N; i++) {
		sum += score[i] / max * 100;
	}

	cout << sum / N;

	return 0;
}
*/