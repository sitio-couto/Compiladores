int checkPrime(int n) {
    int i, isPrime = 1;
    for (i = 2; i <= n/2; ++i) {
        if (n % i == 0) {
            isPrime = 0;
            break;
        }
    }
    return isPrime;
}

int main(){
	assert checkPrime(6299) == 1;
	return 0;
}
