#include <string>
#include <iostream>
#include <stack>

// Write a function which returns true if the two specificed finary trees represent the same string, 
// and false otherwise. Note that two different shaped trees could have the same string representation

struct tnode {
	explicit tnode(tnode* left_ = nullptr, tnode* right_ = nullptr, std::string val_ = "") : left(left_), right(right_), val(val_) {}
	tnode* left;
	tnode* right;
	bool visited = false;
	std::string val; 
};

void print_leaf(tnode* tree){
	if (tree == nullptr){
		return;
	}
	if (tree->left == nullptr && tree->right == nullptr) {
		std::cout << tree->val << std::endl; 
		return;
	}
	print_leaf(tree->left);
	print_leaf(tree->right);
}

bool is_leaf(tnode* node) {
	return (node->left == nullptr) && (node->right == nullptr);
}

std::string get_leaf_r(std::stack<tnode*>& trav) {
	tnode* curr_node = trav.top();
	if (is_leaf(curr_node)) { 
		curr_node->visited = true; 
		trav.pop();
		return curr_node->val; 
	}

	std::string leaf_val = "";
	if (curr_node->left) {
		trav.push(curr_node->left);
		leaf_val = get_leaf_r(trav);
	}

	if (curr_node->right) {
		trav.push(curr_node->right);
	}

	return leaf_val; 
}

bool should_visit(tnode* node) {
	if (node == nullptr) {
		return false;
	}
	if (node->visited == true) {
		return false;
	}
	return true; 
}

void get_leaf(std::stack<tnode*>& trav) {
	while (!trav.empty()) {
		tnode* curr_node = trav.top();
		// std::cout << curr_node->val << std::endl; 
		if (is_leaf(curr_node)) { 
			curr_node->visited = true; 
			return; 
		}
		if (should_visit(curr_node->left)) {
			trav.push(curr_node->left); 
		} 
		else if (should_visit(curr_node->right)) {
			trav.push(curr_node->right); 
		} 
		else {
			curr_node->visited = true; 
			trav.pop();
		}
	}
}

void print_leaves(std::stack<tnode*>& trav) {
	while(!trav.empty()) {
		get_leaf(trav);
		if (trav.empty()) {
			return; 
		}
		tnode* leaf = trav.top();
		std::cout << leaf->val << std::endl; 
		trav.pop();
	}
}

int main() {
	tnode* tree1 = new tnode();
	tree1->left = new tnode(new tnode(nullptr, nullptr, "he"), nullptr, "");
	tree1->right = new tnode(new tnode(nullptr, nullptr, "l"), new tnode(nullptr, nullptr, "lo"), "");
	print_leaf(tree1);	

	tnode* tree2 = new tnode(new tnode(nullptr, nullptr, "hel"), new tnode(nullptr, nullptr, "lo"), "");
	print_leaf(tree2);

	tnode* tree3 = new tnode(nullptr, nullptr, "N1");
	tree3->left = new tnode(new tnode(nullptr, nullptr, "N4 - he"), new tnode(nullptr, nullptr, "N5 - l"), "N2");
	tree3->right = new tnode(new tnode(nullptr, nullptr, "N6 - lo"), nullptr, "N3");

	std::stack<tnode*> trav1;
	std::stack<tnode*> trav2;
	std::stack<tnode*> trav3;
	trav1.push(tree1);
	trav2.push(tree2);
	trav3.push(tree3);

	int iters = 0;
	// std::string leaf_val1 = get_leaf(trav1);
	// std::string leaf_val2 = get_leaf(trav2);

	int index1 = 0;
	int index2 = 0;


	// print_leaves(trav3);
}