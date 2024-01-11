$(document).ready(function(){
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      method: 'GET',
      success: function(data) {
        var moviesList = $('#list_movies');
        $.each(data.results, function(index, movie) {
          moviesList.append('<li>' + movie.title + '</li>');
        });
      },
      error: function() {
        $('#list_movies').append('<li>Error loading movie information</li>');
      }
    });
  });
  