function handleChange(input) {
    var x = document.getElementById("query").value;
    if (x < 0 || x === "") {
        alert("Invalid input!");
        return false;
    }
    return true;
}

function handleChange2(input) {
    var x = document.getElementById("cc").value;
    if (x < 0 || x === "") {
        alert("Invalid cc input!");
        return false;
    }
    var x = document.getElementById("money").value;
    if (x < 0 || x === "") {
        alert("Invalid money input!");
        return false;
    }
    return true;
}

$(":input").inputmask();

$("#phone").inputmask({"mask": "(999) 999-9999"});