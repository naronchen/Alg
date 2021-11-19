#include <iostream>
#include <vector>
using namespace std;

void build(int i, int x, int j, int y, vector<bool> &v){
    v[i * y + j] = false;
    for(int k = -1; k < 2; k++){
        for(int l = -1; l < 2; l++){

            i += k;
            j += l;
            if(i < x && i >= 0 && j < y && j >= 0 && v[i * y + j]){
                build(i, x, j, y, v);
            }
            i -= k;
            j -= l;
        }
    }
}

int main(){

    int x, y;
    cin >> x >> y;
    char pixel;
    vector<bool> table(x * y);
    for(int i = 0; i < x; i++){
        for(int j = 0; j < y; j++){
            cin >> pixel;
            if (pixel == '#'){
            table[i * y + j] = true;
            }
        }
    }
    int Count = 0;
    for(int i = 0; i < x; i++){
        for(int j = 0; j < y; j++){
            if(table[i * y + j]){
                Count++;
                build(i, x, j, y, table);
            }
        }
    }
    cout << Count << endl;
    
    return 0;   
}