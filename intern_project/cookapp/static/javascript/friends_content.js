window.addEventListener('DOMContentLoaded', function(){
    document.getElementById('action').addEventListener('click', function(){
        document.getElementById('form-document').classList.toggle("active");
        document.getElementById('form-unclicked').classList.toggle('active');
        document.getElementById('form').classList.toggle("active");
        document.getElementById('cross').classList.toggle("active");
        this.classList.toggle("active");
    });
});