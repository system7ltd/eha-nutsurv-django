var mappingChecks = {
    initiate: function () {
        mappingChecks.drawMap();
        dataGetter.addNew('/static/sample_data/survey.json', mappingChecks.updateMap);
    },
    drawMap: function () {
        mappingChecks.map = L.map('mapping_checks_map', {
            center: [10.9049100685, 7.7650104523],
            zoom: 6,
            minZoom: 1,
            maxZoom: 18,
            layers: [map.osm],
            fullscreenControl: true,
            fullscreenControlOptions: {
                position: 'topleft'
            }
        });
        mappingChecks.map.attributionControl.setPrefix('');
    },
    mapMarkers: [],
    updateMap: function (data) {
      var group, incorrectSurveys = [];
        _.each(mappingChecks.mapMarkers, function(marker) {
            // Remove all previous markers
            home.map.removeLayer(marker);
        });
        _.each(data.survey_data, function(survey){
            var icon = survey.correct_area ? map.markers.green : map.markers.red,
            marker = L.marker(survey.location, {icon: icon});
            mappingChecks.mapMarkers.push(marker);
            if (survey.correct_area) {
                marker.addTo(mappingChecks.map).bindPopup("Team: "+survey.team);
            } else {
                marker.addTo(mappingChecks.map).bindPopup("ERROR!<br>Team: "+survey.team);
                incorrectSurveys.push(survey);
            }
        });
        group = new L.featureGroup(mappingChecks.mapMarkers);
        mappingChecks.map.fitBounds(group.getBounds());
        mappingChecks.drawAlerts(incorrectSurveys);
    },

    drawAlerts: function (incorrectSurveys) {
        jQuery('#mapping_checks_alerts_list').empty();
        _.each(incorrectSurveys,function(survey){
            jQuery('#mapping_checks_alerts_list').append(mappingChecks.alertTmp(survey));
        });
    },
    alertTmp: _.template('<li>Incorrect placement! Team <%- team %></li>'),

};

mappingChecks.initiate();