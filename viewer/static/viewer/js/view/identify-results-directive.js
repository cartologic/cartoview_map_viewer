/**
 * Created by kamal on 7/2/16.
 */

angular.module('cartoview.mapViewerApp').directive('identifyResults',  function(urlsHelper) {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: urlsHelper.static + "viewer/angular-templates/view/identify-results.html",
        controller: function ($scope, identifyService) {
            $scope.identify = identifyService;
        }
    }
});