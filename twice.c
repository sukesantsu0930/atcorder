#include<stdio.h>
#include<stdloib.h>

int main(){
    char i[4];

    prinntf("a");

    fgets(input,sizeof(input),stdin);

    for(int i=0;i<sizeof(input);i++){
        if(islower(input[i])){
            printf("error");
            return 0;
        }
    }

    int num=atoi(input);

    num*=2;

    printf("%d",num);

    return 1;
}