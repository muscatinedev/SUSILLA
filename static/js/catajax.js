$(function() {


    $(document).on('submit', '#post-form', function (e) {

        e.preventDefault();

        $.ajax({
            type:'POST',
            url:'/recipes/createcategory/',
            data:{
                name:$('#name').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

            },
            success:function (response) {
                alert("succ");
            },
            error:function (jqXHR, exception) {
                alert("err");
            }

        });
    })

});
