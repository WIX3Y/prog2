#include <cstdlib>
//#include <iostream>
//using namespace std;
// Integer class

class Integer{
	public:
		Integer(int);
		int get();
		int fib();
		void set(int);
	private:
		int val;
		int fib_priv(int);
	};

Integer::Integer(int n){
	val = n;
	}

	int Integer::fib_priv(int value){
		if((value==1)||(value==0)){
			return(value);
			}
		else{
			return(fib_priv(value-1)+fib_priv(value-2));
			}
		}

int Integer::fib(){
	int value = val;
	if((value==1)||(value==0)){
		return(value);
		}
	else{
		return(fib_priv(value-1)+fib_priv(value-2));
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
	int Integer_fib(Integer* integer) {return integer->fib();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
