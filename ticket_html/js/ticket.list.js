$(function () {
    var get_user = JSON.parse(localStorage.getItem("activeUser"));
    var backend_url = 'http://localhost:9000';
        console.log(data);
            if (data.username && data.password) {
                $.ajax({
                    url: backend_url + '/tickets/',
                    type: "GET",
                    //data: data,
                    //crossDomain: true,
                    //processData: false,
                    //dataType: 'json',
                    //headers: {'content-type': 'application/json;'},
                    success: function (success) {
                        console.log(success);
                     },
                    error: function (error) {
                        console.log(error);
                        $('#error_msg').show();
                        //window.location.href = "index.html";          
            }           
            });

            }
            event.preventDefault();
        });
