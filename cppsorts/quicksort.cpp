#include<vector>
#include<iostream>
using namespace std;

int partition(int a[], int low, int high) {
	int pivot = a[high];

	int i = low - 1;

	for(int j=low; j<high; j++) {
		if( a[j] < pivot ) {
			i++;
			int temp = a[j];
			a[j] = a[i];
			a[i] = temp;
		}
	}
	
	a[high] = a[i+1];
	a[i+1] = pivot;

	return i+1;
}

void quicksort(int a[], int low, int high) {
  if( high > low ) {
    int i = partition(a, low, high);
	quicksort(a, low, i-1);
	quicksort(a, i+1, high);
  }
}

int main() {
  int v_temp;
  vector<int> items;
  while(cin >> v_temp) {
    items.push_back(v_temp);
  }
  cout << "Original: ";
  for(vector<int>::iterator it=items.begin(); it<items.end(); it++) {
    cout << *it << " ";
  }
  cout << endl;

  int a[items.size()];
  for(int i=0; i<items.size(); i++) {
    a[i] = items[i];
  }

  int a_size = items.size();
  quicksort(a, 0, a_size-1);

  cout << "Sorted: ";
  for(int i=0; i<a_size; i++) {
    cout << a[i] << " ";
  }
  cout << endl;

  return 0;

}
