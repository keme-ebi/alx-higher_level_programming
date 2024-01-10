const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(url, function (data, status) {
  const name = data.name;
  $('DIV#character').text(name);
});
