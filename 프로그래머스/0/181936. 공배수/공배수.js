function solution(number, n, m) {
    const isN = number%n?0:1;
    const isM = number%m?0:1;
    
    return +(isN && isM)
}