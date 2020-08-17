#include<vector>
#include<iostream>
using namespace std;

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
  
  
  for(int i=0; i<a_size; i++) { 
  	int min_i = i;
    for(int j=i; j<a_size; j++) {
      if(a[j] < a[min_i]) {
      	min_i = j;
	  } 
    }

	if(min_i != i) {
		int temp = a[min_i];
		a[min_i] = a[i];
		a[i] = temp;
	}
   }

  cout << "Sorted: ";
  for(int i=0; i<a_size; i++) {
    cout << a[i] << " ";
  }
  cout << endl;

  return 0;
}
