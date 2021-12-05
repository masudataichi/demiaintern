function clickSwich() {
  "use strict";
  var isObject = 0; //現在地判定
  var btnAll = document.getElementById("all");
  var btnLike = document.getElementById("like");
  var resultAll = document.getElementById("content-all");
  var resultLike = document.getElementById("content-like");
  function setState(isA) {
    btnAll.className = isObject == 0 ? "btn-inactive" : "btn";
    resultAll.className = isObject == 0 ? "boxDisplay" : "boxNone";
    btnLike.className = isObject == 1 ? "btn-inactive" : "btn";
    resultLike.className = isObject == 1 ? "boxDisplay" : "boxNone";
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

