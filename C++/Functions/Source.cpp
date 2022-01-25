#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int num1, int num2, int num3, int num4) {
    int max = 0;

    if (num1 > num2 && num1 > num3 && num1 > num4) {
        max = num1;
    }
    else if (num2 > num1 && num2 > num3 && num2 > num4) {
        max = num2;
    }
    else if (num3 > num1 && num3 > num2 && num3 > num4) {
        max = num3;
    }
    else {
        max = num4;
    }

    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}