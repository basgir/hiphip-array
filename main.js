var preferences = new Object();
preferences.single = 0;
preferences.family = 0;
preferences.couple = 0;
preferences.sport = 0;
preferences.nature = 0;
preferences.monuments = 0;
preferences.food = 0;
preferences.cheap = 0;
preferences.normal = 0;
preferences.expensive = 0;

function includePref(pref) {
    if (document.getElementById(pref).className == "selected circle") {
        document.getElementById(pref).className = "circle hvr-grow";
        preferences[pref] = 0;
    } else {
        document.getElementById(pref).className = "selected circle";
        preferences[pref] = 1;
    }
    console.log(pref);
}

function printJson() {
    var offset = -20; //Offset of 20px

    $('html, body').animate({
        scrollTop: $("#journey").offset().top + offset
    }, 1000);
    return $.ajax({
        url: 'http://127.0.0.1:5000/inputs',
        type: 'POST',
        data: JSON.stringify(preferences),
    }).done(handleData);
}
var myLine = [{
    "type": "LineString",
    "coordinates": []
}]

function precisionRound(number, precision) {
    var factor = Math.pow(10, precision);
    return Math.round(number * factor) / factor;
}

function handleData(data /* , textStatus, jqXHR */ ) {

    document.getElementById("price").textContent = "CHF "+ precisionRound(data.price, -1);
    document.getElementById("city1").textContent = data.steps[0].city;
    document.getElementById("city2").textContent = data.steps[1].city;
    document.getElementById("city3").textContent = data.steps[2].city;
    document.getElementById("city4").textContent = data.steps[3].city;

    for(var i  = 0; i<data.steps;i++){
        L.marker([data.steps[i].latitude,data.steps[i].longitude], {icon: selectedIcon}).addTo(mymap);
        myLine[0].coordinates.push([data.steps[i].longitude,data.steps[i].latitude]);
    }
    L.geoJSON(myLine, {
        style: myStyle
    }).addTo(mymap);
    console.log(data.steps[0]);
}