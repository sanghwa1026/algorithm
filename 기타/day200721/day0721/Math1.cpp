#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {
	//5킬로 그램, 3킬로 그램 봉지

	int N;

	cin >> N;

	int ans = -1;

	if (N >= 5 && N % 5 == 0) ans = N / 5;
	else if(N>=5 && N % 5 > 0) {

		int tmpMod = 1;
		int tmp = N ;
		int i = 1;

		int sum = 0;
		while (tmpMod != 0) {
			
			tmp = (N - (5 * i)) / 3;
			tmpMod = (N - (5 * i)) % 3;

			sum = i + tmp;
			cout << sum << endl;
			i++;
		}
		ans = sum;
	}

	
	if (ans == -1 && N % 3 == 0) {
		ans = N / 3;
	}
	
	

	cout << ans;

	return 0;
}


/* 1712 손익분기점 */

/*
#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {

	//A 초기 비용(고정)
	//B 가변 비용
	//C 판매가격

	int A, B, C;

	cin >> A;
	cin >> B;
	cin >> C;

	int ans = 1;

	if (B >= C) cout << "-1";
	else {
		cout << A / (C - B) + 1;
	}

	return 0;
}
*/