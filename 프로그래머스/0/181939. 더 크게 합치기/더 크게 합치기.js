function solution(a, b) {
    let answer = 0;
    const ab = ''+a+b;
    const ba = '' + b + a;
    if (ab < ba){
        return parseInt(ba)
    } else {
        return parseInt(ab)
    }
}