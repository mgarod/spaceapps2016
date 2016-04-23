// MODULE
var app = angular.module('app', ['ngResource']);


// CONTROLLERS
app.controller('homeController', ['$scope','$resource','$http', function($scope, $resource, $http) {

    $scope.url = "https://data.nasa.gov/resource/y77d-th95.json";


    $http.get($scope.url).then(function(response) {
        $scope.mdata = response.data;
        console.log($scope.mdata);
    });

}]);

