'use strict';
angular
  .module('recipeApp')
  // Let's configure our app with a router.
  .config(function ($routeProvider) { // Inject the route provider module
    // Our first route.  Found at /#/demo
    $routeProvider.when('/recipe', {
      // This route should use the following HTML for its template view.
      templateUrl: 'templates/mainpage.html',
      // This route should use the following controller for it's view.
      controller: 'RecipeController'
    });
  });