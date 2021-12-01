
window.addEventListener('DOMContentLoaded', function(){
    document.getElementById('addIcon').addEventListener('click', function(){
    console.log('hello world');
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