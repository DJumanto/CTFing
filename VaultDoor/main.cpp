#include <iostream>
#include <string>

using namespace std;

int main()
{
    string buffer = "jU5t_a_sna_3lpm18gb41_u_4_mfr340";
    char password[32];
    int i;
    for (i=0; i<8;i++){
        password[i] = buffer[i];
    }
    for (i=8;i<16;i++){
        password[23-i] = buffer[i];
    }
    for (i=16;i<32;i+=2){
        password[46-i] = buffer[i];
    }
    for (i=31;i>=17;i-=2){
        password[i] = buffer[i];
    }
    cout<<password<<endl;
    return 0;
}
