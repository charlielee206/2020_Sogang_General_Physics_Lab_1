#include <iostream>
#include <cmath>
using namespace std;

int main()
{    
    float num;
    float mass = 0.1972;
    float pi = 3.1415926;
    float ans;

    cout << "Enter Seconds: ";
    cin >> num;
    ans = (4*(pow(pi,2))*mass)/(pow(num,2));

    cout << "Ans: " << ans << endl;   
    system("pause");
    
    return 0;
}