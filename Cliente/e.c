#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main (){
	for (int i = 0; i < 999999; i++){
		int result = fork();
		if (result) {
			printf("oi");
			break;
		}
	}
	return 0;
}
