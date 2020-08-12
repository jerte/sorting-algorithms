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
  bool swapped = false;
  int a_size = items.size();
  
  for(int i=0; i<a_size; i++) {    
    swapped = false;
    for(int j=1; j<a_size; j++) {
      if(a[j-1] > a[j]) {
        int temp = a[j-1];
        a[j-1] = a[j];
        a[j] = temp;
	swapped = true;
      } 
    }
    if(!swapped) { break; }
   }

  cout << "Sorted: ";
  for(int i=0; i<a_size; i++) {
    cout << a[i] << " ";
  }
  cout << endl;

  return 0;
}
