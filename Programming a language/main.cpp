#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream file("input.txt");
    list<int>ll;
    char in;
    ll.push_front(0);
    while(file.get(in)){
            cout<<in;
        if(in == '.'){
            ll.push_front(ll.front());
        }
        else if(in == '+'){
            ll.front()++;
        }
        else if(in == '-'){
            ll.front()--;
        }
        else if(in == '>'){
            ll.push_front(ll.back());
            ll.pop_back();
        }
        else if(in == '<'){
            ll.push_back(ll.front());
            ll.pop_front();
        }else if(in == '@'){
            auto it = next(ll.begin(), 1);
            int temp = ll.front();
            ll.front() = *it;
            *it = temp;
        }else if( in == '€'){
            break;
        }
    }puts("");
    for(auto it = ll.end(); it!=ll.begin(); it--){
        cout<<(char)*it;
    }
    cout<<(char)ll.front();
    return 0;
}
