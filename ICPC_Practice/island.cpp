#include <iostream>
#include <vector>
using namespace std;

int main(){

    int x, y;
    cin >> x >> y;
    char pixel;
    vector<bool> table(x*y);
    for (int i = 0; i < x; i++){
        for( int j = 0; j < y; j++){
            cin >> pixel;
            if pixel = "C"{
                cloud_transform(i,x,j,y); // if c is around L, turn into L, otherwise turn into W
                
            }
        }
    }

}