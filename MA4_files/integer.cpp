#include <cstdlib>
#include <iostream>
using namespace std;
// Integer class

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib(int val);
	private:
		int val;
	};

Integer::Integer(int n){
	val = n;
	}

int Integer::fib(int value){
	if((value==1)||(value==0)){
		return(value);
		}
	else{
		return(fib(value-1)+fib(value-2));
		}
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
	int Integer_fib(Integer* integer) {return integer->fib(get());}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
