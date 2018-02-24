var mymap = L.map('mapid').setView([47.3694143,8.524951], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.light',
    accessToken: 'pk.eyJ1IjoiYmFzZ2lyIiwiYSI6ImNqZTB1a3d4ODE1ZXMyd21vdTVqajJmbWEifQ.sAmK6VOELXHWdNVlWV7TsQ'
}).addTo(mymap);
var coordinates = [[8.466675,47.3775499], [8.29182679396,47.0562397859], [8.64046745571,46.9155732579]];
var myLines = [{
    "type": "LineString",
    "coordinates": coordinates
}];
var myLayer = L.geoJSON().addTo(mymap);
myLayer.addData(myLines);
