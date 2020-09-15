#include <iostream>
#include <cmath>
using namespace std;

int main()
{   int i = 1;
    while (i == 1){
        float L = 0.8;
        float n = 1;
        float T;
        float mu = 0.0004;
        float f;
        float g = 9.8;
        float m;  
        float v;
        float lambda;      

        //cout << "Enter n: ";
        //cin >> n;
        cout << "Enter m: ";
        cin >> m;
        //cout << "Enter mu: ";
        //cin >> mu;

        lambda = L*2;
        T = g*m;

        f = ((n/(2*L))*(sqrt(T/mu)));
        v = sqrt(T/mu);

        cout << "f: " << f << endl;  
        cout << "v: " << v << endl << endl;

        cout << "Enter 1 to continue, 0 to exit."<<endl;
        cin>>i;
    }
    system("pause");
    
    return 0;
}