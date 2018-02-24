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

function includePref(pref){
    if (document.getElementById(pref).className == "selected circle"){
        document.getElementById(pref).className = "circle hvr-grow";
        preferences[pref] = 0;
    }
    else{
        document.getElementById(pref).className = "selected circle";
        preferences[pref] = 1;
    }
    console.log(pref);
}
function printJson(){
    return $.ajax({
        url: 'http://130.82.239.72:5000/inputs',
        type: 'POST',
        data: JSON.stringify(preferences),
    }).done(handleData);
}

function handleData(data /* , textStatus, jqXHR */ ) {
    console.log(JSON.parse(data));
    //do some stuff
}
