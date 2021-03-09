cc=g++
gtestlib=-lgtest -lgmock -lgtest_main
pthread=-lpthread
inc=../include/

all:string_alg_test.exe tadcc_version.exe

string_alg_test.exe:string_alg.test.cc 
	g++ -o $@ $< -I$(inc) $(gtestlib) $(pthread) -std=c++14
	
tadcc_version.exe:tadcc_version.test.cc 
	g++ -o $@ $< -I$(inc) $(gtestlib) $(pthread) -std=c++14

tadcc_thread_pool_example.exe:tadcc_thread_pool.test.cc 
	$(cc) -o $@ $< -I$(inc) $(pthread) -std=c++14

test:string_alg_test.exe tadcc_version.exe
	./string_alg_test.exe
	./tadcc_version.exe

clean:
	rm *.exe 
