//inputした画像が表示されるようにしました。
window.addEventListener('DOMContentLoaded', function(){
    document.getElementById('id_image').addEventListener('change',function(e){
        var input = document.getElementById('id_image').files[0];
        console.log(input);
        input.width = 300;
        var reader = new FileReader();
        reader.addEventListener('load', function(e){
            document.getElementById('image-display_update').src = reader.result;
        },true);
        reader.readAsDataURL(input);
    },true);
});
//　”写真を選択”　という文字がinputで消えるようにしました。
window.addEventListener('DOMContentLoaded', function(){
    const doc =document.getElementById('doc');
    document.getElementById('id_image').addEventListener('change',function(e){
        doc.style.display = 'none';
    },false);
});