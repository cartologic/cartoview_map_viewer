/**
 * Created by kamal on 6/28/16.
 */
angular.module('cartoview.mapViewerApp').directive('widgetView', function(urlsHelper) {
    return {
        restrict: 'E',
        transclude: true,
        replace: true,
        scope:{
            widgetName: "@"
        },
        templateUrl: urlsHelper.static + "viewer/angular-templates/view/widget-view.html",
        controller: function($scope, appConfig, widgetsInfo) {
            $scope.config = appConfig;
            $scope.widget = widgetsInfo.get($scope.widgetName);
        }
    }
});
