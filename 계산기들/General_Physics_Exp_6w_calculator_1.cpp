#include <iostream>
#include <cmath>
using namespace std;

int main()
{    
    float mg = 0.01624339;
    float r1 = 0.015;
    float r2 = 0.01385;
    float TR = 0.014425;
    float h = 0.00314;
    float rho = 998.4082;
    float g = 9.80;
    float pi = 3.1415926;
    float ans;
    float ans2;
   // mg = mg+ 0.0000021474;
    cout << "Enter mg: " << endl;;

    cin >> mg;
    cout << "Enter r1(outer): " << endl;
    cin >> r1;
    cout << "Enter r2(inner): " << endl;
    cin >> r2;
    cout << "Enter second r: " << endl;
    cin >> TR;
    cout << "Enter h: " << endl;
    cin >> h;
    cout << "Enter rho: " << endl;
    cin >> rho;
    cout << "Enter g(9.8): " << endl;
    cin >> g;
   
    //-------------------

    ans = (mg/(2*pi*(r1 + r2)))-(((r1 - r2)/2)*h*g*rho);

    ans2 = mg/(4*pi*TR);

    cout << "Ans, Formula 1: " << ans << endl;
    cout << endl << "Ans, Formula 2: " << ans2 << endl;   
    system("pause");
    
    return 0;
}
