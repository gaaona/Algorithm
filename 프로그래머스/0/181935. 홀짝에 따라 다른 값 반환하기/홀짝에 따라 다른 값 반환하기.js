function solution(n) {
    let answer = 0;
    const remain = n % 2;
    let i = remain;
    while (i <= n){
        answer += (i ** (2 - 1 * remain));
        i += 2;
    } 
    return answer;
}