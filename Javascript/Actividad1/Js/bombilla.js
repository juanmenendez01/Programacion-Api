function encenderApagarBombillo(interruptor){
    let pic

    if (interruptor == 0){
        pic = "https://th.bing.com/th/id/OIP.jjCRF8-AvHudtM3gJCR-AgAAAA?rs=1&pid=ImgDetMain"
    } else{
        pic = "https://th.bing.com/th/id/OIP.1WAXuL9UCg8YwtUBn8ArYQHaHa?rs=1&pid=ImgDetMain"
    }

    document.getElementById("bombilla").src = pic
}