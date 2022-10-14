#include <iostream>
using namespace std;
int main()
{
    int n, i, store,s,k;
    cin >> n;
    int a[n], b[n],c[n];
    for (i = 0; i < n; i++)
    {
        cin >> a[i] >> b[i] >> c[i];
    }
    for(i=0; i<n; i++){
        s = (b[i]-a[i]);
        k = (c[i] - b[i]);
        if((b[i]-a[i])<0){
            s = (b[i]-a[i])*(-1);
        }
        if((c[i] - b[i])<0){
            k = (c[i] - b[i])*(-1);
        }
        {
            if(s > k){
            cout << k << "\n";}
            else
            cout << s << "\n";
        }
    }
        
    return 0;
}
