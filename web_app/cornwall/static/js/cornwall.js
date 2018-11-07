var Attractions = {
    map: null,
    layers: {
        "BEACHES": { title: "Beaches", icon: "beach.png", kml: "beach.xml" },
        "ENGLISH": { title: "English Heritage", icon: "english_heritage.png", kml: "english_heritage.xml" },
        "FORTS": { title: "Hill Forts", icon: "fort.png", kml: "fort.xml" },
        "MUSEUMS": { title: "Museums", icon: "museum.png", kml: "museum.xml" },
        "NATION_TRUST": { title: "National Trust", icon: "national_trust.png", kml: "national_trust.xml" },
        "PREHISTORIC": { title: "Prehistoric Sites", icon: "prehistoric.png", kml: "prehistoric.xml" },
        "SURFING": { title: "Surfing Beaches", icon: "surfing.png", kml: "surfing.xml" },
        "VISITOR": { title: "Visitor Attractions", icon: "visitor.png", kml: "visitor.xml" }
    }
};


/**
* Show or hide the data layers.
*/
toggleLayer = function (layer, isChecked) {
    var KmlLayer = Attractions.layers[layer]["KmlLayer"]
    if (isChecked) {
        KmlLayer.setMap(Attractions.map);
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
    img.setAttribute('src', 'https://heathmynd.appspot.com/static/cornwall/' + icon);
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
    var latlng = new google.maps.LatLng(50.5, -4.7);
    var myOptions = { zoom: 9, center: latlng, mapTypeId: google.maps.MapTypeId.ROADMAP };
    Attractions.map = new google.maps.Map($("#map_canvas")[0], myOptions);
    for (var layer in Attractions.layers) {
        icon = Attractions.layers[layer].icon;
        title = Attractions.layers[layer].title;
        addCheckBox(layer, icon, title);
        kml = Attractions.layers[layer].kml;
        var kmlLayer = new google.maps.KmlLayer('https://heathmynd.appspot.com/static/cornwall/' + kml,
                {preserveViewport:true});
        Attractions.layers[layer]["KmlLayer"] = kmlLayer;
    }
}

// Call the init function when the page loads.
google.maps.event.addDomListener(window, 'load', initialize)

