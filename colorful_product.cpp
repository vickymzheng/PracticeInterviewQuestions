#include <string>
#include <iostream>
#include <set>
#include <vector>

void print_set(const std::set<int>& to_print) {
	for (const int x : to_print) {
		std::cout << x << " ";
	}
	std::cout << std::endl; 
}

void get_power_set(const std::set<int>& super_set, std::set<std::set<int>>& power_set) {
	int num_digits = super_set.size();
	if (num_digits == 1) {
		power_set.insert(super_set);
		return;
	} 
	for (int x : super_set) {
		std::set<int> subset = super_set; 
		subset.erase(x);
		get_power_set(subset, power_set);
		power_set.insert(subset);
	}
}

bool is_colorful(int num) {
	std::set<int> super_set; 
	std::vector<int> digits;
	while (num > 0) {
		int digit = num % 10;
		num = num / 10;
		if (super_set.find(digit) != super_set.end()) {
			return false;
		}
		super_set.insert(digit); 
		digits.push_back(digit);
	}

	std::set<std::set<int>> power_set;
	get_power_set(super_set, power_set);
	std::set<int> products;
	// for (const std::set<int>& subset : power_set) {
	// 	print_set(subset);
	// }
	for (const std::set<int>& subset : power_set) {
		int product = 1; 
		for (int x : subset) {
			product = product * x;
		}
		if (products.find(product) != products.end()) {
			return false;
		}
		products.insert(product);
	}
	return true; 
}

int main() {
	int test;
	while(std::cin >> test) {
		if(is_colorful(test)) {
			std::cout << "Colorful" << std::endl;
		}
		else {
			std::cout << "Not Colorful" << std::endl;
		}
	}
}