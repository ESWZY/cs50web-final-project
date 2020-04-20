function handleChange(input) {
    var x = document.getElementById("query").value;
    if (x < 0 || x === "") {
        alert("Invalid input!");
        return false;
    }
    return true;
}