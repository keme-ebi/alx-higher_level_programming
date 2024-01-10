const $ = window.$;
const newElement = '<li>Item</li>';
$('DIV#add_item').click(() => {
  $('UL.my_list').append(newElement);
});
