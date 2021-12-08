//tab切り替え
function clickSwich() {
  "use strict";
  var isObject = 0; 
  var btnAll = document.getElementById("all");
  var btnLike = document.getElementById("like");
  var resultAll = document.getElementById("content-all");
  var resultLike = document.getElementById("content-like");
  var btnImgAll_1 = document.getElementById("all-img1");
  var btnImgAll_2 = document.getElementById("all-img2");
  var btnback1 = document.getElementById("background1");
  var btnImgLike_1 = document.getElementById("like-img1");
  var btnImgLike_2 = document.getElementById("like-img2");
  var btnback2 = document.getElementById("background2");

  function setState(isA) {
    btnAll.className = isObject == 0 ? "btn-inactive" : "btn";
    resultAll.className = isObject == 0 ? "boxDisplay" : "boxNone";
    btnImgAll_1.className = isObject == 0 ? "imgNone":"imgDisplay";
    btnImgAll_2.className = isObject == 0 ? "imgDisplay":"imgNone";
    btnback1.className = isObject == 0 ? "imgDisplay":"imgNone";
    btnLike.className = isObject == 1 ? "btn-inactive" : "btn";
    resultLike.className = isObject == 1 ? "boxDisplay" : "boxNone";
    btnImgLike_1.className = isObject == 1 ? "imgNone":"imgDisplay";
    btnImgLike_2.className = isObject == 1 ? "imgDisplay":"imgNone";
    btnback2.className = isObject == 1 ? "imgDisplay":"imgNone";
  }
  setState(0);

  btnAll.addEventListener("click", function () {
    if (isObject == 0) return;
    isObject = 0;
    setState(0);
  });
  btnLike.addEventListener("click", function () {
    if (isObject == 1) return;
    isObject = 1;
    setState(1);
  });
}
document.addEventListener("DOMContentLoaded", clickSwich, false);


// 左から順にタブボタンの要素を取得
const button1 = document.getElementById('button1')
const button2 = document.getElementById('button2')
const button3 = document.getElementById('button3')
const button4 = document.getElementById('button4')


let current_url = location.pathname.split('/').pop()
console.log(current_url)

window.addEventListener('DOMContentLoaded', function(){
    if(current_url === 'home' ){
        
        button1.src = '../static/svg/home_orange.svg'
        button2.src = '../static/svg/friends.svg'
        button3.src = '../static/svg/submission.svg'
        button4.src = '../static/svg/friend_add_before.svg'
        
    } else if(current_url === 'friends' ){
        
        button1.src = '../static/svg/home.svg'
        button2.src = '../static/svg/friends_orange.svg'
        button3.src = '../static/svg/submission.svg'
        button4.src = '../static/svg/friend_add_before.svg'

    } else if(current_url === 'submission' ){

        button1.src = '../static/svg/home.svg'
        button2.src = '../static/svg/friends.svg'
        button3.src = '../static/svg/submission_orange.svg'
        button4.src = '../static/svg/friend_add_before.svg'

    } else if(current_url === 'friends_add_before') {

        button1.src = '../static/svg/home.svg'
        button2.src = '../static/svg/friends.svg'
        button3.src = '../static/svg/submission.svg'
        button4.src = '../static/svg/friend_add_before_orange.svg'

    }
});


