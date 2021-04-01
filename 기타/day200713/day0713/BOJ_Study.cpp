#include <iostream>

using namespace std;

int main() {

	int N = 0;

	cin >> N;

	int cnt = N;
	
	//역피라미드
	for (int i = 0; i < N-1; i++) {
		for (int j = 0; j < N - cnt; j++) { // 공백
			cout << " ";
		}

		for (int j = 0; j < 2 * cnt - 1; j++) {
			cout << "*";
		}
		

		cnt--;

		cout << endl;
	}
	
	cnt = 1;
	//피라미드
	for (int i = 0; i < N; i++ ) {
		for (int j = 0; j < N - cnt; j++) { // 공백
			cout << " ";
		}

		for (int j = 0; j < 2*cnt-1; j++) {
			cout << "*";
		}
		cnt++;

		cout << endl;
	}

	return 0;
}

/* 2523 별 찍기 13 */

/*
int main() {

	int N = 0;

	cin >> N;

	int cnt = 1;
	for (int i = 0; i < 2 * N - 1; i++) {


		for (int j = 0; j < cnt; j++) {
			cout << "*";
		}
		cout << endl;
		if (i < N-1) {
			cnt++;
		}
		else {
			cnt--;
		}

	}

	return 0;
}

*/

/* 2446 별 찍기 - 9 */

/*

*/

/* 10996 별 찍기 - 21 */

/*
#include <iostream>

using namespace std;

int main() {

	int N = 0;

	cin >> N;

	int cnt = N;

	//역피라미드
	for (int i = 0; i < N-1; i++) {
		for (int j = 0; j < N - cnt; j++) { // 공백
			cout << " ";
		}

		for (int j = 0; j < 2 * cnt - 1; j++) {
			cout << "*";
		}


		cnt--;

		cout << endl;
	}

	cnt = 1;
	//피라미드
	for (int i = 0; i < N; i++ ) {
		for (int j = 0; j < N - cnt; j++) { // 공백
			cout << " ";
		}

		for (int j = 0; j < 2*cnt-1; j++) {
			cout << "*";
		}
		cnt++;

		cout << endl;
	}

	return 0;
}
*/