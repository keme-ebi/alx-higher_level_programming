const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(url, (data, status) => {
  const value = data.hello;
  $('DIV#hello').text(value);
});
