const $ = window.$;
const head = $('header');

$('DIV#toggle_header').click(() => {
  head.toggleClass('red');
  head.toggleClass('green');
});
