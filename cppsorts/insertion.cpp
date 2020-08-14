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

  for(int i=1; i<a_size; i++) {
    int j=i-1;
    while( a[j] < a[i] && j>=0 ) {
      j--;
    }
    if( i!=j ) {
      int temp = a[i];
      a[i] = a[j];
      a[j] = temp;
    }
  }

  cout << "Sorted: ";
  for(int i=0; i<a_size; i++) {
    cout << a[i] << " ";
  }
  cout << endl;

  return 0;
}
