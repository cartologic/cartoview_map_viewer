/**
 * Created by kamal on 7/2/16.
 */

angular.module('cartoview.mapViewerApp').directive('cartoviewMap',  function(mapService) {
    return {
        restrict: 'A',
        link:function(scope, element){
            mapService.get().then(function () {
                mapService.map.olMap.setTarget(element[0]);
                mapService.map.olMap.updateSize();
            })
        }
    }
});