var d=new Date();
var ngay=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
var thang=["1","2","3","4","5","6","7","8","9","10","11","12"];
var greeting;
var time = new Date().getHours();
if (time < 8) {
    greeting = "good morning! ";
} else if (time < 19) {
    greeting = "Wish you have a peaceful and happy day!";
} else if(time <23) {
    greeting = "good evening fun!";
}
else{
    greeting="good night! ";
}
document.getElementById("date").innerHTML= d.getHours()+":"+d.getMinutes()+":"+d.getSeconds()+ "   "+ greeting + " "  + ngay[d.getDay()] + " day " + d.getDate()
    + " month " + thang[d.getMonth()] + " year " + d.getFullYear();