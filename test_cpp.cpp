#include <string> 
#include <iostream>
#include <vector>
int main(int argc, char* argv[]) {
	int n = std::stoi(argv[1]);
	std::vector<int> v(n, 0);
//	std::cout << v.at(n) << std::endl; 
	float x = 5.0; 
	int y = 2;
	std::cout << x / y << std::endl;
}
