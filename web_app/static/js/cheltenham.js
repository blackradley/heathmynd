var isLeftMap = false;
var isRightMap = false;


function initMap() {
// The location of Cheltenham
var cheltenham = {lat: 51.89938, lng: -2.0782};
// The map, centered at Cheltenham
var leftMap = new google.maps.Map(
document.getElementById('left-map'), {zoom: 10, center: cheltenham});
var rightMap = new google.maps.Map(
document.getElementById('right-map'), {zoom: 10, center: cheltenham});
// The marker
var marker = new google.maps.Marker({position: cheltenham, map: leftMap});
var marker = new google.maps.Marker({position: cheltenham, map: rightMap});
google.maps.event.addListener(leftMap, 'bounds_changed', function() {
        if (isLeftMap) {
var center = new google.maps.LatLng(leftMap.getCenter().lat(), leftMap.getCenter().lng());
            var zoom = parseInt(leftMap.getZoom());
            rightMap.setCenter(center);
            rightMap.setZoom(zoom);
}
});
google.maps.event.addListener(leftMap, 'mouseover', function() {
isLeftMap = true;
        isRightMap = false;
});
google.maps.event.addListener(leftMap, 'mouseout', function() {
isLeftMap = false;
isRightMap = false;
});	

/* Data points defined as a mixture of WeightedLocation and LatLng objects */
var heatMapData = [
{location: new google.maps.LatLng(51.8191, -2.0171), weight: 0.5}, 
     new google.maps.LatLng(51.8292, -2.0272),
{location: new google.maps.LatLng(51.8393, -2.0373), weight: 2},
{location: new google.maps.LatLng(51.8493, -2.0474), weight: 3},
{location: new google.maps.LatLng(51.8594, -2.0575), weight: 2},
     new google.maps.LatLng(51.8695, -2.0679),
{location: new google.maps.LatLng(51.8196, -2.0778), weight: 0.5},
{location: new google.maps.LatLng(51.8797, -2.0877), weight: 3},
{location: new google.maps.LatLng(51.8898, -2.0976), weight: 2},
     new google.maps.LatLng(51.8899, -2.0375),
{location: new google.maps.LatLng(51.8890, -2.0474), weight: 0.5},
     new google.maps.LatLng(51.8991, -2.0873),
{location: new google.maps.LatLng(51.8092, -2.0672), weight: 2},
{location: new google.maps.LatLng(51.8093, -2.0671), weight: 3}
];

var heatmap = new google.maps.visualization.HeatmapLayer({
data: heatMapData,
radius: 30
});
heatmap.setMap(leftMap);

/*
fetch('static/data/data.json').then(function(response) {
response.json().then(function(result) {
let locations = result.locations.map((val) => {
  return new google.maps.LatLng(val.latitudeE7 * (10 ** -7), val.longitudeE7 * (10 ** -7));
})
heatmap = new google.maps.visualization.HeatmapLayer({
  data: locations,
  map: map,
  maxIntensity: maxI,
  radius: rad,
  opacity: opac
});
});
});
*/
}
var isLeftMap = false;
var isRightMap = false;




function initMap() {
// The location of Cheltenham
var cheltenham = {lat: 51.89938, lng: -2.0782};
// The map, centered at Cheltenham
var leftMap = new google.maps.Map(
document.getElementById('left-map'), {zoom: 10, center: cheltenham});
var rightMap = new google.maps.Map(
document.getElementById('right-map'), {zoom: 10, center: cheltenham});
// The marker
var marker = new google.maps.Marker({position: cheltenham, map: leftMap});
var marker = new google.maps.Marker({position: cheltenham, map: rightMap});
google.maps.event.addListener(leftMap, 'bounds_changed', function() {
        if (isLeftMap) {
var center = new google.maps.LatLng(leftMap.getCenter().lat(), leftMap.getCenter().lng());
            var zoom = parseInt(leftMap.getZoom());
            rightMap.setCenter(center);
            rightMap.setZoom(zoom);
}
});
google.maps.event.addListener(leftMap, 'mouseover', function() {
isLeftMap = true;
        isRightMap = false;
});
google.maps.event.addListener(leftMap, 'mouseout', function() {
isLeftMap = false;
isRightMap = false;
});	

/* Data points defined as a mixture of WeightedLocation and LatLng objects */
var heatMapData = [
{location: new google.maps.LatLng(51.8191, -2.0171), weight: 0.5}, 
     new google.maps.LatLng(51.8292, -2.0272),
{location: new google.maps.LatLng(51.8393, -2.0373), weight: 2},
{location: new google.maps.LatLng(51.8493, -2.0474), weight: 3},
{location: new google.maps.LatLng(51.8594, -2.0575), weight: 2},
     new google.maps.LatLng(51.8695, -2.0679),
{location: new google.maps.LatLng(51.8196, -2.0778), weight: 0.5},
{location: new google.maps.LatLng(51.8797, -2.0877), weight: 3},
{location: new google.maps.LatLng(51.8898, -2.0976), weight: 2},
     new google.maps.LatLng(51.8899, -2.0375),
{location: new google.maps.LatLng(51.8890, -2.0474), weight: 0.5},
     new google.maps.LatLng(51.8991, -2.0873),
{location: new google.maps.LatLng(51.8092, -2.0672), weight: 2},
{location: new google.maps.LatLng(51.8093, -2.0671), weight: 3}
];

var heatmap = new google.maps.visualization.HeatmapLayer({
data: heatMapData,
radius: 30
});
heatmap.setMap(leftMap);

/*
fetch('static/data/data.json').then(function(response) {
response.json().then(function(result) {
let locations = result.locations.map((val) => {
  return new google.maps.LatLng(val.latitudeE7 * (10 ** -7), val.longitudeE7 * (10 ** -7));
})
heatmap = new google.maps.visualization.HeatmapLayer({
  data: locations,
  map: map,
  maxIntensity: maxI,
  radius: rad,
  opacity: opac
});
});
});
*/
}
