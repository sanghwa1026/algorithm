#include <iostream>
#include <vector>

using namespace std;

/* 1065 �Ѽ� */
int main() {
	
	int N = 0;

	cin >> N;

	int ans = 0;

	for (int i = 1; i <= N; i++) {

		int temp = i;
		bool flag = true;

		if (i >= 100) {

			int eqSub = 1001;
			int pre = temp%10;
			temp /= 10;

			while (temp != 0) {
				int cur = temp % 10;
				int sub = pre - cur;
				
				if (eqSub != 1001 && sub != eqSub) {
					flag = false;
					break;
				}

				eqSub = sub;
				pre = cur;
				temp /= 10;
			}

		}
		
		if (flag) ans++;
	}

	cout << ans;
	return 0;
}


/* 15596 ���� N���� �� */
/*
long long sum(vector<int> a, int n) {
	long long s = 0;

	for (int i = 0; i < a.size(); i++) {
		s += a[i];
	}
	return s;
}
*/

/* 4673 ���� �ѹ� */
/*
#include <iostream>
#include <vector>

using namespace std;

int main() {
	// 1 boolean �迭�� �����ڰ� ���� �Լ������ false�ֵ鸸 ���

	vector<bool> v(20000);

	for (int i = 1; i <= 10000; i++) {

		int temp = i;
		int sum = 0;

		while (temp!=0) {
			int mod = temp % 10;

			sum += mod;
			temp /= 10;
		}

		sum += i;

		v[sum] = true;

	}

	for (int i = 1; i <= 10000; i++) {
		if (!v[i]) cout << i << endl;
	}


	return 0;
}
*/