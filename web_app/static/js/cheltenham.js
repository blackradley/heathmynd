var isLeftMap = false;
var isRightMap = false;

/**
 * Tie two Google Maps together so they're behaviour mirrors each other.
 * 
 * The lead map is held in a property set on the maps so it is available 
 * for any function to use.  Formerly it was set on two global variables,
 * it just seemed neater to get it on the map objects themselves.
 * 
 * @param {Object} thisMap - this Google map 
 * @param {Object} thatMap - that Google map 
 */
function mirrorMaps(thisMap, thatMap) {
    thisMap.isTheLeader = false;
    thatMap.isTheLeader = false;
    // When this map changes make that map follow
    google.maps.event.addListener(thisMap, 'bounds_changed', function() {
        if (thisMap.isTheLeader) {
            var center = new google.maps.LatLng(thisMap.getCenter().lat(), thisMap.getCenter().lng());
            var zoom = parseInt(thisMap.getZoom());
            thatMap.setCenter(center);
            thatMap.setZoom(zoom);
        }
    });
    // If the mouse is on this map then it is the leader
    google.maps.event.addListener(thisMap, 'mouseover', function() {
        thisMap.isTheLeader = true; thatMap.isTheLeader = false;
    });
    google.maps.event.addListener(thisMap, 'mouseout', function() {
        thisMap.isTheLeader = false; thatMap.isTheLeader = false;
    });
    // When that map changes make this map follow
    google.maps.event.addListener(thatMap, 'bounds_changed', function() {
        if (thatMap.isTheLeader) {
            var center = new google.maps.LatLng(thatMap.getCenter().lat(), thatMap.getCenter().lng());
            var zoom = parseInt(thatMap.getZoom());
            thisMap.setCenter(center);
            thisMap.setZoom(zoom);
        }
    });
    // If the mouse is on that map then it is the leader
    google.maps.event.addListener(thatMap, 'mouseover', function() {
        thisMap.isTheLeader = false; thatMap.isTheLeader = true;
    });
    google.maps.event.addListener(thatMap, 'mouseout', function() {
        thisMap.isTheLeader = false; thatMap.isTheLeader = false;
    });
}

/**
 * 
 */
function initMap() {
    // The location of Cheltenham
    var cheltenham = {lat: 51.89938, lng: -2.0782};
    // The map, centered at Cheltenham
    var leftMap = new google.maps.Map(
    document.getElementById('left-map'), {zoom: 10, center: cheltenham});
    var rightMap = new google.maps.Map(
    document.getElementById('right-map'), {zoom: 10, center: cheltenham});

    mirrorMaps(leftMap, rightMap);


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
