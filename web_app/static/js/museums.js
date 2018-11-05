var Museums = {
    map: null,
    layers: {
        "ARTS": { title: "Arts", icon: "arts.png", kml: "arts.xml" },
        "HISTO": { title: "History", icon: "historic.png", kml: "historic.xml" },
        "INDUS": { title: "Industrial", icon: "industrial.png", kml: "industrial.xml" },
        "LOCAL": { title: "Local", icon: "local.png", kml: "local.xml" },
        "MULTI": { title: "Multiple", icon: "multiple.png", kml: "multiple.xml" },
        "OTHER": { title: "Other", icon: "other.png", kml: "other.xml" },
        "TRANS": { title: "Transport", icon: "transport.png", kml: "transport.xml" }
    }
};

/**
* Show or hide the data layers.
*/
toggleLayer = function (layer, isChecked) {
    var KmlLayer = Museums.layers[layer]["KmlLayer"]
    if (isChecked) {
        KmlLayer.setMap(Museums.map);
    }
    else {
        KmlLayer.setMap(null);
    }
};

/**
* Add the check boxes for each of the layers
*/
addCheckBox = function (id, icon, title) {
    var input = document.createElement("input");
    input.type = "checkbox";
    input.id = id;
    input.onclick = function () {
        toggleLayer(this.id, this.checked)
    };
    $("#checkboxes")[0].appendChild(input);
    var img = document.createElement("img");
    img.setAttribute('src', './static/museums/' + icon);
    img.setAttribute('width', 26);
    $("#checkboxes")[0].appendChild(img);
    var text = document.createTextNode(' ' + title);
    $("#checkboxes")[0].appendChild(text);
    var br = document.createElement("br");
    $("#checkboxes")[0].appendChild(br);
}


/**
* Called only once on initial page load to initialize the map.
*/
initialize = function () {
    // Create single instance of a Google Map.
    var latlng = new google.maps.LatLng(51.1, -3.5);
    var myOptions = { zoom: 8, center: latlng, mapTypeId: google.maps.MapTypeId.ROADMAP };
    Museums.map = new google.maps.Map($("#map_canvas")[0], myOptions);
    for (var layer in Museums.layers) {
        icon = Museums.layers[layer].icon;
        title = Museums.layers[layer].title;
        addCheckBox(layer, icon, title);
        kml = Museums.layers[layer].kml;
        var kmlLayer = new google.maps.KmlLayer('http://localhost:8080/static/museums/' + kml,
                {preserveViewport:true});
        Museums.layers[layer]["KmlLayer"] = kmlLayer;
    }
}
// Call the init function when the page loads.
google.maps.event.addDomListener(window, 'load', initialize)