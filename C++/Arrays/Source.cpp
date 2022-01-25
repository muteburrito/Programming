#include <iostream>
using namespace std;

int main() {

	int n, arr[n], element;

	cin>>n;

	for (int i = 0; i < n; i++) {
		cin >> element;
		arr[i] = element;
	}
	for (int j = n - 1; j >= 0; j--) {
		cout << arr[j] << " ";
	}

	return 0;
}