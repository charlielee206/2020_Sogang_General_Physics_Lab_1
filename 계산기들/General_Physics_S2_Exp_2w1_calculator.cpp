#include <iostream>
#include <cmath>
using namespace std;

double theory(double, double);
double experimental(double, double, double);

double epsilon = 8.8542 * pow(10,(-12));

int main()
{    
int i = 1;
    while(i) {
    
    double A, d, F, V;

    double exp;
    double thv;

    double error;

    A = 0.008824733613; //r = 53mm
    //A = 0.017671458; //r = 75mm

    //cout << "Enter Area: " << endl;
    //cin >> A;
    cout << "Enter Distance(mm): " << endl;
    cin >> d;
    cout << "Enter Voltage(kv): " << endl;
    cin >> V;
    cout << "Enter Force: " << endl;
    cin >> F;
    
    
    d = d/1000;
    V = V*1000;

    thv = theory(A,d);
    exp = experimental(F,d,V);

    error = ((thv - exp)/thv)*100;

    cout << "Thv: " << thv <<endl;   
    cout << "Exp: " << exp << endl<<endl;
    cout << "Error: " << error << "%" <<endl<<endl;
    cout << "Enter 1 to continue, 0 to exit."<<endl;
    cin>>i;
    }
    
    return 0;
}

double theory(double Area, double dist){
    double Cap = Area* epsilon;
    Cap = Cap/dist;

    Cap = Cap*(pow(10,12));

    return Cap;
}

double experimental(double Force, double dist, double Volt){
    double cap = 2*Force*dist/(pow(Volt,2));
    cap = cap*(pow(10,12));

    return cap;
}