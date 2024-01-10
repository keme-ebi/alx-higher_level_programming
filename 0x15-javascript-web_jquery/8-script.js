const $ = window.$;
const url = 'https://swapi-api.alx-tools/api/films/?format=json';

$.get(url, (data, status) => {
  $.each(data.results, (i, movie) => {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
