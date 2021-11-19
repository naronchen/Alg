#include <iostream>
using namespace std;

int main(){
    char board[25];

    for (int i = 0; i < 25; ++i) {
    cin >> board[i];
    }
    if (checkboard(board)){ system.out.println("valid");}
    else{ system.out.println("invalid")}
    return 0;
};

boolean checkboard(board){
    for (int i = 0; i < 25; ++i){
        if (board[i]=='k'){
        if ((i%5) <= 2 && i<20 && board[i] == board[i+7]) {return True;}
        if ((i%5)) >= 2 && i<20 && board[i] == board[i+3]) {return True;}
        if ((i%5)) < 4 && i<15 && board[i] == board[i+11]){return True;}
        if ((i%5)>0 && i<15 && board[i] == board[i+9]){return True;}
        }
    }
    return false;
}