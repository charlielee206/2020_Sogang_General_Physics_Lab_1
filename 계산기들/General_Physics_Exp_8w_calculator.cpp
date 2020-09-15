#include <iostream>
#include <cmath>
using namespace std;

int main()
{    
int i = 1;
    while(i) {
        int mode = 0;
        cout << "1: disk, 2: ring" << endl;
        cin >> mode;


        if(mode == 1){
            float r = 0;
            float m = 0;
            float ans;

            cout << "Enter Radius: " << endl;
            cin >> r;
            cout << "Enter Mass: " << endl;
            cin >> m;

            ans = (0.5)*m*(pow(r,2));

            cout << "ans: " << ans << endl;  

        }
        else{
            float r = 0;
            float rin = 0;
            float m = 0;
            float ans;

            cout << "Enter Inner Radius: " << endl;
            cin >> rin;
            cout << "Enter Outer Radius: " << endl;
            cin >> r;
            cout << "Enter Mass: " << endl;
            cin >> m;

            ans = (0.5)*m*(pow(r,2)+pow(rin,2));

            cout << "ans: " << ans << endl; 
        }

    cout << "Enter 1 to continue, 0 to exit."<<endl;
    cin>>i;
    }
    
    return 0;
}