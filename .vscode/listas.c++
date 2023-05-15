#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
	list<int> demoList;
    
    demoList.push_back(5);
    demoList.push_back(6);
    demoList.push_back(7);
    
    if (demoList.empty())
       cout<<"Lista vacia\n";
    else
       cout<<"no vacia\n";
    return 0;
}