#include <iostream>
#include <cmath>
using namespace std;

int main()
{   int i = 1;
    while (i == 1){
        float L = 0.5;
        float h;
        float T;
        float thvT;
        float pi = 3.1415926;
        float g = 9.8;
        float expg;

        cout << "Enter h: ";
        cin >> h;
        cout << "Enter T: ";
        cin >> T;

        thvT = 2*pi*(sqrt((pow(L,2)+(12*pow(h,2)))/(12*g*h)));

        g = ((pow(L,2)+12*pow(h,2))/pow((thvT/(2*pi)),2))/(12*h);

        expg = ((pow(L,2)+12*pow(h,2))/pow((T/(2*pi)),2))/(12*h);

        cout << "Theoretical T: " << thvT << endl; 
        cout << "Theoretical g: " << g << endl;
        cout << "Exp g: " << expg << endl << endl;  

        cout << "Enter 1 to continue, 0 to exit."<<endl;
        cin>>i;
    }
    system("pause");
    
    return 0;
}