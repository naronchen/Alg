#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int sequenceCheck(int array[], int amountNum) {
  int arithPass = amountNum - 2;
  
  for(int j = 0; j < amountNum - 2; j++) {
    if(array[j+1] - array[j] == array[j+2] - array[j+1]) {
      arithPass--;
    }
  }
  
  return arithPass;
}


void sortArray(int myInts[], int arrayLength) {
  vector<int> myvector (myInts, myInts+arrayLength);
  int index = 0;
  

  sort (myvector.begin(), myvector.begin()+arrayLength);

  for (vector<int>::iterator it=myvector.begin(); it!=myvector.end(); ++it)
    myInts[index++] = *it;
  
}


int main() {
  
  int numSequences, amountNum, number;
  int counter = 0;
  
  cin >> numSequences;
  
  while(counter != numSequences) {
    cin >> amountNum;
    
    int array[amountNum] = {};
    int arithPass;
    bool failArith = false;
    
    
    for(int i = 0; i < amountNum; i++) {
      cin >> number;
      array[i] += number;
    }
    
    arithPass = sequenceCheck(array,amountNum);
    
    if(arithPass == 0) {
      cout << "arithmetic" << endl;
      failArith = true;
      counter++;
      continue;
    }
    
    sortArray(array, amountNum);
    
    arithPass = sequenceCheck(array,amountNum);
    
    if(arithPass == 0) {
      cout << "permuted arithmetic" << endl;
      failArith = true;
      counter++;
      continue;
    }
    
    if (failArith == false) {
      cout << "non-arithmetic" << endl;
      counter++;
      continue;
    }
    
  }
  
  return 0;
}