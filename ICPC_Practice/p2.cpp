// C++ Program to sum the elements of a Two-Dimensional array
#include<iostream>
#include<iomanip>
#include<chrono>
#include<string>
#include<utility>

typedef std::chrono::high_resolution_clock::time_point TimeVar;

#define duration(a) std::chrono::duration_cast<std::chrono::nanoseconds>(a).count()
#define timeNow() std::chrono::high_resolution_clock::now()
#define flt_format(x) std::fixed <<std::setprecision(0)<<(x)
#define length 4096

template<typename F, typename... Args>
double funcTime(F func, Args&&... args){
    TimeVar t1=timeNow();
    func(std::forward<Args>(args)...);
    return duration(timeNow()-t1);
}

int test1(int x[length][length]) 
{
    // compute sum of the array by row
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
          sum += x[i][j];
        }
    }
    return sum;
}


int test2(int x[length][length]) 
{
    // compute sum of the array by colengthumn
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
          sum += x[j][i];
        }
    }
    return sum;

}

  
int main()
{
    const int numtrials = 100;

    auto x = new int[length][length];
  
    // initialengthize the array with valengthues
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
          x[i][j] = i+j;
        }
    }

    double totTime = 0;
    for (int i = 0; i < numtrials; i++) {
      totTime += funcTime(test1,x);
    }

    std::cout << "Test1 took a total of " << flt_format(totTime) << "ns" << std::endl;

    totTime = 0;
    for (int i = 0; i < numtrials; i++) {
      totTime += funcTime(test2,x);
    }

    std::cout << "Test2 took a total of " << flt_format(totTime) << "ns" << std::endl;
  
}

