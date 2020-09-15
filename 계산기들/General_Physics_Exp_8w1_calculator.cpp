#include <iostream>
#include <cmath>
using namespace std;

int main()
{    
int i = 1;
    while(i) {
    float r = 0.01435;
    float m = 116.6;
    float weight;
    float t;
    float ans;
    float aa = 53.07111;


    //cout << "Enter Radius of disk: " << endl;
    //cin >> r;
    //cout << "Enter aa: " << endl;
    //cin >> aa;
    cout << "Enter Mass of weights: " << endl;
    cin >> weight;
    cout << "Enter Time: " << endl;
    cin >> t;

    ans = weight*(pow(r,2))*(((9.8*(pow(t,2)))/(2*0.7))-1);


    cout << "Ans: " << abs(ans) <<endl<<endl;
    cout << "Enter 1 to continue, 0 to exit."<<endl;
    cin>>i;
    }
    
    return 0;
}