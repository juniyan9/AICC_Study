// 1.
let total = 0;
var n = parseInt(prompt("수 입력:"))
function onetotal (n){
    for(i = 0; i < n+1; i++){
        if (i%2 == 1){
            total += i
        }
    }    
    return total
} 

console.log(onetotal(n))

// console.log(total) 이게 아님.
// onetotal을 호출해야함. 


console.log("----------")


// 2.
var N = parseInt(prompt("수 입력:"))
function abs (N){
    return Math.abs(N);
}
console.log(abs(N))


console.log("----------")


// 3. 
var k = parseInt(prompt("변환하고 싶은 수 입력(cm):"))
function cmtoinch (k){
    let cm = k/2.54;
    return cm;
}
console.log(`inch 값으로 변환 시 ${cmtoinch(k)}inch입니다.`)


console.log("----------")


// 4.
function byteToBit(val,unit){
    var giga = 1000000000;
    var mega = 1000000;
    var kilo = 1000;
    var result = 0;
    switch(unit){
        case 'G':
        case 'g':
        case 'GB':
        case 'Gb':
            return val*8*giga;
        case 'M':
        case 'm':
        case 'MB':
        case 'mb':
            return val*8*mega;
        case 'K':
        case 'k':
        case 'KB':
        case 'kb':
            return val*8*kilo;
    }
    return console.log(result);
}

var a = parseFloat(prompt('용량 입력:'));
var b = prompt('단위 입력:');
console.log(`bit로 변환 시 ${byteToBit(a,b)}bit입니다.`)


console.log("----------")


// 5. 
var h = parseInt(prompt("키를 입력하세요.(cm):"));
var w = parseInt(prompt("현재 체중을 입력하세요.(kg):"));

var standard = (h - 100)*0.9;
var obesity = (w/standard)*100;

function classification(bmi){
    if(bmi<80){
        console.log("저체중");
    }
    else if(bmi >=80 && bmi < 90){
        console.log("경도저체중");
    }
    else if(bmi >=90 && bmi < 110){
        console.log("정상체중");
    }
    else if(bmi >=110 && bmi < 120){
        console.log("과체중");
    }
    else if(bmi >=120 && bmi < 130){
        console.log("경도비만");
    }
    else if(bmi >=130 && bmi < 150){
        console.log("중등도비만");
    }
    else if(bmi >=150 && bmi < 200){
        console.log("고도비만");
    }
    else if(bmi >= 200){
        console.log("고위험 비만");
    }
}

// 구간을 한꺼번에 적어주면 안 됨. && 사용해서 적어주어야 함! 아니면 >만 사용해서 설정.
// console.log(classification(w)); 이거는 obesity한 게 의미가 없어짐.
console.log(classification(obesity));