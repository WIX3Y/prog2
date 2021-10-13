#include <cstdlib>
//#include<bits/stdc++.h>
//using namespace std;
// Integer class

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
	private:
		int val;
	};

Integer::Integer(int n){
	val = n;
	}

int Integer::get(){
	return val;
	}

void Integer::set(int n){
	val = n;
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}

// fibonacci
int fib(int n){
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-2);
}

int main ()
{
    int n = 9;
    cout << fib(n);
    getchar();
    return 0;
}

//Fibonacci Series using Recursion
int fib(int n){
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-2);
}

int main ()
{
    int n = 9;
    cout << fib(12);
//    getchar();
    return 0;
