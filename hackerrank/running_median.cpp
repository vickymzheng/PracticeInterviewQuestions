// Heaps: Find the Running Median

#include <queue>
#include <vector>
#include <iostream>
#include <stdlib.h> 

using namespace std; 

class median_heap {
public:
	float get_median() {
		int size_diff = pq_size_diff();
		float median = _median; 
		if (size_diff == 1) {
			int min_heap_size = _minHeap.size();
			int max_heap_size = _maxHeap.size();
			if (min_heap_size < max_heap_size) {
				median = (_maxHeap.top() + _median) / 2.0;
			}
			else {
				median = (_minHeap.top() + _median) / 2.0;
			}
		}
		return median;
	}

	void add(int to_add) {
		if (_size == 0) {
			_median = to_add;

		}
		else {
			if (to_add > _median) {
				_minHeap.push(to_add);
			}
			else {
				_maxHeap.push(to_add);
			}
			rebalance();
		}
		++_size;
	};
private: 
	int pq_size_diff() {
		int min_heap_size = _minHeap.size();
		int max_heap_size = _maxHeap.size();
		int size_diff = abs(min_heap_size - max_heap_size); 
		return size_diff;
	}

	void rebalance(){
		int size_diff = pq_size_diff();
		if (size_diff > 1) {
			int min_heap_size = _minHeap.size();
			int max_heap_size = _maxHeap.size();
			if (min_heap_size < max_heap_size) {
				_minHeap.push(_median);
				_median = _maxHeap.top();
				_maxHeap.pop();
			}
			else {
				_maxHeap.push(_median);
				_median = _minHeap.top();
				_minHeap.pop();
			}
		}
	}

	int _median; 
	priority_queue<int, vector<int>, std::greater<int> > _minHeap;
	priority_queue<int> _maxHeap;
	int _size = 0;
};

int main(){
    int n;
    cin >> n;
    median_heap mp; 
    
    for(int a_i = 0; a_i < n;++a_i){
        int to_add; 
        cin >> to_add; 
        mp.add(to_add);
        cout << mp.get_median() << endl; 
    }
    return 0;
}