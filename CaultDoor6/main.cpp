#include <iostream>

using namespace std;

int main()
{
    FILE* flag_to_rev = fopen("rev_this.txt","r");
    char out[24];
    char dump;
    for(int i=0;i<8;i++){
        out[i] = fgetc(flag_to_rev);
    }
    for(int i=8;i<23;i++){
        if((i&1)==0){
            dump = fgetc(flag_to_rev)-5;
        }
        else{
            dump = fgetc(flag_to_rev)+2;
        }
        out[i] = dump;
    }
    dump = fgetc(flag_to_rev);
    out[22] = dump;
    cout<<out<<endl;
    fclose(flag_to_rev);
    return 0;
}
