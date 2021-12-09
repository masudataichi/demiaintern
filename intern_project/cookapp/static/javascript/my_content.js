//第一次スレッドの表示
window.addEventListener('DOMContentLoaded', function(){
    document.getElementById('form-unclicked').addEventListener('click', function(){
        this.classList.toggle('active');
        document.getElementById('form-document').classList.toggle("active");
        document.getElementById('form').classList.toggle("active");
        document.getElementById('cross').classList.toggle("active");
    });
});
//第二次スレッド
const unclick = document.getElementsByClassName('reply-trigger');
for (var i = 0; i < unclick.length; i++){
    unclick[i].addEventListener('click', function(){
        const doc = this.getElementsByClassName('unclicked-doc');
        for (var i = 0; i < doc.length; i++){
            doc[i].classList.toggle('active');
        }
        const image = this.getElementsByClassName('form-image3');
        for (var i = 0; i < image.length; i++){
            image[i].classList.toggle('active');
        }
        const form = this.nextElementSibling;
            form.classList.toggle('active');

     });
};