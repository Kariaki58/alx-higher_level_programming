$(document).ready(function(){
    $("#btn_translate, #language_code").on('click keypress', function(e){
      if (e.type === 'click' || (e.type === 'keypress' && e.which === 13)) {
        var languageCode = $("#language_code").val();
        $.ajax({
          url: 'https://www.fourtonfish.com/hellosalut/hello/',
          method: 'GET',
          data: { lang: languageCode },
          success: function(data) {
            $('#hello').text(data.hello);
          },
          error: function() {
            $('#hello').text('Error: Language translation not available');
          }
        });
      }
    });
  });
  