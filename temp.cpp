#include <iostream>
using namespace std;
int main()
{
	long long int t, n;
	cin >> t;
	while (t--)
	{
		cin >> n;
		for (long long int i = 1; i <= (n / 2); i++)
		{
			// cout << "bc" << i << endl;
			long long int temp = i * i + 1;
			if (temp / 2 > n)
			{
				cout << i - 1 << endl;
				break;
			}
		}
	}
	return 0;
}