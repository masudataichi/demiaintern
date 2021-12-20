window.addEventListener('DOMContentLoaded', function(){
   
    let input = document.getElementsByClassName('form-hidden')[0];
    console.log(input)

    input.addEventListener('change', function(){
        
        inputFile = input.files[0];
        const reader = new FileReader();
        
        reader.onload = function(e){
            
            const previewImage = document.getElementById('image_preview');
            
            let imgData = e.target.result
            
            previewImage.src = imgData;
        }

        reader.readAsDataURL(inputFile)　//URLとして読み込み
    });
});
