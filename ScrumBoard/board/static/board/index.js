(function () {
    'use strict';
    angular.module('scrumboard', [])
        .controller('ScrumBoardController', ['$scope', '$http', ScrumboardController])

    function ScrumboardController($scope, $http) {

        $scope.add = function (list, card_title) {
            var card = {
                title: card_title,
            };

            list.cards.push(card)
        };

        $scope.data = [];
        $http.get('/api/lists').then(function (response) {
            $scope.data = response.data;
        })
    }

})();