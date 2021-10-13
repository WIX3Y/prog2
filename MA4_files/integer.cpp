#include <cstdlib>
#include <iostream>
using namespace std;
// Integer class

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib(val);
	private:
		int val;
	};

Integer::Integer(int n){
	val = n;
	}

int Integer::fib(int val){
	if((val==1)||(val==0)){
		return(val);
		}
	else{
		return(fib(val-1)+fib(val-2));
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
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
