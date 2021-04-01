// day0709.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>

using namespace std;

int main()
{
	int N = 5;

	int sum = 0;
	for (int i = 0; i < N; i++) {
		int score = 0;

		cin >> score;

		if (score < 40) score = 40;

		sum += score;

	}

	cout << sum / N;
}


/* 11022 A+B-8 */
/*
int main()
{
	int N = 0;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int A = 0;
		int B = 0;

		cin >> A;
		cin >> B;

		cout << "Case #" << i + 1 << ": " << A << " + " << B << " = " << A + B << endl;

	}
}
*/


/* 2438 별 찍기-1 */

/*

int main()
{
	int N = 0;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < i + 1; j++) {
			cout << "*";
		}

		cout << endl;

	}
}


*/

/* 2439 별 찍기-2 */

/*
int main()
{
	int N = 0;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N-(i+1); j++) {
			cout << " ";
		}

		for (int j = 0; j < i+1; j++) {
			cout << "*";
		}

		cout << endl;

	}
}
*/

/* 10871 X보다 작은 수 */

/*
int main()
{
	int N = 0;
	int X = 0;

	cin >> N;
	cin >> X;

	for (int i = 0; i < N; i++) {
		int temp = 0;

		cin >> temp;

		if (temp < X) cout << temp << " ";
	}
}
*/


/* 10952 A+B - 5 */

/*

int main()
{
	int A = -1;
	int B = -1;

	cin >> A;
	cin >> B;

	do {
		cout << A + B << endl;

		cin >> A;
		cin >> B;
	} while (A != 0 && B != 0);
}

*/

/* 10951 A+B - 4 */

/*

#include <iostream>

using namespace std;

int main()
{
	int A = -1;
	int B = -1;

	while (cin >> A >> B) {
		cout << A + B << endl;
	}
}

*/

/* 1110 더하기 사이클 */

/*

int main()
{
	int N;

	cin >> N;

	int temp = N;
	int cnt = 0;

	do {

		if (((temp / 10) + (temp % 10)) >= 10) {
			temp = ((temp % 10) * 10) + ((temp / 10) + (temp % 10)) - 10;
		}
		else {
			temp = ((temp % 10) * 10) + ((temp / 10) + (temp % 10));
		}

		//cout << temp << endl;
		cnt++;
	} while (temp != N);

	cout << cnt;

}

*/

/* 10039 평균 점수 */

/*
int main()
{
	int N = 5;

	int sum = 0;
	for (int i = 0; i < N; i++) {
		int score = 0;

		cin >> score;

		if (score < 40) score = 40;

		sum += score;

	}

	cout << sum / N;
}
*/
