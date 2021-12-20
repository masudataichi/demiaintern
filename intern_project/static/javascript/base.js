
// 左から順にタブボタンの要素を取得
const button1 = document.getElementById('button1')
const button2 = document.getElementById('button2')
const button3 = document.getElementById('button3')
const button4 = document.getElementById('button4')


let current_url = location.pathname.split('/').pop();
let current_url_special = location.pathname.split('/').reverse()[1];


window.addEventListener('DOMContentLoaded', function(){

    console.log(current_url)
    console.log(current_url_special)

        if(current_url == 'home'){
            
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
    