//第一次スレッドの表示
window.addEventListener('DOMContentLoaded', function(){
    document.getElementById('action').addEventListener('click', function(){
        document.getElementById('form-document').classList.toggle("active");
        document.getElementById('form-unclicked').classList.toggle('active');
        document.getElementById('form').classList.toggle("active");
        document.getElementById('cross').classList.toggle("active");
        this.classList.toggle("active");
    });
});
//第二次スレッドの表示
window.addEventListener('DOMContentLoaded', function(){
    document.getElementById('unclicked').addEventListener('click', function(){
        document.getElementById('doc').classList.toggle('active');
        document.getElementById('img').classList.toggle('active');
        document.getElementById('clicked').classList.toggle('active');
    });
});

let under = document.getElementById('under')
let over = document.getElementById('over')

document.addEventListener('DOMContentLoaded', function(){

    console.log(under)
    console.log(over)
    console.log(document.getElementById('delete'))

    document.getElementById('delete').addEventListener('click', function() {
        
        console.log('成功')
        under.classList.toggle('under')
        over.classList.toggle('over')
        
    }); 
});