function productPrice(){
    var productName = document.getElementById("productName").value;

    var price = 0

    switch(productName.toUpperCase()){
        case 'AREPAS':
            price = 0.5
            break;
        case 'EMPANADAS':
            price = 0.3
            break;
        case 'QUESITO':
            price = 0.8
            break;
        default:
            alert("papi no sabe seleccionar?")
            break
    }
document.getElementById("result").value = price




}

