function solution(my_string) {
    let answer = '';
    
    my_string.split('').forEach(str => answer = str + answer)
    return answer;
}