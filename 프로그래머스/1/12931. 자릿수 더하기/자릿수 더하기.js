function solution(n)
{
    let answer = 0;

    n.toString().split('').forEach(num => answer+= parseInt(num));
    
    return answer;
}