#include <cstdlib>
#include <iostream>
using namespace std;
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

//Fibonacci
int fib(int x){
   if((x==1)||(x==0)){
      return(x);
   }
	 else{
      return(fib(x-1)+fib(x-2));
   }
}

int main() {
   int x , i=0;
   cout << "Enter the number of terms of series : ";
   cin >> x;
   cout << "\nFibonnaci Series : ";
   while(i < x) {
      cout << " " << fib(i);
      i++;
   }
   return 0;
}
