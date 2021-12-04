window.addEventListener('DOMContentLoaded', function(){
    document.getElementById('action').addEventListener('click', function(){
        document.getElementById('form-document').classList.toggle("active");
        document.getElementById('form-unclicked').classList.toggle('active');
        document.getElementById('form').classList.toggle("active");
        document.getElementById('cross').classList.toggle("active");
        this.classList.toggle("active");
    });
});
//いいね
var img_src = new Array('/static/media/コンポーネント 14 – 2.svg', '/static/media/コンポーネント 14 – 2 (1).svg');
var i = 0;
function henkou(){
    if(i == 1){
        i = 0;
    }else{
        i++;
    }
    document.getElementById('like-ikon').src = img_src[i];
}
//第二次スレッド
const unclick = document.getElementsByClassName('reply-trigger');
for (var i = 0; i < unclick.length; i++){
    unclick[i].addEventListener('click', function(){
        const doc = document.getElementsByClassName('unclicked-doc');
        for (var i = 0; i < doc.length; i++){
            doc[i].classList.toggle('active');
        }
        const image = document.getElementsByClassName('form-image3');
        for (var i = 0; i < image.length; i++){
            image[i].classList.toggle('active');
        }
        const form = document.getElementsByClassName('replyform');
        for (var i = 0; i < form.length; i++){
            form[i].classList.toggle('active');
        };
     });
};
