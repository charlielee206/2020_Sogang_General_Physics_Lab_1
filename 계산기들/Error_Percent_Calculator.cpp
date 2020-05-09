#include <iostream>
#include <cmath>
using namespace std;

int main()
{    
int i = 1;
    while(i) {
    float thv;
    float exp;
    float ans;

    cout << "Enter Theoretical Value: " << endl;
    cin >> thv;
    cout << "Enter Experemental Value: " << endl;
    cin >> exp;
    
    ans = ((thv - exp)/thv)*100;

    cout << "Error: " << abs(ans) << "%" <<endl<<endl;   
    cout << "Enter 1 to continue, 0 to exit."<<endl;
    cin>>i;
    }
    
    return 0;
}