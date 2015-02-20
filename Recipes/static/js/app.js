
var recipeApp = angular.module('recipeApp', []);

//app.controller('RecipeAppCtrl', function ($scope) {
//  $scope.comments = [];
//    $scope.comment = {title:'', body:'', name:''};
//
//    $scope.submitComment = function () {
//      $scope.comments.push($scope.comment);
//      $scope.comment = {title:'', body:'', name:''};
//    };
//});

recipeApp.controller('RecipeListCtrl', function ($scope, $http) {
    var sortDates = function(data){
        var today = new Date();
        var score = null;
        var winner = null;
        for (var key in data){
            var obj = data[key];
            var recipe_date = obj.date;
            var j = new Date(recipe_date);
            var score1 = today - j;
            if (score == null || score1 < score){
                score = score1;
                winner = obj;
            }

        }
        return winner;
    };
        recipeApp.directive("productReviews", function() {
      return {
        restrict: 'E',
        templateUrl: "help.html"
      };
    });
  $http.get('/recipe/').success(function(data) {
    $scope.recipes = data;
      $scope.special = sortDates(data);
      console.log($scope.special)
  });
    $http.get('/tag/').success(function(data){
        $scope.tags = data;
    });
    $http.get('/comment/').success(function(data){
        $scope.comments = data;
        });

});