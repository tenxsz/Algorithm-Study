N = int(input())
ans = [0 for x in range(N+1)]
ans[1] = 1

if N>1:
    ans[2] = 2

for i in range(3, N+1):
    ans[i] = (ans[i-2]+ans[i-1])%15746

print(ans[N])



1

00 11

100 001 111

0011 0000 1001 1100 1111

00111 10011 11001 11100
10000 00100 00001 11111

첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.