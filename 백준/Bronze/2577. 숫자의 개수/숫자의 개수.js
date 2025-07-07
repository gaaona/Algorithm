const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const inputs = [];
const idx = Array(10).fill(0);

rl.on('line', (line) => {
  inputs.push(Number(line)); // 입력받은 값을 숫자로 변환하여 저장
  
  if (inputs.length === 3) { // 3개 입력이 들어오면
    let cnt = 1;
    for (let i = 0; i < 3; i++){
      cnt *= inputs[i];
    }
    
    const ans = cnt.toString();
    for (let j = 0; j < ans.length; j++) {
      idx[Number(ans[j])] += 1;
    }
    
    for (let k = 0; k<10; k++){
      console.log(idx[k])
    };

    
    rl.close();
  }
});