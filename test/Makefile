gtestlib=-lgtest -lgmock -lgtest_main
pthread=-lpthread

all:string_alg_test.exe tadcc_version.exe

string_alg_test.exe:string_alg.test.cc 
	g++ -o $@ $< -I../tadcc/ $(gtestlib) $(pthread)
	
tadcc_version.exe:tadcc_version.test.cc 
	g++ -o $@ $< -I../tadcc/ $(gtestlib) $(pthread)

test:string_alg_test.exe tadcc_version.exe
	./string_alg_test.exe
	./tadcc_version.exe

clean:
	rm *.exe 
