window.addEventListener('DOMContentLoaded', function(){
    

    document.getElementsByTagName('input')[0].addEventListener('change', function(){

        const reader = new FileReader();
        console.log(reader.error)
        console.log(reader.readyState)
        
        
        reader.onload = function(e){
            
            const previewImage = document.getElementById('image_preview');
            
            console.log(reader.result)
            console.log('file loaded')
            let imgData = e.target.result
            
            previewImage.src = imgData;
        }
    });
});
