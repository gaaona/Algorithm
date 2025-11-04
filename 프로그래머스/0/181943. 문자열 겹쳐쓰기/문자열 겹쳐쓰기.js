function solution(my_string, overwrite_string, s) {
    let answer = '';
    let idx = 0;
    
    while (idx<s){
        answer += my_string[idx];
        idx++;
    }
    
    answer += overwrite_string;
    idx += overwrite_string.length;
    
    const N = my_string.length;
    
    while (idx<N){
        answer += my_string[idx];
        idx++;
    }
    
    return answer;
}