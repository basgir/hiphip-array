var preferences = new Object();
    preferences.single = 0;
    preferences.family = 0;
    preferences.couple = 0;
    preferences.sport = 0;
    preferences.nature = 0;
    preferences.monuments = 0;
    preferences.food = 0;

    

function includePref(pref){
    
    console.log(pref);
    
    if (document.getElementById(pref).className == "selected circle"){
        document.getElementById(pref).className = "circle";
        preferences[pref] = 0;
    }
    else{
        document.getElementById(pref).className = "selected circle";
        preferences[pref] = 1;
    }
}
  