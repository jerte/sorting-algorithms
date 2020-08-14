#include<vector>
#include<iostream>
using namespace std;

void merge(int a[], int left, int mid, int right) {
  int i=left;
  int left_i = 0;
  int right_i = 0;

  int left_[mid-left]; 
  int right_[right-mid];

 
  for(int j=left; j<mid+1; j++) {
    left_[left_i] = a[j];
    left_i++;
  }
  for(int j=mid+1; j<right+1; j++) {
    right_[right_i] = a[j];
    right_i++;
  }
  
  left_i = 0;
  right_i = 0;
  while( left_i < mid-left && right_i < right-mid) {
    if( left_[left_i] < right_[right_i] ) {
      a[i] = left_[left_i];
      left_i++;
    } else {
      a[i] = right_[right_i];
      right_i++;
    }
    i++;
  }
  while( left_i < mid-left ) {
    a[i] = left_[left_i];
    left_i++;
    i++;
  }
  while( right_i < right-mid ) {
    a[i] = right_[right_i];
    right_i++;
    i++;
  }
}

void merge_sort(int a[], int left, int right) {
  if(right>left) {
    int mid = (int) ((right+left)/2);
    merge_sort(a, left, mid);
    merge_sort(a, mid+1, right);
    merge(a, left, mid, right);
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

  merge_sort(a, 0, a_size-1);
  
  cout << "Sorted: ";
  for(int i=0; i<a_size; i++) {
    cout << a[i] << " ";
  }
  cout << endl;

  return 0;
}
