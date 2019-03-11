/*
variables

データ型
  - 文字列
  - 数値
  - True / false
  - オブジェクト
   - 配列
   - 関数
   - 組み込みオブジェクト
  - undifeind
  - null

*/

var msg = "Hello world";
    x = 20;
    y = 10;

console.log(msg);

// 数字
x = x + 20;
x += 5;
console.log(x);

// 文字列
var s;
s = "hello"
s = 'hel\'lo';

console.log(s);

s = "hello" + "world"

console.log(s);

/*
    条件分岐
    if (条件) {
        真
    } else {
        偽
    }

    比較演算子
    > <
    >= <=
    === ==
    !== !=

    論理演算子
    AND &&
    OR ||
    NOT !
    score > 60 && score < 80
*/
var score = 10;
if (score > 60) {
    console.log("ok!");
} else if (score > 40) {
    console.log("soso...");
} else {
    console.log("ng!");
}



/*
       真偽値
           文字列: 空文字以外だったらtrue
           数値: 0 か NaN 以外だったらtrue
           true / false
           object: null 以外だったらtrue
           undefined, null -> false
   */

   if (x) {
       // 処理
   }

   if (x !== '') {
       // 処理
   }

   /*
       三項演算子

       var a, b, c;
       if (条件) {
           a = b;
       } else {
           a = c;
       }
       a = (条件) ? b : c;

   */
   var max, x, y;
   max = (x > y) ? x : y;


   /*
       条件分岐
       switch
   */
   var signal = "blue";

   switch (signal) {
       case "red":
           console.log("stop!");
           break;
       case "green":
       case "blue":
           console.log("go!");
           break;
       case "yellow":
           console.log("slow down!");
           break;
       default:
           console.log("wrong signal");
           break;
   }

/*
 ループ処理

 while
 do ... while

*/

var i = 0;
while ( i < 10 ) {
  console.log(i);
  i++;
}

for (var i = 0; i < 10; i++ ){
    console.log(i);
    break;
}

/*
  break ループ処理を抜ける
  continue ループ処理を一回スキップ
*/

/*
  alert
  confirm
  prompt
*/
//alert("hello");
//var answer = confirm("aru you sure?");
// true が false返ってくる
//console.log(answer)

//var name = prompt("お名前は？", "first");
//console.log(name);

/*
  関数:複数の処理をまとめたもの

  function 関数名() {
    処理
  }
*/

function hello(name) {
    var msg = "hello" + name;
    return msg;
}

var tomgreet = hello("tom");
console.log(tomgreet)

/*
(function() {
    var x = 10,
        y = 20;
    console.log(x + y);
})();


/*
 タイマー処理
  setInterval
  setTimeout
*/

var i = 0;
function show() {
    console.log(i++);
    var tid = setTimeout(function() {
        show()
    }, 1000);
    if (i > 3) {
        clearTimeout(tid);
    }
 }
 show();

/*
    配列: グループ化されたデータ
*/

var score = [100,300,500];
console.log(score[0]);
score[2] = 400;
console.log(score);

var m = [
  [1,2,3],
  [4,5,6]
]

console.log(m[1][1]);

/*
    オブジェクト
        名前と値のペア
*/

var user = {
    email: "sonic883b@gmail.com", // プロパティ: 値
    score: 80,
    greet: function(name){ // メソッド
        console.log("hello, " + name + "from " + this.email);
    }
};

console.log(user["email"]);
console.log(user.email);

user.greet("Tom");

/*
    組み込みオブジェクト
      - String
      - Array
      - Math
      - Date
*/

//var s = new String("sonic883b");　//文字列オブジェクト
var s = "sonic883b"; //文字列リテラル

console.log(s.length);
console.log(s.replace("s","S"));
console.log(s.substr(1,3));

//var a = new Array(100,300,200);
var a = [100,300,200];
console.log(a.length);
// unshift -> array <- push
// shit <- array -> pop
a.push(500);
console.log(a);
a.splice(1,2);
console.log(a);

console.log(Math.PI);
console.log(Math.ceil(5,3));
console.log(Math.floor(5,3));
console.log(Math.round(5,3));
console.log(Math.random());

var d = new Date();
//var d = new Date(2014, 1, 11, 10, 20, 30);
console.log(d.getFullYear());
console.log(d.getMonth());
console.log(d.getTime());


/*
    DOM
*/

console.dir(window);
console.log(window.outerHeight)
//window.location.href = "http://dotinstall.com"

// Document 今開いてるページ
// Document object Model (DOM)

/*
 DOMでの操作
*/

var e = document.getElementById('msg');
e.textContent = 'hello!';
e.style.color = 'red';
e.className = 'myStyle';


/*
    body
        p
            text
*/
/*
var greet = document.createElement('p'),
    text = document.createTextNode('hello world');

document.body.appendChild(greet).appendChild(text);
*/
document.getElementById('add').addEventListener('click', function() {
    var greet = document.createElement('p'),
        text = document.createTextNode('hello world');
    document.body.appendChild(greet).appendChild(text);
});
