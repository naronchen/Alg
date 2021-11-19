#include <iostream>
using namespace std;

bool checkboard(char board[]){
    for (int i = 0; i < 25; ++i){
        if (board[i]=='k'){
        if ((i%5) <= 2 && i<20 && board[i] == board[i+7]) {return true;}
        if ((i%5) >= 2 && i<20 && board[i] == board[i+3]) {return true;}
        if ((i%5) < 4 && i<15 && board[i] == board[i+11]){return true;}
        if ((i%5) > 0 && i<15 && board[i] == board[i+9]){return true;}
        }
    }
    return false;
}

int main(){
    char board[25];
    for (int i = 0; i < 25; ++i) {cin >> board[i];}
    int count=0;
    for (int i = 0; i < 25; ++i) {if (board[i]=='k'){count+=1;}}
    if (count==9 && checkboard(board) == false){ cout << "valid";}
    else{ cout << "invalid";}
    return 0;
};

