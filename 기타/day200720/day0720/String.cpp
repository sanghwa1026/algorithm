#include <iostream>
#include <string>
#include <vector>

using namespace std;

/* 1316 �׷� �ܾ� üĿ */
int main() {

	int N;

	cin >> N;

	//���� ���� ��..? 

	
	
	int cnt = 0;
	string s;
	for (int n = 0; n < N; n++) {
		cin >> s;
		vector<int> az(26, 0);


		if (s.size() >= 1) {

			char pre = s.at(0);
			az[pre - 'a'] = 1;

			for (int i = 1; i < s.size(); i++) {
				int cur = s.at(i);

				if (cur != pre) az[cur - 'a']++;


				pre = s.at(i);
			}
		}
		else {
			cnt += 0;
		}

		bool flag = true;
		for (int i = 0; i < az.size(); i++) {
			if (az[i] >= 2) flag = false;

			//cout << az[i] << " ";
		}

		if (flag) cnt++;
	}
	
	//cout << endl;

	cout << cnt;


	return 0;
}


/* 2941 ũ�ξ�Ƽ�� ���ĺ� */

/*
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

	string s;

	cin >> s;

	vector<string> croa;

	croa.push_back("c=");
	croa.push_back("c-");
	croa.push_back("dz=");
	croa.push_back("d-");
	croa.push_back("lj");
	croa.push_back("nj");
	croa.push_back("s=");
	croa.push_back("z=");

	//sub string
	//1. ���� �� cnt++, + ���� ���ڿ� ����
	//2.
	//ljes=njak
	int cnt = 0;

	if (s.size() > 1) {
		for (int i = 0; i < croa.size(); i++) {

			for (int j = 0; j < s.size() - (croa[i].size() - 1); j++) {
				//cout << croa[i].compare(s.substr(j, croa[i].size())) << endl;
				if (croa[i].compare(s.substr(j, croa[i].size())) == 0) {
					cnt++;
				}

			}
		}
	}


	cout << s.size() - cnt;

	return 0;
}


*/