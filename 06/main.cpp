#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    
    unsigned int squares = 0;
    for (int i = 1; i <=100; i++)
    {
        squares += (i * i);    
    }
    
    unsigned int sums = 0;
    for (int j = 1; j <=100; j++)
    {
        sums += j;    
    }
    sums *= sums;
    
    cout << (sums - squares) << endl;
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
