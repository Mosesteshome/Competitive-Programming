#include <iostream>

using namespace std;
int piling(int x,int y)
 {return(x*y)/2;}
int main()
{
    int x,y;
    cin>>x>>y;
    cout<<piling(x,y);

    return 0;
}
