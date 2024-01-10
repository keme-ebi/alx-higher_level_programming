const $ = window.$;

window.onload = () => {
  $('DIV#add_item').click(() => {
    const newElement = '<li>Item</li>';
    $('UL.my_list').append(newElement);
  });

  $('DIV#remove_item').click(() => {
    $('UL.my_list li:last-child').remove();
  });

  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
};
