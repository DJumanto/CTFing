
# Programming a language

My friend is a total "programming languages freak", to the point, that he's decided to make one himself!

The language works like that:

 Language is based on stack (works somewhat like an array)
 Initially stack consists of one element, which value is 0

 "-" decreases stack's last element's value by 1
 
 "+" increases stack's last element's value by 1

 ">" puts first element at the end of the stack and shifts every other down
 
 "<" puts last element at the beginning of the stack and shifts every other up
 
 "@" exchanges last 2 elements
 
 "." duplicates stack's last element and puts it at the end of the stack
 
 "€" prints out every stack's element's value in ASCII (from the first to the

    perintah terdapat pada file "input.txt"
code:

```
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
        }else if( in == '�'){
            break;
        }
    }puts("");
    for(auto it = ll.end(); it!=ll.begin(); it--){
        cout<<(char)*it;
    }
    cout<<(char)ll.front();
    return 0;
}
```
