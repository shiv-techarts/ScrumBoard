(function () {
    'use strict';
    angular.module('scrumboard', [])
        .controller('ScrumBoardController', ['$scope', '$http', ScrumboardController])

    function ScrumboardController($scope, $http) {

        $scope.add = function (list, card_title) {
            var card = {
                list: list.id,
                title: card_title,
            };

            $http.post('api/cards/', card).then(function (response) {
                list.cards.push(response.data);
            },
                function () {
                    alert('Could Not Save Card');
                });

        };

        $scope.data = [];
        $http.get('/api/lists/').then(function (response) {
            $scope.data = response.data;
        },
            function () {
                alert('Not Logged In');
            });
    }

})();
