var editor = new Quill('.editor'); 

var container = document.getElementById('editor');
var editor = new Quill(container);

var container = $('.editor').get(0);
var editor = new Quill(container);

var options = {
    debug: 'info',
    modules: {
      toolbar: '#toolbar'
    },
    placeholder: 'Compose an epic...',
    readOnly: true,
    theme: 'snow'
  };
  var editor = new Quill('#editor', options);