#include<stdio.h>

int main() {
	//int result = 1;
	//int sum = 0;
	//int j;
	////printf("enter a number(n < 10):");
	////scanf("%d", &n);
	//for (int j = 1; j <= 3; j++) {
	//		result = result * j;
	//		sum += result;
	//	}
	
	/*printf("%d", result);*/
	/*printf("The sum of the factorial is %d", sum);*/

	int arr[] = {1, 3, 4, 5, 7, 8, 10, 12, 14, 15};
	int high = sizeof(arr)/sizeof(arr[0]);
	srand(time(NULL));
	int low = 0;
	int num = rand() % 15 + 1;
	//printf("enter a number, we will search for you: ");
	//scanf("%d", &num);
	int step = 0;;
	while (low <= high) {
		int mid = (high + low) / 2;
		if (num > arr[mid]) {
			low = mid + 1;
			step++;

		}
		else if (num < arr[mid])
		{
			high = mid-1;
			step += 1;
		}
		else
			printf("we found the number\n");
			step++;
			printf("%d", step);	
			return 0;

	}
	
	printf("We did not find such number");
	return 0;

		
}
