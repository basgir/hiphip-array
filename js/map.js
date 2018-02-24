var mymap = L.map('mapid').setView([46.7094552,8.524951], 7);
var myCities = [];
var cities;

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: '<img src="http://live.starthack.ch/wp-content/uploads/2017/03/l1ghtsab3r-partyparrot.gif" alt="" data-ww="["28px","28px","28px","28px"]" data-hh="["20px","20px","20px","20px"]" data-no-retina="" style="width: 15.4194px; height: 11.0138px; transition: none 0s ease 0s; text-align: inherit; line-height: 0px; border-width: 0px; margin: 0px; padding: 0px; letter-spacing: 0px; font-weight: 300; font-size: 7px;" width="320" height="229">["hip","hip"]',
    maxZoom: 18,
    id: 'mapbox.light',
    accessToken: 'pk.eyJ1IjoiYmFzZ2lyIiwiYSI6ImNqZTB1a3d4ODE1ZXMyd21vdTVqajJmbWEifQ.sAmK6VOELXHWdNVlWV7TsQ'
}).addTo(mymap);

var selectedIcon = L.icon({
    iconUrl: './img/logo/selected-icon.png',

    iconSize:     [15, 15], // size of the icon
    shadowSize:   [0, 0], // size of the shadow
    iconAnchor:   [3, 3], // point of the icon which will correspond to marker's location
    shadowAnchor: [0, 0],  // the same for the shadow
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

$.getJSON( "./json/cities.json", function(obj) { 
    cities = obj;
    cities.forEach(element => {
        //myCities.push({'type': 'Point', "coordinates": [element.longitude,element.latitude] });
        L.marker([element.latitude,element.longitude], {icon: selectedIcon}).addTo(mymap);
    });
    myLayer.addData(myCities);
});


var myLayer = L.geoJSON().addTo(mymap);
myLayer.addData(myCities);
